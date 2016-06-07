from django.contrib import admin
from boa.core.models import Answer

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('chanswer','enanswer',)
    search_field = ('chanswer',)
    list_filter = ('id',)
    ordering = ('id',)


admin.site.register(Answer)
