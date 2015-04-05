from shopsense.models import Mov
from shopsense.models import Genre
from shopsense.serializers import MovSerializer
# from shopsense.serializers import GenreSerializer

from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from shopsense.serializers import UserSerializer
from shopsense.permissions import IsOwnerOrReadOnly


class MovList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    queryset = Mov.objects.all()
    serializer_class = MovSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.save(genre=self.request.genre)
#   def perform_create(self, serializer):
#       serializer.

# class MovList(generics.ListCreateAPIView):
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
# 	queryset = Mov.objects.all()
# 	serializer_class = MovSerializer

# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)
# # 	def perform_create(self, serializer):
# #     	serializer.save(owner=self.request.user)

class MovDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Mov.objects.all()
    serializer_class = MovSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
