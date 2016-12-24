from django.db import models
class Photo(models.Model) :
	image_file = models.ImageField(upload_to='static_files/uploaded/%Y')
	filtered_image_file = models.ImageField(upload_to='static_files/uploaded/%Y')
	description = models.TextField(max_length=500, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def delete(self,*args, **kwargs):
		self.image_file.delete()
		self.filtered_image_file.delete()
		super(Photo, self).delete(*args,**kwargs)


# Create your models here.
