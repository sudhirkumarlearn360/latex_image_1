from django.db import models

# Create your models here.
class LatexImage(models.Model):
	server_image_path = models.CharField(max_length=800) #formula can be very long
	# local_image = models.ImageField(upload_to='img/latex/', null=True, blank=True)

	added_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'latex_image'

	def __str__(self):
		return '%s (%s)' % (self.server_image_path, self.id)