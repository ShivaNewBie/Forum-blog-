from rest_framework import serializers

from discussion.models import Discussion, Category, Answer


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


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    discussion_slug = serializers.SerializerMethodField()

    class Meta:     
        model = Answer
        exclude = ['discussion', 'likes', 'updated_at']

    def get_discussion_slug(self,instance):
        return instance.discussion.slug