from rest_framework import routers
from .views import CarsView

router = routers.DefaultRouter()
router.register(r'cars', CarsView, 'carApi')


urlpatterns = router.urls
