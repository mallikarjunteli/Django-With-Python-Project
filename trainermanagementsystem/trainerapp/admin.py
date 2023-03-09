from django.contrib import admin

# Register your models here.


from trainerapp.models import Course, trainer_batch_Asign, Trainer_Reg, City

admin.site.register(Course)
admin.site.register(City)
admin.site.register(Trainer_Reg)
admin.site.register(trainer_batch_details)


