from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from patient.models import Patient
from patient.serializers import PatientSerializer


class PatientView(APIView):

    def get(self, request):
        markers = Patient.objects.all()
        serializer = PatientSerializer(markers, many=True)
        response_data = {'patients': serializer.data}
        return JsonResponse(response_data, safe=False)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
