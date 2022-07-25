from django import views
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView




from discussion.models import Discussion, Category

from .serializers import CategorySerializer, DiscussionSerializer

class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self,serializer): #when we post data in api. logged in user will be saved as user
        serializer.save(user=self.request.user)

class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'