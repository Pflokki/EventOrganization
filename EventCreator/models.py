from django.db import models


class Decoration(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1000)
    image = models.ImageField(upload_to='images/decorations/', null=True)

    @classmethod
    def get_first(cls, _id):
        f_r = cls.objects.filter(id=_id).first()
        if f_r is not None:
            return {'desc': f_r.name, 'price': f_r.price}
        else:
            return {'desc': "-", 'price': "-"}


    @classmethod
    def get_list(cls, event_location_id) -> list:
        _list = []
        for obj in cls.objects.filter(eventlocation__id=event_location_id):
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': str(obj.price),
                'img': obj.image,
                'address': "",
                'description': obj.description
            })
        return _list

    def __str__(self):
        return self.name


class EventLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    decoration = models.ManyToManyField(to='Decoration')

    @classmethod
    def get_first(cls, _id):
        f_r = cls.objects.filter(id=_id).first()
        if f_r is not None:
            return {'desc': f_r.name, 'price': "-"}
        else:
            return {'desc': "-", 'price': "-"}

    @classmethod
    def get_list(cls, event_id) -> list:
        _list = []
        for obj in cls.objects.filter(event__id=event_id):
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': "",
                'img': "",
                'address': "",
                'description': obj.description
            })
        return _list

    def __str__(self):
        return self.name


class ArtistClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    @classmethod
    def get_first(cls, _id):
        f_r = cls.objects.filter(id=_id).first()
        if f_r is not None:
            return {'desc': f_r.name, 'price': "-"}
        else:
            return {'desc': "-", 'price': "-"}

    @classmethod
    def get_list(cls, event_id) -> list:
        _list = []
        for obj in cls.objects.filter(event__id=event_id):
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': "",
                'img': "",
                'address': "",
                'description': obj.description
            })
        return _list

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    event_location = models.ManyToManyField(to="EventLocation")
    artist_class = models.ManyToManyField(to="ArtistClass")

    @classmethod
    def get_first(cls, _id):
        f_r = cls.objects.filter(id=_id).first()
        if f_r is not None:
            return {'desc': f_r.name, 'price': "-"}
        else:
            return {'desc': "-", 'price': "-"}

    @classmethod
    def get_list(cls) -> list:
        _list = []
        for event in cls.objects.all():
            _list.append({
                'id': f"{event.id}",
                'name': event.name,
                'price': "",
                'img': "",
                'address': "",
                'description': event.description
            })
        return _list

    def __str__(self):
        return self.name


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
    def get_first(cls, _id):
        f_r = cls.objects.filter(id=_id).first()
        if f_r is not None:
            return {'desc': f_r.name, 'price': f_r.price}
        else:
            return {'desc': "-", 'price': "-"}

    @classmethod
    def get_list(cls, id_artist_class) -> list:
        _list = []
        for obj in cls.objects.filter(id_artist_class=id_artist_class):
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': str(obj.price),
                'img': obj.image,
                'address': "",
                'description': obj.description
            })
        return _list

    def __str__(self):
        return self.name


class LocationAddress(models.Model):
    id_location = models.ForeignKey(to='EventLocation', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=1000)
    image = models.ImageField(upload_to='images/location/', null=True)

    @classmethod
    def get_first(cls, _id):
        f_r = cls.objects.filter(id=_id).first()
        if f_r is not None:
            return {'desc': f_r.name, 'price': f_r.price}
        else:
            return {'desc': "-", 'price': "-"}

    @classmethod
    def get_list(cls, id_location) -> list:
        _list = []
        for obj in cls.objects.filter(id_location=id_location):
            _list.append({
                'id': f"{obj.id}",
                'name': obj.name,
                'price': str(obj.price),
                'img': obj.image,
                'address': obj.address,
                'description': obj.description
            })
        return _list

    def __str__(self):
        return self.name


class OrderInfo(models.Model):
    p_first_name = models.CharField(max_length=100)
    p_last_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=100)
    p_email = models.EmailField(max_length=100)
    event_time = models.DateField(max_length=100)

    id_event = models.ForeignKey(to='Event', on_delete=models.CASCADE)
    id_location_address = models.ForeignKey(to='LocationAddress', on_delete=models.CASCADE)
    id_decoration = models.ForeignKey(to='Decoration', on_delete=models.CASCADE)
    id_artist = models.ForeignKey(to='Artist', on_delete=models.CASCADE)

    @classmethod
    def save_record(cls, **kwargs):
        oi = OrderInfo()
        oi.p_first_name = kwargs['p_first_name']
        oi.p_last_name = kwargs['p_last_name']
        oi.p_phone = kwargs['p_phone']
        oi.p_email = kwargs['p_email']
        oi.event_time = kwargs['event_time']

        oi.id_event = Event.objects.filter(id=kwargs['id_event']).first()
        oi.id_location_address = LocationAddress.objects.filter(id=kwargs['id_location_address']).first()
        oi.id_decoration = Decoration.objects.filter(id=kwargs['id_decoration']).first()
        oi.id_artist = Artist.objects.filter(id=kwargs['id_artist']).first()

        oi.save()

