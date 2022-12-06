from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    LANGUAGES = (
        ("English", "English"),
        ("Spanish", "Spanish"),
        ("French", "French"),
        ("Swedish", "Swedish"),
        ("Dutch", "Dutch"),
        ("Portuguese", "Portuguese"),
        ("Mandarin", "Mandarin"),
        ("Hindi", "Hindi "),
        ("Chinese", "Chinese"),
        ("Japanese", "Japanese"),
        ("Korean", "Korean"),
        ("Russian", "Russian"),
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
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=12, choices=LANGUAGES, default='English')
    age = models.CharField(choices=AGE, max_length=8, default='4-7')
    level = models.CharField(choices=LEVEL, max_length=50, default='beginners')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='uploads/', blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.id} {self.title}'
