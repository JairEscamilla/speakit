from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'profile_description')



class UsersInfoSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)



    def update(self, instance, validated_data):
        try:
            profile_description = validated_data.get('profile').get("profile_description")
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)

            instance.profile.profile_description = profile_description
        
        except:
            profile = Profile(user=instance, profile_description=profile_description)
            instance.profile = profile
        
        instance.profile.save()
        instance.save()

        return instance

    class Meta:
        model = User 
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile')



# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class PostUsernameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ("username", )

# Posts serializer
class PostSerializer(serializers.ModelSerializer):
    user = PostUsernameSerializer(many=False)
    class Meta:
        model = Post
        fields = '__all__'
        
