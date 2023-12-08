from django.db import models

class Chat(models.Model):
    user_input = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class SadSongs(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title

class HappySongs(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title

class CalmSongs(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField(upload_to='images')
    audio_file = models.FileField(blank=True,null=True, upload_to='audio_files')
    audio_link = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title
    
class MotivationalSongs(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField(upload_to='images')
    audio_file = models.FileField(blank=True,null=True, upload_to='audio_files')
    audio_link = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title