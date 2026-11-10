"""Build the Pages site from a public, aggregate-only result snapshot (stdlib)."""
import argparse,csv,hashlib,io,json,shutil,statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def snapshot(pilot):
    summary=json.loads((pilot/'report/summary.json').read_text())
    audit=json.loads((pilot/'annotation-audit.json').read_text())
    replay=json.loads((pilot/'replay/latest.json').read_text())
    rows=[json.loads(line) for line in (pilot/'replay'/replay['file']).read_text().splitlines()]
    timing={}
    for model in ('nanodet','yolox_s'):
        values=sorted(r['model_call_ms'] for r in rows if r['model']==model)
        rank=(len(values)-1)*.95;low=int(rank)
        timing[model]={'samples':len(values),'median_ms':statistics.median(values),'p95_ms':values[low]+(values[min(low+1,len(values)-1)]-values[low])*(rank-low)}
    keys=('trial_id','model','object_id','distance_condition','view_condition','motion','frames','visible_frames','absent_frames','hit_rate_iou50','false_positive_rate','median_anchor_error_pct','median_residual_jitter_pct','longest_miss_run_frames','median_model_call_ms','p95_model_call_ms','median_total_ms','fully_reviewed','capture_complete')
    trials=[{k:t[k] for k in keys} for t in summary['trials']]
    means={m:{obj:statistics.mean(t['hit_rate_iou50'] for t in trials if t['model']==m and t['object_id']==obj) for obj in ('sanitizer','toy_motorcycle')} for m in timing}
    value={'updated':'2026-11-10','milestone':'UCLA ECE M202A · Milestone 3','physical_trials':11,'captured_frames':229,'visible_frames':210,'empty_frames':19,'instances':2,'threshold':.35,'iou_threshold':.5,'user_annotations':18,'ai_annotations':211,'ai_annotations_human_verified':False,'flagged_annotations':len(audit['review_flags']),'frame_size':[480,640],'replay_id':replay['run_id'],'source_archive_sha256':audit['source_archive_sha256'],'source_summary_sha256':hashlib.sha256((pilot/'report/summary.json').read_bytes()).hexdigest(),'application_revision':'a4b59406fc0871657621972ffbf2693e544329e9','timing':timing,'condition_means':means,'trials':trials,'limitations':summary['warnings'],'timing_scope':'Saved OpenCV 4.13.0 CPU replay; two threads; native 416/640 inputs; one timed call per frame/model; excludes camera, network and display. CPU model not recorded.'}
    (ROOT/'results.json').write_text(json.dumps(value,indent=2)+'\n')

def build():
    data=json.loads((ROOT/'results.json').read_text())
    assert len(data['trials'])==33 and len({t['trial_id'] for t in data['trials']})==11
    assert all(t['fully_reviewed'] and t['capture_complete'] for t in data['trials'])
    out=ROOT.parent/'site';out.mkdir(exist_ok=True);(out/'data').mkdir(exist_ok=True)
    table=[]
    for trial in sorted({t['trial_id'] for t in data['trials']}):
        models={t['model']:t for t in data['trials'] if t['trial_id']==trial};t=models['nanodet']
        obj={'sanitizer':'Sanitizer','toy_motorcycle':'Toy motorcycle','empty_scene':'Empty scene'}[t['object_id']]
        condition=' / '.join(t[k].replace('_',' ') for k in ('distance_condition','view_condition','motion')) if t['object_id']!='empty_scene' else 'Both targets removed'
        rates=[]
        for name in ('live_nanodet','nanodet','yolox_s'):
            row=models[name];rate=row['hit_rate_iou50'];n=row['visible_frames']
            rates.append(f'<td><strong>{rate*100:.1f}%</strong><span>{round(rate*n)}/{n} frames</span></td>' if rate is not None else '<td><strong>0/19</strong><span>false-positive frames</span></td>')
        table.append(f'<tr data-object="{t["object_id"]}"><th scope="row">{obj}<span>{condition}</span></th>'+''.join(rates)+'</tr>')
    template=(ROOT/'index.html').read_text()
    rendered=template.replace('<!-- RESULT_ROWS -->','\n'.join(table)).replace('/* RESULT_DATA */',json.dumps(data).replace('<','\\u003c'))
    for model,values in data['condition_means'].items():
        for obj,rate in values.items():rendered=rendered.replace('{{'+model+'_'+obj+'}}',f'{rate*100:.1f}')
    assert '{{' not in rendered and '<!-- RESULT_ROWS -->' not in rendered
    (out/'index.html').write_text(rendered)
    for name in ('styles.css','app.js'):shutil.copyfile(ROOT/name,out/name)
    shutil.copyfile(ROOT/'results.json',out/'data/results.json')
    with (out/'data/trial-metrics.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(data['trials'][0]));w.writeheader();w.writerows(data['trials'])
    (out/'.nojekyll').touch()
    print(f'Built {out}: 11 trials, 229 frames, 33 trial/model records. Public aggregate data only.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',type=Path,help='Refresh public snapshot from a completed local pilot');a=parser.parse_args()
    if a.pilot:snapshot(a.pilot)
    build()
