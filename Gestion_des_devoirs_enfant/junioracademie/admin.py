from django.contrib import admin
from junioracademie.models import Enfant ,Enseignant, Classe ,Cours
# Register your models here.
admin.site.register(Enfant)
admin.site.register(Enseignant)
admin.site.register(Classe)
admin.site.register(Cours)
