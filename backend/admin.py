from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Member)
admin.site.register(Cinema)
admin.site.register(Cinema_Movie)
admin.site.register(Movie)
admin.site.register(Order)