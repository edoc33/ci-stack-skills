#!/usr/bin/env python3
"""Offline fixture/contract validation. No model calls or network access."""
from pathlib import Path
import ast
import copy
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
RESULTS = []

def check(name, condition, detail=''):
    if not condition:
        raise AssertionError(name + ': ' + detail)
    RESULTS.append({'check': name, 'status': 'pass', 'detail': detail})

def readj(path):
    return json.loads((ROOT / path).read_text())

def csvrows(path):
    with (ROOT / path).open(newline='') as stream:
        return list(csv.DictReader(stream))

def pattern_counts(deals, notes):
    eligible = {d['deal_id']: d for d in deals if d['region'] == 'US' and d['segment'] == 'midmarket' and d['competitor'] == 'AcmeFlow'}
    rows = [n for n in notes if n['deal_id'] in eligible and '2026-08-01' <= n['date'] <= '2026-08-06']
    covered = {n['deal_id'] for n in rows}
    positive = {n['deal_id'] for n in rows if n['sso_mentioned'] == 'true'}
    return len(positive), len(covered), len(eligible), len(rows), sorted(positive), sorted(set(eligible) - covered)

def contract_ok(record, generated=True):
    required = ('Event', 'Evidence', 'Business relevance', 'Response', 'Status')
    if not all(field in record for field in required): return False
    ev, resp, st = record['Evidence'], record['Response'], record['Status']
    if ev['Evidence basis'] not in ('observed','field report','inferred'): return False
    if ev['Verification'] not in ('not tested','single-source','corroborated','contradicted','unresolved'): return False
    if ev['Handling'] not in ('public','internal','restricted'): return False
    if resp['Recommended option'] not in ('ignore','continue monitoring','validate','reframe','respond','match','diverge'): return False
    if resp['Recommended option'] in ('ignore','continue monitoring') and not resp.get('Revisit if'): return False
    if not record['Event'].get('Source locator and preserved evidence'): return False
    if not resp.get('Owner and decision deadline'): return False
    if generated and (st['Human decision'],st['Review status'],st['External-use approval']) != ('pending','draft','not approved'): return False
    if not generated and st['Human decision'] != 'pending' and not st.get('Decided by / date'): return False
    return True

def apply_unified(original, patch):
    source = original.splitlines(True)
    result, cursor, in_hunk = [], 0, False
    for line in patch.splitlines(True):
        if line.startswith('--- ') or line.startswith('+++ '): continue
        if line.startswith('@@'):
            match = re.match(r'@@ -(\d+)(?:,\d+)? \+\d+(?:,\d+)? @@', line)
            assert match, 'Invalid hunk'
            start = int(match.group(1)) - 1
            result.extend(source[cursor:start]); cursor=start; in_hunk=True
        elif in_hunk and line.startswith(' '):
            assert source[cursor] == line[1:], 'Patch context mismatch'
            result.append(source[cursor]); cursor += 1
        elif in_hunk and line.startswith('-'):
            assert source[cursor] == line[1:], 'Patch removal mismatch'
            cursor += 1
        elif in_hunk and line.startswith('+'):
            result.append(line[1:])
        elif line.startswith('\\ No newline'): pass
        else: raise AssertionError('Unexpected patch line')
    result.extend(source[cursor:])
    return ''.join(result)

for p in ROOT.rglob('*.json'):
    if '.validation-tmp' not in p.parts and 'session' not in p.parts:
        json.loads(p.read_text())
check('JSON files parse', True)
for p in (ROOT / 'prompts').glob('*.md'):
    check('Prompt fictional label: '+p.name, 'fictional' in p.read_text().lower() or 'ILLUSTRATIVE' in p.read_text())

manifest = readj('evidence/manifest.json')
for e in manifest['evidence']:
    p=ROOT/e['path']
    check('Preserved evidence hash: '+p.name, p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==e['sha256'])
    check('Synthetic evidence marker: '+p.name, e['synthetic'] is True)

sample=readj('reference/original-sample-webhook-payload.json')
event=readj('evidence/change-event.json')
check('Original sample text retained', event['added_text']==sample['added_text'] and event['removed_text']==sample['removed_text'])
for field, path in [('added_text','evidence/pricing-after.txt'),('removed_text','evidence/pricing-before.txt')]:
    body=(ROOT/path).read_text().split('\n\n',1)[1]
    check('Payload text is in preserved '+field, ' '.join(body.split())==event[field])
check('Synthetic event scope explicit', event['fictional'] and event['capture_context']['currency']=='USD')
for value in event['preserved_evidence'].values(): check('Local event evidence resolves: '+value,(ROOT/value).is_file())

triage=readj('worked/01-triage/records.json')
check('Three separate triage propositions',len(triage)==3 and len({b['id'] for b in triage})==3)
for b in triage: check('Contract defaults and action: '+b['id'],contract_ok(b))
patch_brief=readj('inputs/patch-handoff-brief.json')
check('Patch handoff contract/defaults',contract_ok(patch_brief))
check('Patch claim passes current evidence gate',patch_brief['Evidence']['Verification']=='corroborated' and patch_brief['Evidence']['Confidence'].startswith('medium') and patch_brief['Response']['Recommended option'] not in ('ignore','continue monitoring'))
corroboration=readj('worked/02-corroboration/record.json')
check('Original broad claim stays unresolved',corroboration['Answer to original claim'].startswith('unresolved'))
check('Vendor pages share one origin',corroboration['Sources'][0]['origin']==corroboration['Sources'][1]['origin'])
check('Two simulated independent origins explicit',len({s['origin'] for s in corroboration['Sources'][2:]})==2)
check('Corroboration cannot grant approval',corroboration['External-use approval']=='not approved')

original=(ROOT/'inputs/existing-battlecard.md').read_text()
patch=(ROOT/'worked/03-battlecard/battlecard.patch').read_text()
proposed=(ROOT/'worked/03-battlecard/existing-battlecard.proposed.md').read_text()
check('Unified patch applies to supplied card',apply_unified(original,patch)==proposed)
check('Proposed card holds draft approval',all(t in proposed for t in ('AWAITING REVIEW','not for seller use','External-use approval: not approved')))
check('Single-source price/usage held internally',proposed.count('INTERNAL REVIEW NOTE:')==2)
check('Unrelated onboarding preserved','Ask which identity provider, user groups and migration constraints the buyer needs us to support.' in proposed)

counts=pattern_counts(csvrows('inputs/pattern/deals.csv'),csvrows('inputs/pattern/notes.csv'))
expected=readj('worked/04-pattern/counts.json')
check('Independent-deal count and coverage',counts[:4]==(3,6,8,9),str(counts[:4]))
check('Independent cases match expected',counts[4]==expected['occurrence_deal_ids'] and counts[5]==expected['missing_deal_ids'])
check('Pattern conclusion is limited',expected['verdict']=='repeated signal')
report=(ROOT/'worked/04-pattern/2026-08-06-sso-mentions.md').read_text()
for record_id in ('N01','N04','N06'):
    n=next(x for x in csvrows('inputs/pattern/notes.csv') if x['record_id']==record_id)
    check('Representative quote exact: '+record_id,n['quote'] in report)

weekly=readj('inputs/weekly-ci/records.json')
for b in weekly: check('Supplied weekly human history: '+b['id'],contract_ok(b,False))
wc={'accepted':sum(b['Status']['Human decision']=='accepted' for b in weekly),'rejected':sum(b['Status']['Human decision']=='rejected' for b in weekly),'pending':sum(b['Status']['Human decision']=='pending' for b in weekly),'accepted_ignore':sum(b['Status']['Human decision']=='accepted' and b['Response']['Recommended option']=='ignore' for b in weekly)}
we=readj('worked/05-weekly/counts.json')
check('Weekly decisions, pending and ignore counts',all(we[k]==v for k,v in wc.items()),str(wc))
check('Unobserved outcomes remain blank',all(b['Status']['Outcome observed']=='' for b in weekly[1:]))
check('No external approval in fixture history',all(b['Status']['External-use approval']=='not approved' for b in weekly))

for path in ('inputs/candidate-pages.csv','worked/00-portfolio/ci-portfolio-export.csv','inputs/pattern/deals.csv','inputs/pattern/notes.csv'):
    for row in csvrows(path):
        check('CSV formula neutralization: '+path,not any(str(v).lstrip().startswith(('=','+','-','@')) for v in row.values()))
ex=readj('output-excerpts.json')
check('All requested slide excerpts present',{x['slide'] for x in ex['excerpts']}==set(range(24,37)))
for e in ex['excerpts']:
    check('Excerpt source/context boundaries: '+str(e['slide']),e['evidence_kind']=='synthetic' and e['business_context_label']=='Illustrative PMM context' and e['external_use_approval']=='not approved')
    for path in e['source_files']:check('Excerpt source resolves: '+path,(ROOT/path).is_file())

# Negative probes exercise substantive guardrails without altering source files.
changed=copy.deepcopy(triage[0]); changed['Status']['External-use approval']='approved'
check('Negative probe rejects auto-approval',not contract_ok(changed))
changed=copy.deepcopy(triage[1]); changed['Response']['Revisit if']=''
check('Negative probe rejects missing revisit rule',not contract_ok(changed))
changed_notes=csvrows('inputs/pattern/notes.csv'); changed_notes.append(copy.deepcopy(changed_notes[0]))
check('Duplicate-note probe leaves deal fraction unchanged',pattern_counts(csvrows('inputs/pattern/deals.csv'),changed_notes)[:3]==(3,6,8))
check('Hash probe detects changed source bytes',hashlib.sha256((ROOT/'evidence/pricing-after.txt').read_bytes()+b'changed').hexdigest()!=next(x['sha256'] for x in manifest['evidence'] if x['path']=='evidence/pricing-after.txt'))

# Run the setup script in a contained copy. It only writes under the copied kit.
ast.parse((ROOT/'prepare_session.py').read_text())
work=ROOT/'.validation-tmp';work.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(dir=work) as temp:
    target=Path(temp)/'kit';target.mkdir()
    shutil.copy2(ROOT/'prepare_session.py',target/'prepare_session.py')
    shutil.copytree(ROOT/'prompts',target/'prompts')
    shutil.copytree(ROOT/'inputs',target/'inputs')
    result=subprocess.run([sys.executable,str(target/'prepare_session.py')],cwd=target,capture_output=True,text=True)
    check('Session setup executes locally',result.returncode==0,result.stderr.strip())
    paths=json.loads((target/'session/paths.json').read_text())
    check('All generated paths confined to kit',all(Path(v).is_relative_to(target) for v in paths.values()))
    generated=list((target/'session/prompts').glob('*.md'))
    check('Seven exact invocation files generated',len(generated)==7 and all('{{' not in p.read_text() for p in generated))
    check('Original card copy is identical',(target/'session/existing-battlecard.md').read_bytes()==(ROOT/'inputs/existing-battlecard.md').read_bytes())
    second=subprocess.run([sys.executable,str(target/'prepare_session.py')],cwd=target,capture_output=True,text=True)
    check('Setup rerun protects existing session',second.returncode!=0 and 'already exists' in second.stderr)
work.rmdir()

out={'status':'pass','scope':'offline fixture validation','checks_passed':len(RESULTS),'model_runtime_executed_by_this_validator':False,'model_runtime_note':'This validator makes no model calls. See VALIDATION.md and validation/claude-smoke-status.json for the separate runtime test.','checks':RESULTS}
(ROOT/'validation').mkdir(exist_ok=True)
(ROOT/'validation/results.json').write_text(json.dumps(out,indent=2)+'\n')
print(str(len(RESULTS))+' offline checks passed. This validator makes no model calls.')
