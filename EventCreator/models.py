from django.db import models


class Decoration(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class EventLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    decoration = models.ManyToManyField(to='Decoration')


class ArtistClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    event_location = models.ManyToManyField(to="EventLocation")
    artist_class = models.ManyToManyField(to="ArtistClass")


class Artist(models.Model):
    id_artist_class = models.ForeignKey(to='ArtistClass', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/artist/')


class LocationAddress(models.Model):
    id_location = models.ForeignKey(to='EventLocation', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/location/')


class OrderInfo(models.Model):
    p_first_name = models.CharField(max_length=100)
    p_last_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=100)
    p_email = models.EmailField(max_length=100)
    event_time = models.DateTimeField(max_length=100)

    id_event = models.ForeignKey(to='Event', on_delete=models.CASCADE)
    id_location_address = models.ForeignKey(to='LocationAddress', on_delete=models.CASCADE)
    id_decoration = models.ForeignKey(to='Decoration', on_delete=models.CASCADE)
    id_artist = models.ForeignKey(to='Artist', on_delete=models.CASCADE)
