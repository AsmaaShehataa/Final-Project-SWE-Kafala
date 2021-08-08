from rest_framework import serializers
from .models import  CountryModel,CityModel,OrphanageModel,AdoptionTypeModel,ChildrensModel,ChildImageModel



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'
#
class CitySerializer(serializers.ModelSerializer):
     class Meta:
         model = CityModel
         fields = '__all__'

class OrphanageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrphanageModel
        fields = '__all__'
# #
class AdoptionTypeSerializer(serializers.ModelSerializer):
        class Meta:
            model = AdoptionTypeModel
            fields = ("AdoptionTypeID","AdoptionTypeName")


class ChildrensSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildrensModel
        fields = '__all__'

#
#
class ChildImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildImageModel
        fields = '__all__'