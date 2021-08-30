from django.shortcuts import render
from testapp.forms import StudentResultForm
from django.views.generic import View
from testapp.models import StudentResult
from testapp.serializers import StudentResultSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentResultCURDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            Stu=StudentResult.objects.get(id=id)
            Serializer=StudentResultSerializer(Stu)
            json_data=JSONRenderer().render(Serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=StudentResult.objects.all()
        Serializer=StudentResultSerializer(qs,many=True)
        json_data=JSONRenderer().render(Serializer.data)
        return HttpResponse(json_data,content_type='application/json')


    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        Serializer=StudentResultSerializer(data=pdata)
        if Serializer.is_valid():
            Serializer.save()
            Msg={'msg':'Resource Created Successfully..'}
            json_data=JSONRenderer().render(Msg)
            return HttpResponse(json_data,content_type='application/json')

        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)
