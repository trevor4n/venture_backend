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
