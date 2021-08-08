from django.contrib import admin
from orphanage.models import OrphanageModel,CityModel,CountryModel,ChildrensModel,ChildImageModel,AdoptionTypeModel



admin.site.register(CityModel)
admin.site.register(CountryModel)
admin.site.register(ChildrensModel)
admin.site.register(ChildImageModel)
admin.site.register(OrphanageModel)
admin.site.register(AdoptionTypeModel)

