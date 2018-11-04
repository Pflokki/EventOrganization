from django.db import models


class Decoration(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1000)
    image = models.ImageField(upload_to='images/decorations/', null=True)

    @classmethod
    def get_list(cls) -> list:
        _list = []
        for obj in cls.objects.all():
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': str(obj.price),
                'img': obj.image,
                'description': obj.description
            })
        return _list


class EventLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    decoration = models.ManyToManyField(to='Decoration')

    @classmethod
    def get_list(cls) -> list:
        _list = []
        for obj in cls.objects.all():
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': "",
                'img': "",
                'description': obj.description
            })
        return _list


class ArtistClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    @classmethod
    def get_list(cls) -> list:
        _list = []
        for obj in cls.objects.all():
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': "",
                'img': "",
                'description': obj.description
            })
        return _list


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    event_location = models.ManyToManyField(to="EventLocation")
    artist_class = models.ManyToManyField(to="ArtistClass")

    @classmethod
    def get_list(cls) -> list:
        _list = []
        for event in cls.objects.all():
            _list.append({
                'id': f"{event.id}",
                'name': event.name,
                'price': "",
                'img': "",
                'description': event.description
            })
        return _list


class Artist(models.Model):
    id_artist_class = models.ForeignKey(to='ArtistClass', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1000)
    image = models.ImageField(upload_to='images/artist/', null=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_list(cls) -> list:
        _list = []
        for obj in cls.objects.all():
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': str(obj.price),
                'img': obj.image,
                'description': obj.description
            })
        return _list


class LocationAddress(models.Model):
    id_location = models.ForeignKey(to='EventLocation', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=1000)
    image = models.ImageField(upload_to='images/location/', null=True)

    @classmethod
    def get_list(cls) -> list:
        _list = []
        for obj in cls.objects.all():
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': str(obj.price),
                'img': obj.image,
                'description': f"{obj.address}{obj.description}"
            })
        return _list


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
