import sys
import os
import json

def extract_score(value):
    last_underscore = value.rfind("_")
    return int(value[last_underscore+1:])
habitas_path =r"I:\Programs\WetlandProtection\WP20\Ensym\habitas.geojson"
#sys.argv[1]
if not os.path.isfile(habitas_path):
    print ("Requested resource is not a file")
    exit()
path,ext = os.path.splitext(habitas_path)
if ext != '.geojson':
    print ("Requested resource must be geojson")
    exit()
with open(habitas_path,'r') as habitas_file:
    habitas_json = json.load(habitas_file)
    for feature in habitas_json['features']:
        feature['properties']['HH_PAI'] = feature['properties']['EOI']
        feature['properties']['HH_ZI'] = feature['properties']['ZoneNo']
        feature['properties']['HH_SI'] = feature['properties']['SiteNo']
        feature['properties']['VERSION'] = '9.3.1.2 (WCMA Konect)'
        feature['properties']['BNKCND'] = 0
        feature['properties']['ISLRGWOOD'] = 0
        feature['properties']['STLENGTH'] = 0
        feature['properties']['ZC_LT_S'] = extract_score(feature['properties']['ZC_LT_S'])
        feature['properties']['ZC_TCC_S'] = extract_score(feature['properties']['ZC_TCC_S'])
        feature['properties']['ZC_US_S'] = extract_score(feature['properties']['ZC_US_S'])
        feature['properties']['ZC_W_S'] = extract_score(feature['properties']['ZC_W_S'])
        try:
            recrutiment_score = extract_score(feature['properties']['ZC_R_S'])
        except:
            try:
                recrutiment_score = extract_score(feature['properties']['ZC_NWR_S'])
            except:
                recrutiment_score = 0
        feature['properties']['ZC_R_S'] = recrutiment_score
        feature['properties']['ZC_OL_S'] = extract_score(feature['properties']['ZC_OL_S'])
        feature['properties']['ZC_L_S'] = extract_score(feature['properties']['ZC_L_S'])
        if feature['properties']['HH_CP'] == 'Other':
            feature['properties']['HH_CP'] = feature['properties']['HH_CP_O']
outfile = "{0}_habitasify_temp{1}".format(path,ext)

print (outfile)
exit(0)
with open(outfile,'w') as habitas_file:
    habitas_file.write(json.dumps(habitas_json,sort_keys=True, indent=4, separators=(',', ': ')))

    print (habitas_file)
    
ogr_cmd = "ogr2ogr \"{0}.shp\" \"{1}\"".format(path,outfile)
os.system(ogr_cmd)
#os.remove(outfile)
