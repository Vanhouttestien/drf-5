from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
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

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=12, choices=LANGUAGES, blank=True, null=True)
    language2 = models.CharField(max_length=12, choices=LANGUAGES, blank=True, null=True)
    language3 = models.CharField(max_length=12, choices=LANGUAGES, blank=True, null=True)
    about_me = models.TextField(blank=True, max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


@receiver(post_save, sender=User)    
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)
