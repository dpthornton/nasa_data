from rest_framework import serializers
from facilities.models import Facility

class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'