from rest_framework import generics
from .models import Snippet
from .serializers import SnippetModelSerializer

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer