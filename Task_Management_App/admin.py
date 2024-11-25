from django.contrib import admin
from .models import CustomUser, Task

# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'due_date', 'assignto')