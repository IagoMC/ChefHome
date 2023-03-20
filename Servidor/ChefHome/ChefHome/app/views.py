from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
from datetime import datetime, timedelta
from .models import Usuarios
import json
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        email = datos.get('email')
        contraseña = datos.get('contrasena')
        confirm_contraseña = datos.get('confirmarContrasena')
        nombre = datos.get('nombre')
        
        # Validamos que los campos obligatorios hayan sido suministrados
        if not email or not contraseña or not confirm_contraseña or not nombre:
            return JsonResponse({'error': 'Debe suministrar todos los campos obligatorios'})
        
        # Validamos que las contraseñas coincidan
        if contraseña != confirm_contraseña:
            return JsonResponse({'error': 'Las contraseñas no coinciden'})
        
        # Validamos que no exista un usuario con el mismo correo electrónico o nombre
        if Usuarios.objects.filter(email=email).exists() or Usuarios.objects.filter(nombre=nombre).exists():
            return JsonResponse({'error': 'Ya existe un usuario con este correo electrónico o nombre'})
        
        # Creamos el usuario y guardamos su contraseña con set_password
        usuario = Usuarios(nombre=nombre, email=email, contraseña=make_password(contrasena))
        usuario.save()
        
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
        'usuario_nombre': usuario.nombre,
        'usuario_email': usuario.email,
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
    return token.decode('utf-8')


"""
   raise FieldError(
django.core.exceptions.FieldError: Cannot resolve keyword 'Email' into field. Choices are: comentarios, contraseña, descripcion, email, fotoperfil, id, nombre, publicacion, seguidores_de, token, usuarios_seguidos


AttributeError: 'Manager' object has no attribute 'create_user'
--------

   raise FieldError(
django.core.exceptions.FieldError: Cannot resolve keyword 'username' into field. Choices are: comentarios, contraseña, descripcion, email, fotoperfil, id, nombre, publicacion, seguidores_de, token, usuarios_seguidos
__________________

    usuario.set_password(contraseña)
AttributeError: 'Usuarios' object has no attribute 'set_password


"""
