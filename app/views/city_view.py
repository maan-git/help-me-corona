from rest_framework.viewsets import ModelViewSet
from app.models.city import City
from utils.views_utils import get_generic_read_serializer


class CityView(ModelViewSet):
    queryset = City.objects.all()
    ordering = ('name',)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(City, 1)
        return serializer_class