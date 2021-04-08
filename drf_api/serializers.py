from rest_framework import serializers
from drf_api.models import User, UserProfile, Content



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone', 'pincode', 'roles', 'photo')



class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user
        
        
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        
        profile.phone = profile_data.get('phone', profile.phone)
        profile.pincode = profile_data.get('pincode', profile.pincode)
        profile.roles = profile_data.get('roles', profile.roles)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()
        
        return instance




class ContentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Content
        fields = ('id','title', 'body', 'summary', 'attachment', 'categories','created_by')
        
    def create(self, validated_data):
        created_by = validated_data.pop('created_by')
        content = Content.objects.create(**validated_data)
        content.save()

        User.objects.create(created_by=created_by, **content)

        return content