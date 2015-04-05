from django.forms import widgets
from rest_framework import serializers
from shopsense.models import Mov
from shopsense.models import Genre
from django.contrib.auth.models import User
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


class GenreSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField(many=True)
    class Meta:
        model = Genre
        fields = ('name',)   
        

class MovSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)   
    # genre = GenreSerializer(many=True)

    class Meta:
        model = Mov
        fields = ('popularity','director','genre','imdb_score','name',)
        # extra_kwargs = {'genre': {'write_only': True}}

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        genre_data = validated_data.pop('genre')
        genre_data = genre_data.serialize
        stream = BytesIO(genre_data)
        data = JSONParser().parse(stream)
        serializer = GenreSerializer(data=genre_data)
        serializer.is_valid()
        genre_data = serializer.validated_data

        movie = Mov.objects.create(**validated_data)
        Genre.objects.create(genre_id=3,**genre_data)
        return movie

    def update(self, instance, validated_data):
        """
        Update and return an existing `Mov` instance, given the validated data.
        """
        # genre_data = validated_data.pop('genre')
        # # genre_data = genre_data.serialize
        # stream = BytesIO(genre_data)
        # data = JSONParser().parse(stream)
        # serializer = GenreSerializer(data=genre_data)
        # serializer.is_valid()
        # genre_data = serializer.validated_data

        genre = instance.genre
        
        instance.name = validated_data.get('name', instance.name)
        instance.director = validated_data.get('director', instance.director)
        instance.imdb_score = validated_data.get('imdb_score', instance.imdb_score)
        instance.popularity = validated_data.get('popularity', instance.popularity)
        instance.save()
        genre.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Mov.objects.all())

    class Meta:
        model = User
        fields = ('username', 'movies')

