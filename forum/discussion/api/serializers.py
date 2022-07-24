from rest_framework import serializers

from discussion.models import Discussion


class DiscussionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField() 
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Discussion
        exclude = ['id','updated_at']
    
    def get_created_at(self,instance):
        return instance.created_at.strftime('%B, %d, %Y')
    