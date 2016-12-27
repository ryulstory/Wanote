from django.db import models

class Categories(models.Model):
	Title = models.CharField(max_length=40, null=False)

class TagModel(models.Model)j:
	Title = models.CharField(max_length=20,null=False)

class Photo(models.Model) :
	Category = models.ForeignKey(Categories)
	Tags = models.ManyToManyField(TagModel)
	image_file = models.ImageField(upload_to='static_files/uploaded/%Y')
	filtered_image_file = models.ImageField(upload_to='static_files/uploaded/%Y')
	description = models.TextField(max_length=500, blank=True)
	Comments = models.PositiveSmallIntegerField(default=0, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def delete(self, *args, **kwargs):
		self.image_file.delete()
		self.filtered_image_file.delete()
		super(Photo, self).delete(*args, **kwargs)
class Comments(models.Model):
	Name = models.CharField(max_length=20, null=False)
	Content = models.TextField(max_length=2000, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	photo = models.ForeignKey(Photo)
		

# Create your models here.
