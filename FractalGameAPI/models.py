from django.db import models
		
class MandelbrotRoute(models.Model):
	level 	= models.IntegerField(default=0)
	route 	= models.TextField(default='')
