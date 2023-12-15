from rest_framework import serializers
from apiV1.models import Employee2

# Create Serialers for EMployee2


class Employee2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee2
        fields = "__all__"
