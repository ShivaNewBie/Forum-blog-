from django import views
from django.shortcuts import get_object_or_404
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError




from discussion.models import Discussion, Category, Answer

from .serializers import CategorySerializer, DiscussionSerializer, AnswerSerializer

class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all().order_by('-created_at')
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
    pagination_class = None


class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Answer.objects.filter(discussion__slug=kwarg_slug) #we want a url where answer will be based on discussion thus we will lookup on discussion slug

class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    
    def perform_create(self,serializer):
        request_user = self.request.user 
        kwarg_slug = self.kwargs.get('slug') #get slug of discussion we are answering
        discussion = get_object_or_404(Discussion,slug=kwarg_slug)
    
        if discussion.answers.filter(author=request_user).exists():
            raise ValidationError('You already answered this question')
        
        serializer.save(author=request_user,discussion=discussion)

class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = 'uuid'