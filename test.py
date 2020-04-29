import yaml
import glob
import json
import sys

cnt=0
for certData in glob.glob('**/certifai.yaml', recursive=True):
    try:
        with open(certData) as yamlfile:
            cert = yaml.full_load(yamlfile)
    except yaml.YAMLError as e:
        cnt+=1
        print(f"{certData} - invalid certifai YAML file {e}")

for certData in glob.glob('**/certifai.json', recursive=True):
    try:
        with open(certData) as jsonfile:
            cert = json.load(jsonfile)
    except yaml.YAMLError as e:
        cnt+=1
        print(f"{certData} - invalid certifai JSON file {e}")

for metaData in glob.glob('**/metadata.yaml', recursive=True):
    try:
        with open(metaData) as yamlfile:
            cert = yaml.full_load(yamlfile)
    except yaml.YAMLError as e:
        cnt+=1
        print(f"{metaData} - invalid metadata YAML file {e}")

if cnt > 0:
    print(f"{cnt} errors found")
    sys.exit(1)
