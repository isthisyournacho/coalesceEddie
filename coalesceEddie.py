import json
import glob

i = 0

for filename in glob.glob('*.replay'):
    json_data = open(filename, "r")
    print "Processing " + filename
    if (i > 0):
        parsed_json2 = json.load(json_data)
        parsed_json["Conversations"].append(parsed_json2["Conversations"][0])  # add 1st element from array
    if (i == 0):
        parsed_json = json.load(json_data)
        i+=1

print json.dumps(parsed_json) #collapsed json

f = open("output.replay", "w")
f.write(json.dumps(parsed_json, indent=4))
print "Check output.replay for a prettier version :p"