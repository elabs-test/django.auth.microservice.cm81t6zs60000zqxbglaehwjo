from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
import json
from users.serializers import RegisterSerializer

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            serializer = RegisterSerializer(data=data)

            if serializer.is_valid():
                user = serializer.save()
                return JsonResponse({"message": "Usuario registrado con éxito", "user_id": user.id}, status=201)

            return JsonResponse({"error": serializer.errors}, status=400)

        except Exception as e:
            return JsonResponse({"error": f"Error interno: {str(e)}"}, status=500)

