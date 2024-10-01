from rest_framework import serializers
from .models import Station, Information

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    # برای نمایش اطلاعات ایستگاه در GET
    station = StationSerializer(read_only=True)
    # برای دریافت شناسه ایستگاه در POST)
      # برای دریافت شناسه ایستگاه در POST
    station_id = serializers.PrimaryKeyRelatedField(queryset=Station.objects.all(), source='station', write_only=True)


    class Meta:
        model = Information
        fields = '__all__'
