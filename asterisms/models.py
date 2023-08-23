from django.db import models

class Continent(models.Model):
    continent_name = models.CharField(max_length=200)

    def __str__(self):
        return self.continent_name 
    


class Region(models.Model): 
    region_name = models.CharField(max_length=200)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.region_name
    


class Culture(models.Model): 
    culture_name = models.CharField(max_length=200)
    geographic_region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True) 
    culture_desc = models.CharField(max_length=1000, blank=True, null=True)
    culture_img = models.CharField(max_length=30, blank=True, null=True)
    culture_img_2 = models.CharField(max_length=30, blank=True, null=True)
    

    def __str__(self): 
        return self.culture_name
    

class Asterism(models.Model): 
    asterism_name = models.CharField(max_length=200)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    asterism_desc = models.CharField(max_length=1000, blank=True, null=True)
    asterism_img = models.CharField(max_length=30, blank=True, null=True)
    asterism_img_2 = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self): 
        return self.asterism_name


class Stars(models.Model):
    star_hip = models.IntegerField(primary_key=True)
    star_ra = models.FloatField()
    star_dec = models.FloatField()
    asterisms = models.ManyToManyField(Asterism)

   # def __str__(self): 
       # return self.star_hip


    #gives error django.db.utils.OperationalError: foreign key mismatch - "asterisms_stars_asterisms" referencing "asterisms_stars"
    #I am not sure what is going wrong here -- i want to try to set the star_hip as PK, since there should only be one of each 
    #but idk how to implement this in my import script




