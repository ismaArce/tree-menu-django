from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def has_children(self):
        return self.children.exists()

    def has_active_child(self, current_url):
        return self.children.filter(url=current_url).exists() or any(child.has_active_child(current_url) for child in self.children.all())