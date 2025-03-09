from django.contrib.auth.models import User

def create_user(username, email, password):
    """
    Crear un nuevo usuario validando que no exista previamente.
    """
    if User.objects.filter(username=username).exists():
        raise ValueError("El usuario ya existe")
    if User.objects.filter(email=email).exists():
        raise ValueError("El correo ya está en uso")
    user = User.objects.create_user(username=username, email=email, password=password)
    return user

def authenticate_user(email, password):
    """
    Autenticar un usuario basado en email y contraseña.
    """
    user = User.objects.filter(email=email).first()
    if user and user.check_password(password):
        return user
    return None
