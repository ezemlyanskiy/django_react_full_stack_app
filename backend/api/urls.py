from django.urls import include, path

from .views import NoteDelete, NoteListCreate

urlpatterns = [
    path('v1/notes/', NoteListCreate.as_view(), name='note-list'),
    path(
        'v1/notes/<int:pk>/delete/', NoteDelete.as_view(), name='delete-note'
    ),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
