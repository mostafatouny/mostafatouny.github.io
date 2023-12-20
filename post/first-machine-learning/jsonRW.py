import json

def readJson( name ):
	with open(name+'.json', 'r') as inp:
		return json.load(inp)

def writeJson( data, name ):
	with open(name+'.json', 'w') as out:
		json.dump(data, out, sort_keys=True, indent='\t')
