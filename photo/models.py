from django.db import models
class Categories(models.Model):
	Title = models.CharField(max_length=40, null=False)

class Photo(models.Model) :
	#분류
	Categories = models.ForeignKey(Categories)
	#틀린이유
	Content = models.TextField(blank=True)
	image_file = models.ImageField(upload_to='static_files/uploaded/%Y')
	filtered_image_file = models.ImageField(upload_to='static_files/uploaded/%Y')
	description = models.TextField(max_length=500, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def delete(self,*args, **kwargs):
		self.image_file.delete()
		self.filtered_image_file.delete()
		super(Photo, self).delete(*args,**kwargs)
class Comments(models.Model):
	Name = models.CharField(max_length=20, null=False)
	Content = models.TextField(max_length=2000, null=False)
	Created = models.DateTimeField(auto_now_add=True, auto_now=True)
	


# Create your models here.
