from django.db import models


#defining attributes of djangoClasses objects
class djangoClasses(models.Model):
    title = models.CharField(max_length=30)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=30)
    duration = models.FloatField()


