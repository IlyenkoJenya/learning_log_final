from django.db import models
from django.contrib.auth.models import User
# Create your models here. создате тут свои модели

class Topic(models.Model): #если назвать NameTopic, то напишет Select name topic to change. разделения большими буквами как пробел работает в подсказке.
	"""Тема, которую изучает пользователь"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)
 
	def __str__(self):
#Возвращает строковое представление модели."""
		return self.text


class Entry(models.Model):
	"информация узученная пользоватеем по теме"
	topic=models.ForeignKey(Topic,on_delete=models.CASCADE) #чтобы шли ключем и удалялись цепочками
	text=models.TextField()
	data_added=models.DateTimeField(auto_now_add=True)

	class Meta():
		verbose_name_plural = 'entries' # если так не напишем,то будет писать Entrys. тупо довавит S в конце. это имя коммента к теме грубо гововя. Слева пишет это

	def __str__(self):
			#возвращает стоковое представление модели

		if len(self.text)>=50:
			return f"{self.text[:50]}..."
		else:
			return f"{self.text}"