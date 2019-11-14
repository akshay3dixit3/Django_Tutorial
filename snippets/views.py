from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format = format),
		'snippets': reverse('snippet-list', request=request, format = format),
		})


# class SnippetList(generics.ListCreateAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
# 	def  perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permissions_classes = (permissions.IsAuthenticatedOrReadOnly,
# 							 IsOwnerOrReadOnly,)

class SnippetViewSet(viewsets.ModelViewSet):
	"""
	Provides all the basic operations anmely list create update retrieve and action.
	We will add highlight functionality as well
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permissions_classes = (permissions.IsAuthenticatedOrReadOnly,
							 IsOwnerOrReadOnly,)

	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *arg, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlight)

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)




class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	it provies list amn detail directly, if you want to have some different actions then override them
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class SnippetHighlight(generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	renderer_classses = (renderers.StaticHTMLRenderer,)

# 	def get(self, request, *args, **kwargs):
# 		snippet = self.get_object()
# 		return Response(snippet.highlighted)