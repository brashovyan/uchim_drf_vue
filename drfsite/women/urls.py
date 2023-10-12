from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from women.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'womenviewset', WomenViewSet)
router.register(r'tag', TagViewSet)
router.register(r'new', NewViewSet)
router.register(r'subtag', SubtagViewSet)

urlpatterns = [
    path('activate/<str:uid>/<str:token>', ActivateUser.as_view()),
    path('me/', UserDetail.as_view()),
    path('womenlist_old/', WomenApiView.as_view()),
    path('womenlist_old/<int:pk>', WomenApiView.as_view()),
    path('womenlist/', WomenApiList.as_view()),
    path('womendetail/<int:pk>', WomenApiDetail.as_view()),
    path('womenupdate/<int:pk>', WomenApiUpdate.as_view()),
    path('womenupdelete/<int:pk>', WomenApiDelete.as_view()),
    path('womenlistuser/<int:pk>', WomenApiListUser.as_view()),
    # path('api/v1/womenviewset/', WomenViewSet.as_view({'get':'list'})),
    # path('api/v1/womenviewset/<int:pk>', WomenViewSet.as_view({'put':'update'})),
    path('', include(router.urls)),
    path('category/<int:pk>', CategoryApiDetail.as_view()),
]