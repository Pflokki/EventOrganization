from django.db import models
from django.utils.translation import gettext_lazy as _


class Decoration(models.Model):
    class Meta:
        verbose_name = _('Украшение')
        verbose_name_plural = _('Украшения')

    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField( verbose_name="Описание")
    price = models.PositiveIntegerField(default=1000, verbose_name="Цена")
    image = models.ImageField(upload_to='images/decorations/', null=True, verbose_name="Изображение")

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
    class Meta:
        verbose_name = _('Место проведения')
        verbose_name_plural = _('Места проведения')

    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    decoration = models.ManyToManyField(to='Decoration', verbose_name="Украшение")

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
    class Meta:
        verbose_name = _('Тип артиста')
        verbose_name_plural = _('Тип артистов')

    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField( verbose_name="Описание")

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
    class Meta:
        verbose_name = _('Событие')
        verbose_name_plural = _('События')

    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    event_location = models.ManyToManyField(to="EventLocation", verbose_name="Место проведения")
    artist_class = models.ManyToManyField(to="ArtistClass", verbose_name="Тип артиста")

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
    class Meta:
        verbose_name = _('Артист')
        verbose_name_plural = _('Артисты')

    id_artist_class = models.ForeignKey(to='ArtistClass', on_delete=models.CASCADE, verbose_name="Тип артиста")

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    description = models.TextField( verbose_name="Описание")
    price = models.PositiveIntegerField(default=1000, verbose_name="Стоимость")
    image = models.ImageField(upload_to='images/artist/', null=True, verbose_name="Изображение")

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
    class Meta:
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')

    id_location = models.ForeignKey(to='EventLocation', on_delete=models.CASCADE, verbose_name="Номер")
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField( verbose_name="Описание")
    address = models.CharField(max_length=200, verbose_name="Арес")
    price = models.PositiveIntegerField(default=1000, verbose_name="Стоимость")
    image = models.ImageField(upload_to='images/location/', null=True, verbose_name="Изображение")

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
    class Meta:
        verbose_name = _('Информация о заказе')
        verbose_name_plural = _('Информация о заказах')
        ordering = ['-event_time']

    p_first_name = models.CharField(max_length=100, verbose_name="Имя")
    p_last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    p_phone = models.CharField(max_length=100, verbose_name="Телефон")
    p_email = models.EmailField(max_length=100, verbose_name="Мыло")
    event_time = models.DateField(max_length=100, verbose_name="Дата")

    id_event = models.ForeignKey(to='Event', on_delete=models.CASCADE, verbose_name="СОбытие")
    id_location_address = models.ForeignKey(to='LocationAddress', on_delete=models.CASCADE, verbose_name="Адрес")
    id_decoration = models.ForeignKey(to='Decoration', on_delete=models.CASCADE, verbose_name="Украшение")
    id_artist = models.ForeignKey(to='Artist', on_delete=models.CASCADE, verbose_name="Артист")

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

    def __str__(self):
        return f"Имя: {self.p_first_name}, Фамилия: {self.p_last_name}, " \
               f"Дата: {self.event_time}, Телефон: {self.p_phone}"
