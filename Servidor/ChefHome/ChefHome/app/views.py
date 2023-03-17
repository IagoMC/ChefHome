from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
from datetime import datetime, timedelta
from .models import Usuarios


@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        email = datos.get('email')
        Contraseña = datos.get('contraseña')
        confirm_contraseña = datos.get('confirmarContraseña')
        nombre = datos.get('nombre')
        
        # Validamos que los campos obligatorios hayan sido suministrados
        if not email or not Contraseña or not confirm_contraseña or not nombre:
            return JsonResponse({'error': 'Debe suministrar todos los campos obligatorios'})
        
        # Validamos que las contraseñas coincidan
        if Contraseña != confirm_contraseña:
            return JsonResponse({'error': 'Las contraseñas no coinciden'})
        
        # Validamos que no exista un usuario con el mismo correo electrónico o nombre
        if Usuarios.objects.filter(Email=email).exists() or Usuarios.objects.filter(Nombre=nombre).exists():
            return JsonResponse({'error': 'Ya existe un usuario con este correo electrónico o nombre'})
        
        # Creamos el usuario y guardamos su contraseña con set_password
        usuarios = Usuarios.objects.create_user(Email=email, Nombre=nombre)
        usuarios.set_password(Contraseña)
        usuarios.save()
        
        return JsonResponse({'mensaje': 'Usuario creado exitosamente'})
    else:
        return JsonResponse({'error': 'Este endpoint solo acepta solicitudes POST'})
    
    
@csrf_exempt    
def login(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        campos_requeridos = ['email', 'contrasena']
        for campo in campos_requeridos:
            if campo not in body:
                return JsonResponse({'error': f'Falta campo requerido: {campo}'}, status=400,safe=False)

        email = body.get('email')
        contraseña = body.get('contraseña')

        Usuarios = authenticate(request, email=email, contraseña=contraseña)
        if usuario is not None:
            login(request, usuario)
            Token = get_token(usuario)
            usuario.Token = Token
            usuario.save()
            return JsonResponse({'token': token})
        else:
            usuario_existente = Usuarios.objects.filter(email=email).exists()
            if usuario_existente:
                usuario = Usuarios.objects.get(email=email)
                if check_password(contraseña, usuario.contraseña):
                    return JsonResponse({'error': 'Contraseña incorrecta'}, status=401,safe=False)
                else:
                    return JsonResponse({'error': 'Usuario no encontrado'}, status=404,safe=False)
            else:
                return JsonResponse({'error': 'Usuario no encontrado'}, status=404,safe=False)
    else:
        return render(request, 'login.html')
    
@csrf_exempt    
def get_token(usuario):
    payload = {
        'usuario_id': usuario.id,
        'usuario_nombre': usuario.Nombre,
        'usuario_email': usuario.Email,
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
    return token.decode('utf-8')


"""
class Seguidores(models.Model):
    idseguido = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='seguidores_de')
    idusuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='usuarios_seguidos')

"""
