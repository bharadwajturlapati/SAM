__author__ = 'bharadwaj'

from django.contrib import admin
from models import quakedetails
from models import MyModel
from views import export_csv,export_xls,export_xlsx


# admin.py

# ... export functions will go here ...

# admin.py
from django.contrib import admin
from models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    actions = [export_xls, export_xlsx]

class QuakeAdmin(admin.ModelAdmin):
    actions = [export_csv]

admin.site.register(MyModel, MyModelAdmin)
admin.site.register(quakedetails,QuakeAdmin)




