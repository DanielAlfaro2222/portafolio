from django.contrib import admin
from .models import Technology
from .models import Project
from .models import Formation

admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(Formation)
