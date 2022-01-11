from django.contrib import admin

from .models import Topic,Entry # обязательно добавлять чтобы появились в админ панели


# Register your models here.
admin.site.register(Topic) #сообщает Django, что управление моделью должно осуществляться через административный сайт
admin.site.register(Entry)