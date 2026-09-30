#!/usr/bin/env python3
"""Reproduce B12 working overlap tests. These are not navigational geometries.

Requires shapely and pyproj. Source coordinate facts are in coordinate_extraction.json.
The IMO Vlieland text says European datum. ED50 and the locally matched source
endpoints are sensitivity cases, not certified transformations for navigation.
"""
from pathlib import Path
import json
try:
    from shapely.geometry import Polygon, Point
    from shapely.ops import transform
    from pyproj import Transformer
except ImportError as exc:
    raise SystemExit('This optional geometry check requires shapely and pyproj.') from exc
ROOT=Path(__file__).resolve().parent
source=json.loads((ROOT/'coordinate_extraction.json').read_text())
metric=Transformer.from_crs('EPSG:4326','EPSG:32631',always_xy=True)
ed50=Transformer.from_crs('EPSG:4230','EPSG:4326',always_xy=True)
vts=transform(metric.transform,Polygon(source['Off_Texel_VTS_WGS84']))
CASES={
'TSS-0058':('IMO_Off_Texel_WGS84', {'NE':[1,2,3,4,12,11,10,9,8], 'SW_main':[7,6,5,15,16]}),
'TSS-0059':('IMO_Vlieland_European_datum', {'NE':[11,12,6,2,3,4,5,17,16,15,14,13], 'W':[1,2,23,22], 'SW':[10,9,8,7,6,30,25,26,27,28,29]}),
'TSS-0060':('IMO_Vlieland_European_datum', {'N':[30,33,24,23], 'S':[31,32,34,25]})}
results={}
for tid,(dataset,lanes) in CASES.items():
    pts={int(k):v for k,v in source[dataset].items()};results[tid]={}
    for label,indices in lanes.items():
        raw=Polygon([pts[i] for i in indices])
        if not raw.is_valid:raise ValueError(f'Invalid working lane: {tid}/{label}')
        cases={'WGS84':raw} if 'WGS84' in dataset else {
            'raw_European_coordinates_for_sensitivity_only':raw,
            'ED50_working_assumption':transform(ed50.transform,raw),
            'local_source_endpoint_tie':Polygon([(pts[i][0]-.08/60,pts[i][1]-.05/60) for i in indices])}
        values={}
        for datum,geom in cases.items():
            lane=transform(metric.transform,geom)
            values[datum]={
                'robust_interior_overlap':lane.intersection(vts.buffer(-200)).area>1,
                'robust_outside_area':lane.difference(vts.buffer(200)).area>1,
                'max_vertex_distance_outside_m':round(max(vts.distance(Point(x,y)) for x,y in lane.exterior.coords),2)}
        results[tid][label]={'source_vertices':indices,'tests':values}
# Confirm positive overlap for each scheme; never infer entire coverage from a name.
for tid,lanes in results.items():
    if not any(all(d['robust_interior_overlap'] for d in lane['tests'].values()) for lane in lanes.values()):
        raise ValueError(f'No robust confirmed overlap for {tid}')
for tid in ('TSS-0058','TSS-0059'):
    if not any(all(d['robust_outside_area'] for d in lane['tests'].values()) for lane in results[tid].values()):
        raise ValueError(f'Partial coverage not demonstrated for {tid}')
output={'warning':'Research test, not official geometry or passage instructions. The 200 m sensitivity distance is not a legal boundary buffer.',
        'scope':'Sampled traffic-lane polygons; no inshore traffic zone or excluded manoeuvring area treated as TSS lane.',
        'results':results}
(ROOT/'geometry_checks.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
