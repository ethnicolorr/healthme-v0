from django.contrib import admin
from .models import Appointment, ProcedureType, NoteType, Note  # , Procedure

admin.site.register(Appointment)
admin.site.register(ProcedureType)
admin.site.register(NoteType)
admin.site.register(Note)
