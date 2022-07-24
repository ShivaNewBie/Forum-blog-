from django import views
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from discussion.models import Discussion

from .serializers import DiscussionSerializer

class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self,serializer): #when we post data in api. logged in user will be saved as user
        serializer.save(user=self.request.user)