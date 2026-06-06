from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, error_messages={
        "min_length": "رمز عبور نمی‌تواند کمتر از ۶ کاراکتر باشد."
    })

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number'),
            password=validated_data['password']
        )
        return user
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'date_joined']
        read_only_fields = ['id', 'date_joined']