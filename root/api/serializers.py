from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from todo.models import Task


class TaskSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Task
        fields = '__all__'
        read_only = 'created'

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.complete = validated_data.get('complete', instance.complete)
        instance.save()
        return instance
