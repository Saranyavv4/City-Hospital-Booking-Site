from django.contrib import admin
from .models import Departments,Doctors,BookingDetails


# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)

class BookingDetailsAdmin(admin.ModelAdmin):
    list_display=['id','p_name','p_phone','p_email','doc_name','booking_date','booked_on']
admin.site.register(BookingDetails,BookingDetailsAdmin)





