from rest_framework import serializers
from .models import Countries


# create serializers here

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Countries
        fields="__all__"
        