from django.shortcuts import render,redirect,get_object_or_404 #render-воспроизводить с англ, 
#HttpResponseRedirect-redirect=перенаправления пользователя к странице topics после отправки введенной темы
from django.contrib.auth.decorators import login_required
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

from django.http import Http404
# Create your views here.

def index(request):
	"домашняя страница application"	
	return render (request,'application/index.html')
	
@login_required
def topics(request):
	#выводит список тем
	TOPICS=Topic.objects.filter(owner=request.user).order_by('date_added') #выдает запрос к базе по получению 
	#обьектов Toпик отсортированных по атрибуту даты
#Фрагмент кода Topic.objects.
#filter(owner=request.user) приказывает Django извлечь из базы данных только 
#те объекты Topic, у которых атрибут owner соответствует текущему пользователю. 
#Так как способ отображения не изменяется, изменять шаблон для страницы тем 
#вообще не нужно
	context={'topics5':TOPICS} #определяется что будет передваться шаблону. В шаблоне перебирается топикс5.
	return render (request,'application/topics.html',context)
	
@login_required
def topic(request,topic_id):
	#ВЫводит одну теmу и все ее записи
	topic=get_object_or_404(Topic,id=topic_id)
	#проверка того что тебя принадлежит текущему пользователю
	check_topic_owner(request,topic)
	entries=topic.entry_set.order_by('id')
	context={'topic':topic,'entries':entries} #в щаблоне перебираются значения,но передает ключ.
	return render (request,'application/topic.html',context) 
@login_required
def new_topic(request):
	"""определяет новую форму"""
	if request.method!='POST': #проверяем тип запроса
		#данные не отправляются,создается пустая форма
		form=TopicForm() #создаем топик и сохранили в переменной его

	else:
		#отправлены данные POST. обработать данные
		form=TopicForm(data=request.POST) #передаем данные введенные пользователем , хранящиеся в request.POST.

		if form.is_valid(): #проверяет запоненны ли все обязательные поля. Априори стоят все обязятельные
			new_topic=form.save(commit=False)
			new_topic.owner=request.user #Атрибуту 
#owner новой темы присваивается текущий пользователь
			new_topic.save()
			form.save() #если все заполненно,то сохраняет в базу данных
			return redirect('апликейшн:топики') #перенаправляет данную страницу


	#вывести пустую или недействительную форму
	context={'form':form}
	return render(request,'application/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
	#Добавление новой записи по конкретной теме
	topic=Topic.objects.get(id=topic_id) #нужно для работы с определенной темой
	if request.method!='POST':
		#данные не отправлялись,создается пустая форма
		form=EntryForm()

	else:
		#отправлены данные POST,обрвботать данные

		form=EntryForm(data=request.POST)
		if form.is_valid(): #проверяем все ли заполненно
		#Если данные корректны, необходимо задать атрибут topic объекта записи перед сохранением его в базе данных
			new_entry=form.save(commit=False) # не сохранять в базу данных,но сохранить в переменной
			new_entry.topic=topic #Мы присваиваем атрибуту topic объекта new_entry тему, прочитанную из базы данных в начале функции
			new_entry.save()
			return redirect('апликейшн:топик', topic_id=topic_id) #показываем путь куда передаем и какую запись 
			#перенаправляет на страницу с записями к теме.

	#вывести пустую или недействительную форму
	context={'topic':topic,'form':form}
	return render(request,'application/new_entry.html',context)		

@login_required
def edit_entry(request,entry_id):
	#редактирование существующей записи
	entry=Entry.objects.get(id=entry_id) #получаем запись которую хотим изменить
	topic=entry.topic # тема связанная с этой записью
	check_topic_owner(request,topic)
	if request.method!='POST':
		#исходный запрос. форма заполняется данными текущей записи
		form=EntryForm(instance=entry) #instance-пример. Аргумент приказывает джанго создать форму,
		#заранее заполненной инфой из существующей записи. Пользователь видит существующие записи и может их изменить


	else:
		#отправка даннх РОСТ. обработать данные
		form= EntryForm(instance=entry,data=request.POST) 
		#Они приказывают Django создать экземпляр формы на 
#основании информации существующего объекта записи, обновленный данными из request.POST
		if form.is_valid():
			form.save()
			return redirect('апликейшн:топик',topic_id=topic.id)

	context={'entry':entry,'topic':topic,'form':form}
	return render(request,'application/edit_entry.html',context)


def check_topic_owner(request,topic):
	if topic.owner !=request.user:
		raise Http404

