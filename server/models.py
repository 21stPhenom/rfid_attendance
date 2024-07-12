from django.db import models

# Create your models here.
class Tag(models.Model):
    serial_number = models.CharField(max_length=3)
    tag_id = models.CharField(max_length=15)
    assigned = models.BooleanField(default=False)

    class Meta:
        ordering = ('serial_number',)

    def __str__(self):
        return f'{self.serial_number} ----> {self.tag_id}'

class TestTag(Tag):
    pass