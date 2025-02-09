from rest_framework import permissions, viewsets
from todo.models import Task
from todo.serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TODOS to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticated]
    