from django.db import models

PROPERTY_TYPES = [
    ('land', 'Land'),
    ('plot', 'Plot'),
    ('shop', 'Shop'),
    ('house', 'House'),
    ('kothi', 'Kothi'),
    ('hotel', 'Hotel'),
]

PURPOSE_CHOICES = [
    ('buy', 'Buy'),
    ('rent', 'Rent'),
    ('sell', 'Sell'),
]

class Property(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    purpose = models.CharField(
        max_length=10,
        choices=PURPOSE_CHOICES,
        null=True,
        blank=True
    )
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES,
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='properties/', null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Unnamed Property"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_gallery/')

    def __str__(self):
        return f"Image for {self.property.title if self.property.title else 'Property'}"
