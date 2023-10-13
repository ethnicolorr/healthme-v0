from django.urls import path
from api import views

urlpatterns = [
    path('appointment/', views.AppointmentView.as_view()),
    path('appointments', views.UserAppointmentView.as_view()),
    path('appointment/<int:pk>', views.AppointmentDetailView.as_view()),
    path('note/', views.NoteView.as_view()),
    path('notes', views.UserNoteView.as_view()),
    path('note/<int:pk>', views.NoteDetailView.as_view())
]
