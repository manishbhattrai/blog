from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.



class Post(models.Model):

    published = 'p'
    draft = 'd'

    STATUS_CHOICES = [
        (published,'Published'),
        (draft, 'Draft')
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

            original_slug = self.slug

            count = 1

            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug} - {count}"

                count += 1
        
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', blank=True)
    
    def __str__(self):
        return f"Image for {self.post.title}"


class Comments(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.post} commented by {self.author.username}"
    






