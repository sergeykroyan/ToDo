from rest_framework.serializers import ModelSerializer
from todo.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'created', 'complete')
        read_only = 'created'

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.complete = validated_data.get('complete', instance.complete)
        instance.save()
        return instance
