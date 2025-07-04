from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
    ]
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"
