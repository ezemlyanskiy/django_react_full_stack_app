from rest_framework import generics

from .mixins import NoteMixin


class NoteListCreate(NoteMixin, generics.ListCreateAPIView):
    ...

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDelete(NoteMixin, generics.DestroyAPIView):
    ...
