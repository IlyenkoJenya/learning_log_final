#этот фай создали мы сами,изначаьно его не было в папке11
"Определяет схемы URL для application."


from django.urls import path  #необходима для связывания URL с представлениями 
from . import views #точка говорит что виевс в этой же папке

app_name='апликейшн' #помогает джанго отличать юрлс.ру На его ссылаются из вне
urlpatterns=[
	#home page
	path ('',views.index,name='индекс'), # даем имена,чтоюы ссылаться в шаблонах
	# '' говорит что базу сайта берется со стратовой страницы
	#Django вызывает index() из views.py,то есть представления
	#аргумент определяет имя index для этой схемы URL,чтобы на ее можно было ссыаться в других частях кожа

	#страница со списком всех тем
	path ('topics/',views.topics,name='топики'), # даем имена,чтоюы ссылаться в шаблонах
	path ('topics/<int:topic_id>/',views.topic,name='топик'),# даем имена,чтоюы ссылаться в шаблонах

	#страница для добавления новой темы
	path('new_topic/',views.new_topic,name='NEW_TOPIC'),

	#cтраница добавления новой записи
	path ('new_entry/<int:topic_id>/',views.new_entry,name='NEW_ENTRY'),

	#страница редактирования записи
	path ('edit_entry/<int:entry_id>/',views.edit_entry,name='EDIT_ENTRY')
	
]	
