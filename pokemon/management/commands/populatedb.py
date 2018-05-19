from django.core.management.base import BaseCommand
from pokemon.models import Pokemon

import csv
from itertools import islice

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("Pokemon.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['Name']
                if "Mega" in name:
                    continue

                number = row['#']
                gen = row['Generation']
                type1 = row['Type 1'].capitalize()
                type2 = row['Type 2'].capitalize()

                hp = row['HP']
                attack = row['Attack']
                defense = row['Defense']
                sp_attack = row['Sp. Atk']
                sp_defense = row['Sp. Def']
                speed = row['Speed']
                total = row['Total']

                p = Pokemon.objects.create(name=name, number=number, type1=type1, type2=type2, hp=hp, attack=attack, defense=defense, sp_attack=sp_attack, sp_defense=sp_defense, total=total, speed=speed, gen=gen)