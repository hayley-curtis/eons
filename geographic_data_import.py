import os 
import sys 
import csv 

sys.path.append("/Users/hayleycurtis/Desktop/eons/eons_project/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eons_project.settings")
 
import django 
django.setup()

from django.conf import settings

from asterisms.models import Culture, Continent, Region

with open('asterisms/constellationdata/asterism_regions.csv', 'r') as file: 
        data = list(csv.reader(file, delimiter=','))
        for line in data: 
            culture = line[0]
            region = line[1]
            continent = line[2]
            #to check if continent already in database 
            try: 
                con = Continent.objects.get(continent_name=continent)
            except: 
                con, create = Continent.objects.get_or_create(continent_name=continent)
            #to check if region already in database, if not, adds to db 
            try: 
                 r = Region.objects.get(region_name=region)
            except: 
                 r, create = Region.objects.get_or_create(region_name=region, continent=con)
            #updates culture to include geographic regions 
            c = Culture.objects.get(culture_name=culture) 
            c.geographic_region = r 
            c.save()

