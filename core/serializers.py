from rest_framework import serializers
from core.models import Usuario, Score

class ScoreSerializer(serializers.ModelSerializer):
    user_id_name = serializers.StringRelatedField(read_only=True, source='user_id')
    class Meta:
        model = Score
        fields= ['score','user_id_name']