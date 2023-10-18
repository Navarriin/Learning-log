from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """um topico que o usuario esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """retorna uma apresentaçao de string do modelo"""
        return self.text
    
class Entry(models.Model):
    """algo especifico aprendido sobre um topico"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """retorna uma string simples representando a entrada"""
        if len(self.text) > 50:
            reticence = f'{self.text[:50]}...'
        else: 
            reticence = f'{self.text[:50]}'
        return reticence
    

