from django.db import models
from django.conf import settings
from django.utils import timezone


# >> model for posting within blog <<
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) # >> link to another module <<
    title = models.CharField(max_length = 200) # >> define text w/ char limit <<
    text = models.TextField() # >> define text w/o char limit <<
    created = models.DateTimeField(default = timezone.now) # >> date and time of creation <<
    published = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published = timezone.now()
        self.save()

        def __str__(self):
            return self.title