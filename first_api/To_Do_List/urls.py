from rest_framework import routers
from . import views
from django.urls import path,include

router=routers.DefaultRouter()
router.register(r'heros',views.HeroViewSet)

urlpattern=[
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
    namespace='rest_framework'))
]