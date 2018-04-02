from django.db import models

# Model
class ImageModel(models.Model):
	img = models.ImageField(width_field="width_field", height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	def __str__(self):
		return str(self.id)