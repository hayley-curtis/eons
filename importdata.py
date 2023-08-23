#what else should I import? 
import sys
import os
import csv



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eons_project.settings') #what does this do 
                      
import django 
django.setup()

from django.conf import settings 

from asterisms.models import Culture, Asterism, Stars




def add_Culture(data1):
    d, created  = Culture.objects.get_or_create(culture_name=data1) #what exactly does created do here?

    return d 

def add_Asterism(data1, data2):
    d = Asterism.objects.get_or_create(asterism_name=data1, culture=data2)

    return d

def add_Stars(data1, data2, data3, data4):
    d = Stars.objects.get_or_create(star_hip=data1, star_ra=data2, star_dec=data3, asterism=data4)

    return d 



def importelements(): 
    with open("allstarinfo") as file: 
        data = list(csv.reader(file, delimiter=','))
        for line in data: 
            cultureline = str(line[0])
            if cultureline.startswith("kamilaroi-E"):
                cultureline = str(cultureline[:-5])
            else:
                cultureline = str(cultureline[:-4])
            culture_name = cultureline
            asterism_const = line[1]
            culture = cultureline
            star_hip = line[2]
            star_ra = line[4]
            star_dec = line[5]
            asterism = line[1]


importelements()


