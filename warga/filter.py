import django_filters

from .models import DataWarga

class SearchWarga(django_filters.FilterSet):
    class Meta:
        model = DataWarga
        fields = {
            'no_kk': ['icontains'],
            'nik': ['icontains'],
        }
