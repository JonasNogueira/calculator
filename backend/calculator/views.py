from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Operation
from .serializers import OperationSerializer, ExpressionInputSerializer
from .services import save_operation, eval_expr
from django.shortcuts import render

def frontend_index(request):
    return render(request, "index.html")


class CalculateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpressionInputSerializer

    def post(self, request):
        serializer = ExpressionInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        expression = serializer.validated_data["parameters"]

        try:
            result = eval_expr(expression)

        except ValueError as e:
            return Response({"error": str(e)}, status=400)

        operation = save_operation(user=request.user, expression=expression, result=result)
        return Response(OperationSerializer(operation).data, status=201)


class HistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recent_operations = Operation.objects.filter(user=request.user).order_by("-created_at")[:10]
        return Response(OperationSerializer(recent_operations, many=True).data)
    
    def delete(self, request):
        Operation.objects.filter(user=request.user).delete()
        return Response({"detail": "Histórico apagado com sucesso."}, status=204)

