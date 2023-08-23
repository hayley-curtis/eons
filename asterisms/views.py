from django.shortcuts import render, get_object_or_404
from .models import Culture, Asterism, Stars, Region





def main(request): 
   return render(request, 'asterisms/main.html')

def about(request): 
   return render(request, 'asterisms/about.html')

def index(request):
   culture_list = Culture.objects.order_by('culture_name')
   regionlist = Region.objects.order_by('region_name')
   context = { 'culture_list' : culture_list, 
              'regionlist': regionlist
              }
   return render(request, 'asterisms/index.html', context)


def regions(request, region): 
   regionlist = Region.objects.order_by('region_name')
   regionset= Region.objects.all() #this returns a queryset of all regions
   r = regionset.filter(region_name=region) #this returns a single region that matches region name
   regionname = r[0]
   culturelist = Culture.objects.filter(geographic_region=r[0].pk)
   context = { 'r': r, 
              'culturelist': culturelist,
              'regionlist': regionlist,
              'regionname': regionname,
   }
   return render(request, 'asterisms/regionview.html', context)
   


def culture_detail(request, culture, region):
   regionlist = Region.objects.order_by('region_name')
   c = Culture.objects.get(culture_name = culture)
   cultureregion = c.geographic_region
   asterism = Asterism.objects.filter(culture_id = c.id)
   asterism_list = asterism.order_by('asterism_name')
   context = { 'asterism_list': asterism_list, 
              'c': c,
              'regionlist': regionlist,
              'cultureregion': cultureregion
              }
   return render(request, 'asterisms/culture.html', context)
   

def asterism_detail(request, culture, asterism, region):
   a = Asterism.objects.get(asterism_name = asterism)
   culture = a.culture 
   region = culture.geographic_region
   cultureasterisms = Asterism.objects.filter(culture_id=culture)
   stars = Stars.objects.filter(asterisms = a.id)    
   stars_list = stars.order_by('-star_hip')
   relatedasterismlist = []
   for star in stars_list:
      star.related_asterisms = star.asterisms.all()
      for object in list(star.related_asterisms):
         if object not in relatedasterismlist: 
            relatedasterismlist.append(object)
      #star.is_related = len(star.related_asterisms)
   #decided to change the design of page -- give all related asterisms
   #for a given asterism, not connected to specific stars

      
   context = {'stars_list': stars_list, 
              'a': a,
              #'star.related_asterisms': star.related_asterisms,
              #'star.is_related': star.is_related,
              'relatedasterismlist': relatedasterismlist,
              'culture': culture, 
              'region': region,
              'cultureasterisms': cultureasterisms
             }
   return render(request, 'asterisms/asterism.html', context)



