from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return "%s " %self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200,blank=True, null=True)
    students = models.ManyToManyField(Student,blank=True, null=True)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return "%s " %self.name