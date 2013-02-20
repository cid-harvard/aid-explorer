from django.db import models

class Entity(models.Model):
   name = models.CharField(max_length = 256)
   COUNTRY = 'CO'
   ORGANIZATION = 'OR'
   ISSUE = 'IS'
   TYPE_OF_ENTITY_CHOICES = (
      (COUNTRY, 'Country'),
      (ORGANIZATION, 'Organization'),
      (ISSUE, 'Issue'),
   )
   type_of_entity = models.CharField(max_length = 2, choices = TYPE_OF_ENTITY_CHOICES)
   subtype = models.CharField(max_length = 256)
   entropy = models.FloatField()
   size = models.FloatField()
   x = models.FloatField()
   y = models.FloatField()
   bipartite_relations = models.ManyToManyField('self', through = 'Bipartite', symmetrical = False, related_name = "bipartite")
   edge_relations = models.ManyToManyField('self', through = 'Edge', symmetrical = False, related_name = "edge")

class Bipartite(models.Model):
   entity_src = models.ForeignKey(Entity, related_name = "bipartite_entity_src")
   entity_trg = models.ForeignKey(Entity, related_name = "bipartite_entity_trg")
   hits = models.IntegerField()
   rca = models.FloatField()
   alpha = models.FloatField()
   beta = models.FloatField()

class Edge(models.Model):
   entity_src = models.ForeignKey(Entity, related_name = "edge_entity_src")
   entity_trg = models.ForeignKey(Entity, related_name = "edge_entity_trg")
   weight = models.FloatField()
   type = models.IntegerField()

class Ranking(models.Model):
   entity = models.ForeignKey(Entity)
   consistency_value = models.FloatField()
   rank = models.IntegerField()
