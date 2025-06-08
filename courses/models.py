# yourapp/models.py
from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
  

class Course(models.Model):
    course_title = models.CharField(max_length=255)
    description = models.TextField()

    instructor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'}, 
        related_name='courses'
    )

    content_list = models.JSONField(default=list)
    course_cover_image = models.ImageField(upload_to='course_images/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses'
    )
    price=models.IntegerField(max_length=4)

    def __str__(self):
        return self.course_title

class Course_Module(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True)
    module_no= models.IntegerField()
    module_name= models.TextField(max_length=300)


    def __str__(self):
        return f"Title: {self.course.course_title} -> Module No: {self.module_no}"
    
class Course_Video(models.Model):
    module = models.ForeignKey(Course_Module,on_delete=models.CASCADE,blank=True)
    lecture_no = models.IntegerField()
    video_title = models.TextField(max_length=250)
    video= models.FileField(upload_to='course_video/')
    

    def __str__(self):
        return f"Course Name: {self.module.course.course_title} -> Course Module: {self.module.module_name} -> Course Video: {self.lecture_no}"


