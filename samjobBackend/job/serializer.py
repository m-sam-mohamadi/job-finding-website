from rest_framework import serializers

from .models import Job,Category

class CategSerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ('id','title',)
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'positionSalary',
            'positionLocation',
            'companyName',
            'created_by',
            'createdAtFormatted'
        )
class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'category',
            'description',
            'companyLocation',
            'companyEmail',
            'positionSalary',
            'positionLocation',
            'companyName',
            'createdAtFormatted'
        )
