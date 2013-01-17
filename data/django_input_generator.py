import json
from collections import defaultdict

entity_id = {}
issues = []

f = open("activity_list", 'r')
for line in f:
   issues.append(line.strip().capitalize())
f.close()

f = open("concern_list", 'r')
for line in f:
   issues.append(line.strip().capitalize())
f.close()

countries = []
f = open("country_list", 'r')
for line in f:
   countries.append(line.strip().capitalize())
f.close()

orgs = []
f = open("institution_list", 'r')
for line in f:
   orgs.append(line.strip().capitalize())
f.close()

json_list = []
n = 1
for i in range(len(issues)):
   entity_id[issues[i]] = n
   record = {}
   record["model"] = "explore.entity"
   record["pk"] = n
   record["fields"] = {"name": issues[i], "type_of_entity": "IS"}
   json_list.append(record)
   n += 1

for i in range(len(countries)):
   entity_id[countries[i]] = n
   record = {}
   record["model"] = "explore.entity"
   record["pk"] = n
   record["fields"] = {"name": countries[i], "type_of_entity": "CO"}
   json_list.append(record)
   n += 1

for i in range(len(orgs)):
   entity_id[orgs[i]] = n
   record = {}
   record["model"] = "explore.entity"
   record["pk"] = n
   record["fields"] = {"name": orgs[i], "type_of_entity": "OR"}
   json_list.append(record)
   n += 1

f = open("fixture_entity.json", 'w')
f.write(json.dumps(json_list))
f.close()

hits = defaultdict(lambda : defaultdict(int))
rca = defaultdict(lambda : defaultdict(float))
alpha = defaultdict(lambda : defaultdict(float))
beta = defaultdict(lambda : defaultdict(float))

f = open("20120501country_issue_poweregressions_anneal", 'r')
for line in f:
   fields = line.strip().split('\t')
   alpha[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[2])
   alpha[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[2])
   beta[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[3])
   beta[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[3])
f.close()

f = open("20120501country_organization_poweregressions_anneal_2", 'r')
for line in f:
   fields = line.strip().split('\t')
   alpha[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[2])
   alpha[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[2])
   beta[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[3])
   beta[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[3])
f.close()

f = open("20120501organization_issue_poweregressions_anneal_2", 'r')
for line in f:
   fields = line.strip().split('\t')
   alpha[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[2])
   alpha[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[2])
   beta[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[3])
   beta[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[3])
f.close()

f = open("20120501country_issue_rca_aidweb_2", 'r')
for line in f:
   fields = line.strip().split('\t')
   hits[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = int(fields[2])
   hits[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = int(fields[2])
   rca[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[3])
   rca[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[3])
f.close()

f = open("20120501org_country_rca_aidweb", 'r')
for line in f:
   fields = line.strip().split('\t')
   hits[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = int(fields[2])
   hits[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = int(fields[2])
   rca[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[3])
   rca[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[3])
f.close()

f = open("20120501org_issue_rca_aidweb", 'r')
for line in f:
   fields = line.strip().split('\t')
   hits[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = int(fields[2])
   hits[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = int(fields[2])
   rca[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[3])
   rca[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[3])
f.close()

n = 1
json_list = []

for entity1 in hits:
   for entity2 in hits[entity1]:
      record = {}
      record["model"] = "explore.bipartite"
      record["pk"] = n
      record["fields"] = {"entity_src": entity1, "entity_trg": entity2, "hits": hits[entity1][entity2], "rca": rca[entity1][entity2], "alpha": alpha[entity1][entity2], "beta": beta[entity1][entity2]}
      json_list.append(record)
      n += 1

f = open("fixture_bipartite.json", 'w')
f.write(json.dumps(json_list))
f.close()

rank = {}
value = {}
f = open("rankings", 'r')
for line in f:
   fields = line.strip().split('\t')
   rank[entity_id[fields[1].capitalize()]] = fields[0]
   value[entity_id[fields[1].capitalize()]] = fields[2]
f.close()

n = 1
json_list = []
for entity in rank:
   record = {}
   record["model"] = "explore.ranking"
   record["pk"] = n
   record["fields"] = {"entity": entity, "rank": rank[entity], "consistency_value": value[entity]}
   json_list.append(record)
   n += 1

f = open("fixture_rankings.json", 'w')
f.write(json.dumps(json_list))
f.close()
