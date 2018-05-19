from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name        = models.CharField(max_length=120)
    type1       = models.CharField(max_length=120, blank=True, default=False)
    type2       = models.CharField(max_length=120, blank=True, default=False)
    hp          = models.IntegerField(blank=True, default=False)
    attack      = models.IntegerField(blank=True, default=False)
    defense     = models.IntegerField(blank=True, default=False)
    sp_attack   = models.IntegerField(blank=True, default=False)
    sp_defense  = models.IntegerField(blank=True, default=False)
    speed       = models.IntegerField(blank=True, default=False)
    gen         = models.IntegerField(blank=True, default=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name