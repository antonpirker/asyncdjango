from django.db import models

class Pokemon(models.Model):
    number = models.PositiveIntegerField('PokeDex index number')
    name = models.CharField('Name of the Pokemon', max_length=100)

    type1 = models.CharField('Type of Pokemon', max_length=50)
    type2 = models.CharField('Other Type of Pokemon', max_length=50)

    hp = models.IntegerField('Hit Points')
    attack = models.IntegerField('Attack Strength')
    defense = models.IntegerField('Defensive Strength')
    sp_atk = models.IntegerField('Special Attack Strength')
    sp_def = models.IntegerField('Special Defensive Strength')
    speed = models.IntegerField('Speed')
    generation = models.IntegerField('Generation')
    legendary = models.BooleanField('Legendary Pokemon?', default=False)

    class Meta:
        ordering = ('number', 'name')
