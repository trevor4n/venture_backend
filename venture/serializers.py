from rest_framework import serializers
from .models import Trip, Guideline, Restriction, Airline

class TripSerializer(serializers.HyperlinkedModelSerializer):
    guidelines = serializers.HyperlinkedRelatedField(
        view_name='guideline_detail',
        # todo - swap flags?
        many=True,
        read_only=True
    )
    trip_url = serializers.ModelSerializer.serializer_url_field(
        view_name='trip_detail'
    )
    class Meta:
        model = Trip
        fields = ('id', 'trip_url', 'guidelines', 'name' ,'destination', 'description', 'photo_url',)


class GuidelineSerializer(serializers.HyperlinkedModelSerializer):
    trip = serializers.HyperlinkedRelatedField(
        view_name='trip_detail',
        read_only=True
    )
    trip_id = serializers.PrimaryKeyRelatedField(
        queryset=Trip.objects.all(),
        source='trip'
    )
    class Meta:
        model = Guideline
        fields = ('id', 'trip', 'trip_id', 'location_type', 'location') 

# class TripSerializer(serializers.ModelSerializer):
    # todo - https://git.generalassemb.ly/flex-323/django-rest-framework#:~:text=ArtistSerializer(serializers.HyperlinkedModelSerializer)%3A-,songs%20%3D%20serializers.HyperlinkedRelatedField(%0A%20%20%20%20%20%20%20%20view_name%3D%27song_detail%27%2C%0A%20%20%20%20%20%20%20%20many%3DTrue%2C%0A%20%20%20%20%20%20%20%20read_only%3DTrue%0A%20%20%20%20),-Awesome%2C%20this%20is
    # class Meta:
    #     model = Trip
    #     fields = ('name' ,'destination', 'description', 'photo_url')