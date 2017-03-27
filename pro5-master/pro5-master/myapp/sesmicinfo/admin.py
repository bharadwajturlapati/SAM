__author__ = 'bharadwaj'

from django.contrib import admin
from models import QuakeDetail
from models import MyModel
from models import SAMNode
from views import export_csv, export_xls, export_xlsx

from django.contrib import admin
from models import MyModel


class MyModelAdmin(admin.ModelAdmin):
    actions = [export_xls, export_xlsx]


class QuakeAdmin(admin.ModelAdmin):
    actions = [export_csv]

class RegisterSAMNODESToAdmin(admin.ModelAdmin) :
    action = []

admin.site.register(MyModel, MyModelAdmin)
admin.site.register(QuakeDetail, QuakeAdmin)
admin.site.register(SAMNode, RegisterSAMNODESToAdmin)




