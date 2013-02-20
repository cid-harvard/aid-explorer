import json
from collections import defaultdict

entity_id = {}
issues = []

issue_attrs = defaultdict(lambda : defaultdict(str))
f = open("activity_list", 'r')
for line in f:
   issue = line.strip().capitalize()
   issues.append(issue)
   issue_attrs[issue]["subtype"] = "activity"
f.close()

f = open("concern_list", 'r')
for line in f:
   issue = line.strip().capitalize()
   issues.append(issue)
   issue_attrs[issue]["subtype"] = "concern"
f.close()

f = open("20120501issue_pop", 'r')
for line in f:
   fields = line.strip().split('\t')
   issue_attrs[fields[0].capitalize()]["size"] = fields[1]
f.close()

countries = []
f = open("country_list", 'r')
for line in f:
   countries.append(line.strip().capitalize())
f.close()

country_attrs = defaultdict(lambda : defaultdict(str))
f = open("20120501country_pop_region", 'r')
for line in f:
   fields = line.strip().split('\t')
   country_attrs[fields[0].capitalize()]["size"] = fields[2]
   if "Europe" in fields[1]:
      fields[1] = "05_Europe"
   elif fields[1] == "15_Melanesia" or fields[1] == "12_South-eastern_Asia":
      fields[1] = "11_Eastern_Asia"
   country_attrs[fields[0].capitalize()]["subtype"] = fields[1]
f.close()

orgs = []
f = open("institution_list", 'r')
for line in f:
   orgs.append(line.strip().capitalize())
f.close()

org_attrs = defaultdict(lambda : defaultdict(float))
f = open("20120501org_betweenness_issuercaentropy", 'r')
for line in f:
   fields = line.strip().split('\t')
   org_attrs[fields[0].capitalize()]["size"] = float(fields[1])
   org_attrs[fields[0].capitalize()]["entropy"] = float(fields[2])
f.close()

x = defaultdict(float)
y = defaultdict(float)
f = open("networks_xy", 'r')
for line in f:
   fields = line.strip().split('\t')
   x[int(fields[0])] = float(fields[1])
   y[int(fields[0])] = float(fields[2])
f.close()

json_list = []
n = 1
for i in range(len(issues)):
   entity_id[issues[i]] = n
   record = {}
   record["model"] = "explore.entity"
   record["pk"] = n
   record["fields"] = {"name": issues[i], "type_of_entity": "IS", "x": x[n], "y": y[n], "entropy": 0.0, "size": float(issue_attrs[issues[i]]["size"]), "subtype": issue_attrs[issues[i]]["subtype"]}
   json_list.append(record)
   n += 1

for i in range(len(countries)):
   entity_id[countries[i]] = n
   record = {}
   record["model"] = "explore.entity"
   record["pk"] = n
   record["fields"] = {"name": countries[i], "type_of_entity": "CO", "x": x[n], "y": y[n], "entropy": 0.0, "size": float(country_attrs[countries[i]]["size"]), "subtype": country_attrs[countries[i]]["subtype"]}
   json_list.append(record)
   n += 1

for i in range(len(orgs)):
   entity_id[orgs[i]] = n
   record = {}
   record["model"] = "explore.entity"
   record["pk"] = n
   record["fields"] = {"name": orgs[i], "type_of_entity": "OR", "x": x[n], "y": y[n], "entropy": org_attrs[orgs[i]]["entropy"], "size": org_attrs[orgs[i]]["size"], "subtype": "N/A"}
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
   if fields[0].capitalize() in entity_id and fields[1].capitalize() in entity_id:
      alpha[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[2])
      alpha[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[2])
      beta[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[3])
      beta[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[3])
f.close()

f = open("20120501country_organization_poweregressions_anneal_2", 'r')
for line in f:
   fields = line.strip().split('\t')
   if fields[0].capitalize() in entity_id and fields[1].capitalize() in entity_id:
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
   if fields[0].capitalize() in entity_id and fields[1].capitalize() in entity_id:
      hits[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = int(fields[2])
      hits[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = int(fields[2])
      rca[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]] = float(fields[3])
      rca[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]] = float(fields[3])
f.close()

f = open("20120501org_country_rca_aidweb", 'r')
for line in f:
   fields = line.strip().split('\t')
   if fields[0].capitalize() in entity_id and fields[1].capitalize() in entity_id:
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

edges = defaultdict(lambda : defaultdict(lambda : defaultdict(str)))

f = open("20120501org_org_rca_aidweb_undir_mst_453", 'r')
for line in f:
   fields = line.strip().split('\t')
   edges[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]]["weight"] = fields[2]
   edges[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]]["weight"] = fields[2]
   edges[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]]["type"] = "1"
   edges[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]]["type"] = "1"
f.close()

f = open("20120524country_country_rca_aidweb_rca1", 'r')
for line in f:
   fields = line.strip().split('\t')
   if fields[0].capitalize() in entity_id and fields[1].capitalize() in entity_id:
      edges[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]]["weight"] = fields[2]
      edges[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]]["weight"] = fields[2]
      edges[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]]["type"] = "2"
      edges[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]]["type"] = "2"
f.close()

f = open("20120524issue_issue_rca_aidweb_rca1", 'r')
for line in f:
   fields = line.strip().split('\t')
   edges[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]]["weight"] = fields[2]
   edges[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]]["weight"] = fields[2]
   edges[entity_id[fields[0].capitalize()]][entity_id[fields[1].capitalize()]]["type"] = "3"
   edges[entity_id[fields[1].capitalize()]][entity_id[fields[0].capitalize()]]["type"] = "3"
f.close()

n = 1
json_list = []
for entity1 in edges:
   for entity2 in edges[entity1]:
      record = {}
      record["model"] = "explore.edge"
      record["pk"] = n
      record["fields"] = {"entity_src": entity1, "entity_trg": entity2, "weight": float(edges[entity1][entity2]["weight"]), "type": int(edges[entity1][entity2]["type"])}
      json_list.append(record)
      n += 1

f = open("fixture_edges.json", 'w')
f.write(json.dumps(json_list))
f.close()
