import datetime

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Appointment, ProcedureType, NoteType, Note  # , Procedure
from .serializers import AppointmentSerializer, NoteSerializer  # , ProcedureSerializer


class AppointmentView(generics.ListCreateAPIView, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        appointments = Appointment.objects.filter(user=self.request.user)
        return appointments.order_by('date_time')

    def perform_create(self, serializer):
        user = self.request.user
        ptype = generics.get_object_or_404(ProcedureType, id=self.request.data.get('ptype'))
        return serializer.save(user=user, ptype=ptype)


class UserAppointmentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        appointments = Appointment.objects.filter(user=self.request.user,
                                                  date_time__gte=datetime.datetime.now()).order_by('date_time')[:2]
        serializer_class = AppointmentSerializer(appointments, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        if not self.request.data.get('date'):
            raise ValueError("Выберите дату")
        appointments = Appointment.objects.filter(user=self.request.user,
                                                  date_time__date=self.request.data.get('date')).order_by('date_time')
        serializer_class = AppointmentSerializer(appointments, many=True)
        return Response(serializer_class.data)


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_update(self, serializer):
        ptype = generics.get_object_or_404(ProcedureType, id=self.request.data.get('ptype'))
        return serializer.save(ptype=ptype)


class NoteView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NoteSerializer

    def get_queryset(self):
        notes = Note.objects.filter(user=self.request.user)
        return notes.order_by('date_time')

    def perform_create(self, serializer):
        user = self.request.user
        ntype = generics.get_object_or_404(NoteType, id=self.request.data.get('ntype'))
        return serializer.save(user=user, ntype=ntype)


class UserNoteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if not self.request.data.get('date'):
            raise ValueError("Выберите дату")
        notes = Note.objects.filter(user=self.request.user,
                                    date_time__date=self.request.data.get('date')).order_by('date_time')
        serializer_class = NoteSerializer(notes, many=True)
        return Response(serializer_class.data)


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_update(self, serializer):
        ntype = generics.get_object_or_404(NoteType, id=self.request.data.get('ntype'))
        return serializer.save(ntype=ntype)


# class ProcedureView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Procedure.objects.all()
#     serializer_class = ProcedureSerializer
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         ptype = generics.get_object_or_404(Procedure, id=self.request.data.get('ptype'))
#         frequency = datetime.timedelta(seconds=self.request.data.get('frequency'))
#         return serializer.save(user=user, ptype=ptype, frequency=frequency)
