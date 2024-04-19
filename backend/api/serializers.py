from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Note

User = get_user_model()


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        extra_kwargs = {'author': {'read_only': True}}
