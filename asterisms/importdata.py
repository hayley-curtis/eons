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


with open('asterisms/constellationdata/stars_asterisms_main_data.csv', 'r') as file:
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
        asterism_desig = (str(line[1]) + "-" + cultureline[0:3])
    
        d, create = Culture.objects.get_or_create(culture_name=cultureline)
        d, create = Asterism.objects.get_or_create(asterism_name=asterism_desig, culture=d)
        d, create = Stars.objects.get_or_create(star_hip=line[2], star_ra=line[4], star_dec=line[5], asterisms=d)





        #culture = Culture(culture_name=cultureline)
        #asterism = Asterism(asterism_name=line[1], culture=cultureline)
        #stars = Stars(star_hip=line[2], star_ra=line[4], star_dec=line[5], asterism=line[1])
        #try:
           # culture.save()
           # asterism.save()
           # stars.save()
           # print('all done')
      #  except: 
           # print('there was a problem')






          

