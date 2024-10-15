from rest_framework import serializers

from .models import Prosodia_cancion_info, Prosodia_trabalenguas_info

class ProsodiaCancionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prosodia_cancion_info
        fields = '__all__'

class ProsodiaTrabalenguasInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prosodia_trabalenguas_info
        fields = '__all__'