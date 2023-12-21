from rest_framework import serializers
from apiV2.models import Employee2, Role2, Department2


class Employee2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee2
        fields = '__all__'


class Role2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role2
        fields = '__all__'


class Department2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department2
        fields = '__all__'
