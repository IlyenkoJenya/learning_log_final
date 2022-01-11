#определение схемы юрс для пользователей

from django.urls import path,include #м функция include для включения аутентификационных URL-адресов по умолчанию, определенных Django. Эти URLадреса по умолчанию включают именованные схемы, такие как 'login' и 'lo

from . import views


app_name='users'

urlpatterns=[
	#включать юрл аторизации по умолчанию
	path('', include('django.contrib.auth.urls')),

	#page registration
	path ('register/',views.register, name='регистрация'),

	]