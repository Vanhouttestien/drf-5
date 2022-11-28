from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    LANGUAGES = (
    ("english", "English"),
    ("spanish", "Spanish"),
    ("french", "French"),
    ("swedish", "Swedish"),
    ("dutch", "Dutch"),
    ("portuguese", "Portuguese"),
    ("mandarin", "Mandarin"),
    ("hindi", "Hindi "),
)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=12, choices=LANGUAGES, default='1')
    language2 = models.CharField(max_length=12, choices=LANGUAGES, default='1')
    language3 = models.CharField(max_length=12, choices=LANGUAGES, default='1')
    about_me = models.TextField(blank=True, max_length=600)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"
    
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(owner=instance)

    post_save.connect(create_profile, sender=User)

   
