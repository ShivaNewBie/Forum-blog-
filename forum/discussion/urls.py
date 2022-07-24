from django.urls import path,include

from rest_framework.routers import DefaultRouter

from discussion.api import views as dv

router = DefaultRouter()
router.register(r'discussions', dv.DiscussionViewSet)

urlpatterns = [
    path('', include(router.urls))


]