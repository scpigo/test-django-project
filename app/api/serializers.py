from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        user.set_password(password)
        user.save()
        return user


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    parent_note = serializers.PrimaryKeyRelatedField(
        queryset=Note.objects.all(),
        required=False,
        allow_null=True
    )
    parent_note_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'status', 'user', 'parent_note', 'parent_note_detail', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def get_parent_note_detail(self, obj):
        if not obj.parent_note:
            return None
        return NoteSerializer(obj.parent_note).data

    def validate_parent_note(self, value):
        user = self.context['request'].user
        if value is not None and value.user != user:
            raise serializers.ValidationError("Родительская заметка должна принадлежать авторизованному пользователю.")
        return value