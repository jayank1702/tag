from django.contrib import admin
from testapp.models import Resident,Visitor,Worker
# Register your models here.
class ResidentAdmin(admin.ModelAdmin):
    fields=['rid','name','phonenumber','address','email','fathersname','occupation','idproof','vehiclenumber','rfid','date','status']


admin.site.register(Resident,ResidentAdmin)

class VisitorAdmin(admin.ModelAdmin):
    fields=['resident','name','mobilenumber','vehiclenumber','address_to_visit','purpose_of_visit','date','status']

admin.site.register(Visitor,VisitorAdmin)

class WorkerAdmin(admin.ModelAdmin):
    field=['resident','name','mobilenumber','address','date','status']

admin.site.register(Worker,WorkerAdmin)
