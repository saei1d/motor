from rest_framework import serializers
from honda.models import *


class MotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motor
        fields = '__all__'


class GroupLavazemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_lavazem
        fields = '__all__'


class LavazemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lavazem
        fields = '__all__'
