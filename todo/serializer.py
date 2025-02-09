from rest_framework import serializers
from todo.models import Task

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=200)
    completed = serializers.BooleanField()
    created_at = serializers.DateTimeField(required=False)
    def create(self, validated_data):
        # return Task.objects.create(**validated_data)
        t = Task(**validated_data)
        t.save()
        return t 

    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance
    