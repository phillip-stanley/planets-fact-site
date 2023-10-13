from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Planet.Status.PUBLISHED)


class Planet(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    name = models.CharField(max_length=7)
    slug = models.SlugField(max_length=7, unique_for_date='created_at')
    link = models.CharField(max_length=250)
    rotation_time = models.DecimalField(max_digits=5, decimal_places=2)
    revolution_time = models.DecimalField(max_digits=5, decimal_places=2)
    radius = models.DecimalField(max_digits=6, decimal_places=1)
    average_temp = models.IntegerField()
    overview = models.TextField()
    overview_img = models.ImageField(upload_to='uploads/')
    internal_structure = models.TextField()
    internal_structure_img = models.ImageField(upload_to='uploads/')
    surface_geology = models.TextField()
    surface_geology_img = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
            max_length=2,
            choices=Status.choices,
            default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return self.name
