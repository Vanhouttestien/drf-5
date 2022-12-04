from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    LANGUAGES = (
        ("english", "English"),
        ("spanish", "Spanish"),
        ("french", "French"),
        ("swedish", "Swedish"),
        ("dutch", "Dutch"),
        ("portuguese", "Portuguese"),
        ("mandarin", "Mandarin"),
        ("hindi", "Hindi "),
        ("chinese", "Chinese"),
        ("japanese", "Japanese"),
        ("korean", "Korean"),
        ("russian", "Russian"),
        )
        
    LEVEL = (
        ("beginners", "Beginners"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        )
    
    AGE = (
        ("4-7", "4-7"),
        ("7-11", "7-11"),
        ("11-13", "11-13"),
        ("14-17", "14-17"),
        ("18+", "18+")
        )
    title = models.CharField(max_length=250, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=12, choices=LANGUAGES, default='1')
    age = models.CharField(choices=AGE, max_length=8, default='1')
    level = models.CharField(choices=LEVEL, max_length=50, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='uploads/', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.id} {self.title}'
