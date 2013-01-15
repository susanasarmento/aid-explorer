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
   relations = models.ManyToManyField('self', through = 'Bipartite', symmetrical = False)

class Bipartite_manager(models.Manager):
   pass

class Bipartite(models.Model):
   entity_src = models.ForeignKey(Entity)
   entity_trg = models.ForeignKey(Entity)
   hits = models.IntegerField()
   rca = models.FloatField()
   alpha = models.FloatField()
   beta = models.FloatField()
