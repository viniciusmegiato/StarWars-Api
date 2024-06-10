from rest_framework import serializers

class RelatedPersonSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    relation = serializers.URLField()

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    height = serializers.CharField()
    mass = serializers.CharField()
    hair_color = serializers.CharField()
    skin_color = serializers.CharField()
    eye_color = serializers.CharField()
    birth_year = serializers.CharField()
    gender = serializers.CharField()
    homeworld = serializers.URLField()
    films = serializers.ListField(child=serializers.URLField())
    species = serializers.ListField(child=serializers.URLField())
    vehicles = serializers.ListField(child=serializers.URLField())
    starships = serializers.ListField(child=serializers.URLField())
    created = serializers.DateTimeField()
    edited = serializers.DateTimeField()
    url = serializers.URLField()
    related = RelatedPersonSerializer(many=True)
