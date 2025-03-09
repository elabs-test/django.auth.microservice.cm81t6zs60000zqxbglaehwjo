def validate_password(password):
    """
    Validar que la contraseña cumpla con los requisitos:
    - Al menos 8 caracteres
    - Al menos 1 letra mayúscula
    - Al menos 1 número
    - Al menos 1 carácter especial
    """
    errors = []

    if len(password) < 8:
        errors.append("Debe tener al menos 8 caracteres.")
    if not any(char.isupper() for char in password):
        errors.append("Debe incluir al menos una letra mayúscula.")
    if not any(char.isdigit() for char in password):
        errors.append("Debe contener al menos un número.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" for char in password):
       errors.append("Debe incluir al menos un carácter especial.")

    return errors if errors else None