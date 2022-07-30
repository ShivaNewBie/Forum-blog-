from django.urls import path,include

from rest_framework.routers import DefaultRouter

from discussion.api import views as dv

router = DefaultRouter()
router.register(r'discussions', dv.DiscussionViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('discussions/<slug:slug>/answers/', dv.AnswerListAPIView.as_view(), name='answer-list'),
    path('discussions/<slug:slug>/answer/', dv.AnswerCreateAPIView.as_view(), name='answer-create'),

    path('answers/<uuid:uuid>/', dv.AnswerRUDAPIView.as_view(), name='answer-rud'),

    path('categories/', dv.CategoryList.as_view(),name='category-list'),
    path('categories/create/',dv.CategoryCreateAPIView.as_view(), name='category-create' ),
    path('categories/<slug:slug>/', dv.CategoryDetail.as_view(), name='category-detail')

    

]