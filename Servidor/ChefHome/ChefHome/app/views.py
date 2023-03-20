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
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.hashers import check_password


@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        email = datos.get('email')
        contraseña = datos.get('contrasena')
        confirm_contraseña = datos.get('confirmarContrasena')
        nombre = datos.get('nombre')
        
        # Validamos que los campos obligatorios hayan sido suministrados
        if not email:
            return JsonResponse({'mensaje': 'Debe suministrar el correo electrónico'})
        if not nombre:
            return JsonResponse({'mensaje': 'Debe suministrar el nombre'})
        if not contraseña:
            return JsonResponse({'mensaje': 'Debe suministrar la contraseña'})
        if not confirm_contraseña:
            return JsonResponse({'mensaje': 'Debe confirmar la contraseña'})
        
        # Validamos que las contraseñas coincidan
        if contraseña != confirm_contraseña:
            return JsonResponse({'mensaje': 'Las contraseñas no coinciden'})
        
        # Validamos que no exista un usuario con el mismo correo electrónico o nombre
        usuario_existente = None
        if Usuarios.objects.filter(email=email).exists():
            usuario_existente = "correo electrónico"
        elif Usuarios.objects.filter(nombre=nombre).exists():
            usuario_existente = "nombre"
            
        if usuario_existente:
            return JsonResponse({'mensaje': f'Ya existe este {usuario_existente}'})
                  
        # Creamos el usuario y guardamos su contraseña con set_password
        usuario = Usuarios(nombre=nombre, email=email, contraseña=make_password(contraseña))
        usuario.save()
        
        return JsonResponse({'mensaje': 'Usuario creado exitosamente'})
    else:
        return JsonResponse({'mensaje': 'Este endpoint solo acepta solicitudes POST'})
    
    
@csrf_exempt    
def login(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        campos_requeridos = ['email', 'contrasena']
        for campo in campos_requeridos:
            if campo not in body:
                return JsonResponse({'error': f'Falta campo requerido: {campo}'}, status=400)

        email = body.get('email')
        contraseña = body.get('contrasena')

        usuario = authenticate(request, email=email, password=contraseña)
        if usuario is not None:
            login(request, usuario)
            token = get_token(usuario)
            usuario.token = token
            usuario.save()
            return JsonResponse({'token': token})
        else:
            usuario_existente = Usuarios.objects.filter(email=email).exists()
            if usuario_existente:
                usuario = Usuarios.objects.get(email=email)
                if check_password(contraseña, usuario.contraseña):
                    return JsonResponse({'error': 'Contraseña incorrecta'}, status=401)
                else:
                    return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
            else:
                return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    else:
        return render(request, 'home.html')
    
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

___--
   usuario_existente = Usuarios.objects.filter(email=email).exists()
AttributeError: 'NoneType' object has no attribute 'objects'

"""
