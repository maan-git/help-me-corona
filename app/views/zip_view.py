from rest_framework.viewsets import ModelViewSet
from app.models.zip import Zip
from utils.views_utils import get_generic_read_serializer


class ZipView(ModelViewSet):
    queryset = Zip.objects.all()
    ordering = ("name",)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(Zip, 1)
        return serializer_class
