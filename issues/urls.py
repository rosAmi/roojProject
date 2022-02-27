from django.urls import path
from rest_framework import routers
from issues.views import IssuesViewSet

# from .views import index


router = routers.DefaultRouter()
router.register('issues', IssuesViewSet)

urlpatterns = router.urls

# urlpatterns = [
#   path('issues/', index) ]
