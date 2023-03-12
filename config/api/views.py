from rest_framework import viewsets
from .models import Cars
from .serializers import CarsSerializer
# Create your views here.


class CarsView(viewsets.ModelViewSet):

    queryset = Cars.objects.raw('SELECT id, name, company FROM api_Cars')
    serializer_class = CarsSerializer
