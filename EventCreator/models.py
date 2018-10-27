from django.db import models


class Event(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class EventLocation(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Event_EventLocation(models.Model):
    id_Event = models.ForeignKey(to='Event', on_delete=models.CASCADE)
    id_EventLocation = models.ForeignKey(to='EventLocation', on_delete=models.CASCADE)


class ArtistClass(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Event_ArtistClass(models.Model):
    id_Event = models.ForeignKey(to='Event', on_delete=models.CASCADE)
    id_ArtistClass = models.ForeignKey(to='ArtistClass', on_delete=models.CASCADE)


class Artist(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    id_ArtistClass = models.ForeignKey(to='ArtistClass', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    description = models.CharField(max_length=200)
    src_img = models.CharField(max_length=200)


class Decoration(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Decoration_EventLocation(models.Model):
    id_Decoration = models.ForeignKey(to='Decoration', on_delete=models.CASCADE)
    id_EventLocation = models.ForeignKey(to='EventLocation', on_delete=models.CASCADE)


class LocationAddress(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)

    id_location = models.ForeignKey(to='EventLocation', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    address = models.CharField(max_length=200)
    src_img = models.CharField(max_length=200)


class OrderInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)

    p_first_name = models.CharField(max_length=100)
    p_last_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=100)
    p_email = models.EmailField(max_length=100)
    event_time = models.DateTimeField(max_length=100)

    id_event = models.ForeignKey(to='Event', on_delete=models.CASCADE)
    id_location_address = models.ForeignKey(to='LocationAddress', on_delete=models.CASCADE)
    id_decoration = models.ForeignKey(to='Decoration', on_delete=models.CASCADE)
    id_artist = models.ForeignKey(to='Artist', on_delete=models.CASCADE)
