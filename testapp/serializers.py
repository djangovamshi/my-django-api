from rest_framework import serializers
from testapp.models import StudentResult

class StudentResultSerializer(serializers.Serializer):
    roll_number=serializers.IntegerField()
    name=serializers.CharField()
    dob=serializers.DateField()
    marks=serializers.IntegerField()
    

    def create(self,Validated_data):
        return StudentResult.objects.create(**Validated_data)
