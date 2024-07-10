from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'patient_name', 'appointment_types', 'appointment_status',
                    'symptom', 'time', 'cancel']
    def doctor_name(self, obj):
        return obj.doctor.first_name

    def patient_name(self, obj):
        return obj.patient.first_name
admin.site.register(Appointment, AppointmentAdmin)