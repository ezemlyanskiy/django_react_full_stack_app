from .models import Note
from .serializers import NoteSerializer


class NoteMixin:
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
