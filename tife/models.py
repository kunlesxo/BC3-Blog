from django.db import models

class Tife(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, unique=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to="Tife_image")
    video = models.FileField(upload_to="Tife_video")
    audio = models.FileField(upload_to="Tife_audio")
    hastag = models.CharField(max_length=50, null=True)
    created_at= models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_at"]

    def ___str__(self):
        return self.title

class category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Tife, on_delete=models.CASCADE, related_name='comment') 
    author = models.CharField(max_length=100 )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    class meta:
        ordering = ['-created_at']         


    def __str__ (self):
        return f"comment by {self.author} on {self.post.title}"

class like(models.Model):
    id = models.AutoField(primary_key=True)
    like = models.BooleanField(default=True)
    tife = models.ForeignKey(Tife, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class meta:
        ordering = ['-created_at']         

    

