import yaml

with open("params.yaml") as f:
     list_doc = yaml.safe_load(f)

     documents = yaml.safe_load(f)

print(list_doc)
for sense in list_doc:
    if sense == "featurize":
         list_doc[sense]["max_features"] = list_doc[sense]["max_features"]*2

with open("params.yaml", "w") as f:
    yaml.dump(list_doc, f)