from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
