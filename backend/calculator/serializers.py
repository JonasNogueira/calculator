from rest_framework.serializers import ModelSerializer, CharField, Serializer
from .models import Operation


class OperationSerializer(ModelSerializer):
    class Meta:
        model = Operation
        fields = ["parameters", "result", "created_at"]


class ExpressionInputSerializer(Serializer):
    parameters = CharField(max_length=255)
