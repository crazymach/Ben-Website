from django.contrib import admin
from .models import Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	('Question',			{'fields': ['question_text'], 'classes': ['collapse']}),
	('Date information', 	{'fields': ['pub_date'], 'classes': ['collapse']}),



	]

admin.site.register(Question, QuestionAdmin)