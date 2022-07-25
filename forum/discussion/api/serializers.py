from rest_framework import serializers

from discussion.models import Discussion, Category  


class DiscussionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField() 
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Discussion
        exclude = ['id','updated_at'] #it is not good to show id
    
    def get_created_at(self,instance): #modified date time
        return instance.created_at.strftime('%B, %d, %Y')

class CategorySerializer(serializers.ModelSerializer):
    discussions = DiscussionSerializer(many=True,required=False)
    slug = serializers.SlugField(read_only=True)
    class Meta: 
        model = Category
        fields = ['title','discussions','slug']

