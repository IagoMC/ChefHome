from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
from datetime import datetime, timedelta
from .models import Usuarios

def login(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        campos_requeridos = ['email', 'contrasena']
        for campo in campos_requeridos:
            if campo not in body:
                return JsonResponse({'error': f'Falta campo requerido: {campo}'}, status=400,safe=False)

        email = body.get('email')
        contraseña = body.get('contraseña')

        Usuarios = authenticate(request, Email=email, Contraseña=contraseña)
        if usuario is not None:
            login(request, usuario)
            Token = get_token(usuario)
            usuario.Token = Token
            usuario.save()
            return JsonResponse({'token': Token})
        else:
            usuario_existente = Usuarios.objects.filter(Email=email).exists()
            if usuario_existente:
                usuario = Usuarios.objects.get(Email=email)
                if check_password(password, usuario.Contraseña):
                    return JsonResponse({'error': 'Contraseña incorrecta'}, status=401,safe=False)
                else:
                    return JsonResponse({'error': 'Usuario no encontrado'}, status=404,safe=False)
            else:
                return JsonResponse({'error': 'Usuario no encontrado'}, status=404,safe=False)
    else:
        return render(request, 'login.html')
    
  
def get_token(usuario):
    payload = {
        'usuario_id': usuario.id,
        'usuario_nombre': usuario.Nombre,
        'usuario_email': usuario.Email,
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
    return token.decode('utf-8')
