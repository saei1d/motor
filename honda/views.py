from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView
from honda.models import *
from honda.seryalizers import *


class Honda125(APIView):
    def get(self, request):
        context = {}
        try:
            mmd = Motor.objects.get(id=1)
            context = MotorSerializer(mmd, many=False).data
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'Not Found'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)


class GroupLavazem(APIView):
    def get(self, request, pk):
        context = {}
        try:
            mmd = Group_lavazem.objects.filter(motor=pk)
            context = GroupLavazemSerializer(mmd, many=True).data
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'Not Found'
            status_code = HTTP_404_NOT_FOUND

        return Response(context, status=status_code)


class Lavazem125(APIView):
    def get(self, request, pk):
        context = {}
        try:
            saeid = Lavazem.objects.filter(lavazem=pk)
            context = LavazemSerializer(saeid, many=True).data
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'Not Found'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)
