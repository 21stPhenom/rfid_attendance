from django.db import models

# Create your models here.
class Tag(models.Model):
    serial_number = models.PositiveIntegerField()
    tag_id = models.CharField(max_length=15)
    assigned = models.BooleanField(default=False)

    class Meta:
        ordering = ('serial_number',)

    def __str__(self):
        return f'{self.serial_number} ----> {self.tag_id}'

class TestTag(Tag):
    pass

class Trainee(models.Model):
    _track_choices = {'1': 'Web Development', '2': 'Robotics', '3': 'Scratch'}
    
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    track = models.CharField(max_length=200, choices=_track_choices)
    tag = models.OneToOneField(Tag, on_delete=models.CASCADE, related_name='trainee')
    date_created = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_joined',)
    
    def __str__(self):
        return f'{self.name} in {self.track}' 
    
    @property
    def name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
    
class Entry(models.Model):
    _entry_choices = {'0': 'sign-in', '1': 'sign-out'}
    
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE, related_name='entries')
    date_added = models.DateTimeField(auto_now_add=True)
    entry_status = models.CharField(max_length=10, choices=_entry_choices)
    
    class Meta:
        ordering = ('-date_created',)
    
    def __str__(self):
        return f'{self.entry_status} by {self.trainee.name} with {self.trainee.tag.tag_id}'