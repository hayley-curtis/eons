#what else should I import? 
import os
import sys
import csv

sys.path.append("/Users/hayleycurtis/Desktop/eons/eons_project/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eons_project.settings")


import django
django.setup()

from django.conf import settings 


from asterisms.models import Culture, Asterism, Stars


with open('asterisms/constellationdata/allstarinfo.csv', 'r') as file:
    data = list(csv.reader(file, delimiter=','))
    for line in data: 
        cultureline = str(line[0])
        if cultureline.startswith("kamilaroi-E"):
            cultureline = str(cultureline[:-5])
        elif cultureline.startswith("japanese_moon"):
            cultureline = "japanese moon stations"
        elif cultureline.startswith("arabic_moon"): 
            cultureline = "arabic moon stations"
        elif cultureline.startswith("hawaiian"): 
            cultureline = "hawaiian starlines"
        else:
            cultureline = str(cultureline[:-4])
        asterism_desig = (str(line[1]) + "-" + cultureline[0:3]) #to make each asterism designation unique


        c, create = Culture.objects.get_or_create(culture_name=cultureline)
        a, create = Asterism.objects.get_or_create(asterism_name=asterism_desig, culture=c) 
     
     #to avoid multiple instances -- I set star_hip to pk, so have to check if star is already in database before
     #I relate it to a certain asterism
        star_hip = str(line[2])
        try: 
            s = Stars.objects.get(star_hip=star_hip)
        except: 
            s, create = Stars.objects.get_or_create(star_hip=line[2], star_ra=line[4], star_dec=line[5])
        a.stars_set.add(s)


print("cultures, asterisms and stars have been added to the database -- remember to run the geographic region import script so information about regions and continents can be included")
