from django import views
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView




from discussion.models import Discussion, Category, Answer

from .serializers import CategorySerializer, DiscussionSerializer, AnswerSerializer

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

class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Answer.objects.filter(discussion__slug=kwarg_slug) #we want a url where answer will be based on discussion thus we will lookup on discussion slug

class AnswerRUDAPIView(generics.RetrieveUpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = 'uuid'