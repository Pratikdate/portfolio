from django.contrib import admin

# Register your models here.
from .models import Personal_About_Me,Professional_About_Me,Testimonials,My_Service,My_Works,Messages,Skill

admin.site.register(Personal_About_Me)
admin.site.register(Professional_About_Me)
admin.site.register(Testimonials)
admin.site.register(My_Service)
admin.site.register(My_Works)
admin.site.register(Messages)
admin.site.register(Skill)