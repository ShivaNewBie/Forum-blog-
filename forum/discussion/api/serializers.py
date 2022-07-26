from rest_framework import serializers

from discussion.models import Discussion, Category, Answer


class DiscussionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField() 
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()
    

    class Meta:
        model = Discussion
        exclude = ['id','updated_at'] #it is not good to show id
    
    def get_created_at(self,instance): #modified date time
        return instance.created_at.strftime('%B, %d, %Y')

    def get_answers_count(self,instance):
        return instance.answers.count()
    
    def get_user_has_answered(self,instance):
        request = self.context.get('request')
        return instance.answers.filter(author=request.user).exists() #condition returns true or false


class CategorySerializer(serializers.ModelSerializer):
    discussions = DiscussionSerializer(many=True,required=False)
    slug = serializers.SlugField(read_only=True)
    class Meta: 
        model = Category
        fields = ['id','title','discussions','slug']


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    discussion_slug = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    
    class Meta:     
        model = Answer
        exclude = ['discussion', 'likes', 'updated_at']

    def get_discussion_slug(self,instance):
        return instance.discussion.slug

    def get_created_at(self,instance):
        return instance.created_at.strftime('%B %d, %Y')

    def get_likes_count(self,instance):
        return instance.likes.count()
    
    def get_user_has_liked(self,instance):
        request = self.context.get('request')
        return instance.likes.filter(pk=request.user.pk).exists()