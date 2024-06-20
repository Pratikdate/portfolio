from django.db import models

# Create your models here.



class Personal_About_Me(models.Model):
    Name=models.CharField(max_length=100)
    Short_intro=models.TextField(blank=True,max_length=2000)
    Birthday = models.DateField()
    Age = models.IntegerField()
    Website = models.CharField(max_length=100)
    Degree = models.CharField(max_length=13, )
    PhEmailone = models.EmailField()
    City = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Call = models.CharField(max_length=200)
    Freelance = models.CharField(max_length=200)


    def __str__(self):
        return self.Name
    



class Skill(models.Model):
    skill=models.CharField(max_length=50)
    percent=models.IntegerField()

    def __str__(self):
        return self.skill
    

    


class Professional_About_Me(models.Model):
    Happy_Clients=models.IntegerField()
    Projects=models.IntegerField()
    Hours_Of_Support=models.IntegerField()
    Awards=models.IntegerField()



class Testimonials(models.Model):
    short_intro=models.TextField(blank=True,max_length=2000)
    image=  models.ImageField(upload_to='Testimonials/', null=True, blank=False)
    roal=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,blank=True)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class My_Service(models.Model):
    short_intro=models.TextField(blank=True,max_length=2000)
    logo =  models.ImageField(upload_to='services/', null=True, blank=True)
    boostrap_logo = models.CharField(blank=True,max_length=20)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    


class My_Works(models.Model):
    field=models.CharField(max_length=50)
    short_intro=models.TextField(blank=True,max_length=2000)
    image =  models.ImageField(upload_to='Portfolio/', null=True, blank=True)
    video=models.URLField(blank=True)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.field
    

    
class Messages(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(blank=True,max_length=2000)

    def __str__(self):
        return self.name
