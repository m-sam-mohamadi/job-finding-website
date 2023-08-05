from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('title',)

class Job(models.Model):
    category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    positionSalary = models.CharField(max_length=255)
    positionLocation = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    companyLocation = models.CharField(max_length=255)
    companyEmail = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-createdAt',)

    def createdAtFormatted(self):
        return defaultfilters.date(self.createdAt, 'M d, Y')
