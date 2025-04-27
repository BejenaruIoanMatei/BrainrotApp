from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image, UnidentifiedImageError
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.image.path)
            
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            if img.height > 400 or img.width > 400:
                output_size = (400,400)
                img.thumbnail(output_size)
                img.save(self.image.path)

        except UnidentifiedImageError:
            print(f"Could not identify image at {self.image.path}")
            
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        