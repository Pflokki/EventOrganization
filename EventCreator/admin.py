from django.contrib import admin

from .models import Artist, ArtistClass, Decoration, Event, EventLocation, LocationAddress, OrderInfo

# Register your models here.
admin.site.register(Artist)
admin.site.register(ArtistClass)
admin.site.register(Decoration)
admin.site.register(Event)
admin.site.register(EventLocation)
admin.site.register(LocationAddress)

admin.site.register(OrderInfo)
