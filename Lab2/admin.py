from django.contrib import admin

# Register your models here.
from .models import TeamUser, Mentor

admin.site.register(TeamUser)
admin.site.register(Mentor)