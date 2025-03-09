from rest_framework import serializers
from django.contrib.auth.models import User
from users.utils import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, data):
        """Validar todos los campos del formulario, incluyendo la contraseña."""
        password = data.get('password')
        errors = validate_password(password)
        if errors:
            raise serializers.ValidationError({"password": errors})
        return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class RecoveryPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
