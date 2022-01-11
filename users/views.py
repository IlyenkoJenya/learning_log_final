from django.shortcuts import render,redirect
from django.contrib.auth import login #Затем мы импортируем 
#функцию login() для выполнения входа пользователя, если регистрационная 
#информация верна
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register (request):
	if request.method!='POST':
		#выводит пустую форму регистрации
		form=UserCreationForm() #Если нет, создается экземпляр UserCreationForm, не содержащий исходных данных 

	else:
		form=UserCreationForm(data=request.POST)


		if form.is_valid():
			new_user=form.save() #сли отправленные данные верны, мы вызываем метод save() формы для сохранения имени пользователя и хеша пароля в базе данных . Метод save()
#возвращает только что созданный объект пользователя, который сохраняется 
#в new_user
			#выполнение входа и перенаправление на домашнюю страницу
			login(request,new_user) #, которая создает действительный сеанс для нового пользователя
			return redirect ('апликейшн:индекс')



	#вывести пустую или недействительную форму
	context={'form':form}
	return render (request, 'users/register.html',context)