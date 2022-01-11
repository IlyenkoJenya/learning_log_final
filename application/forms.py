from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):  #Простейшая версия ModelForm состоит из вложенного класса Meta, 
#который сообщает Django, на какой модели должна базироваться форма и какие поля на ней 
#должны находиться.
	class Meta:
		model=Topic  #форма создается на базе модели Topic
		fields=['text'] #размещается только поле text
		labels={'text':''}  #приказывает Django не генерировать подпись для текстового поля

class EntryForm(forms.ModelForm):
	class Meta:
		model=Entry
		fields=['text']
		labels={'text':'сообщение:'}
		widgets={'text':forms.Textarea(attrs={'cols':80})} #виджет который задает ширину текуствого столбца


