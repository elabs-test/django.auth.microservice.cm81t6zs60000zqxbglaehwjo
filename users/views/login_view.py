from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
import json
from users.serializers import LoginSerializer
from users.services import authenticate_user

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            serializer = LoginSerializer(data=data)

            if not serializer.is_valid():
                return JsonResponse({"error": serializer.errors}, status=400)

            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate_user(email, password)
            if user:
                return JsonResponse({"message": "Inicio de sesión exitoso"}, status=200)

            return JsonResponse({"error": "Usuario no existe o credenciales inválidas"}, status=401)

        except Exception as e:
            return JsonResponse({"error": f"Error interno: {str(e)}"}, status=500)

