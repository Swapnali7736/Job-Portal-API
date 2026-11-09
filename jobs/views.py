from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from jobs.models import Job
from jobs.serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from jobs.serializers import UserSerializer
from jobs.permissions import JobPermission

class JobListCreate(APIView):
    permission_classes=[JobPermission]
    authentication_classes=[TokenAuthentication]  
    def get(self,request):
        j=Job.objects.all()
        serializer_instance=JobSerializer(j,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer_instance=JobSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(postedby=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class JobRud(APIView):
    permission_classes=[JobPermission]
    authentication_classes=[TokenAuthentication]
    def get(self,request,i):
        j=get_object_or_404(Job,id=i)
        serializer_instance=JobSerializer(j)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,i):
        j=get_object_or_404(Job,id=i)
        self.check_object_permissions(request,j)
        serializer_instance=JobSerializer(j,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,i):
        j=get_object_or_404(Job,id=i)
        self.check_object_permissions(request, j)
        j.delete()
        return Response({"message":"Job deleted successfully"},status=status.HTTP_204_NO_CONTENT)



class Register(APIView):
    def post(self, request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



class Logout(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({"message":"Logout successfull"},status=status.HTTP_200_OK)