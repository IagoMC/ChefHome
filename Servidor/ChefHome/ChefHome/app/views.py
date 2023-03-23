from django.contrib.auth import authenticate, login, logout
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
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.views import APIView

from rest_framework.authentication import TokenAuthentication

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
def login_user(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        campos_requeridos = ['email', 'contrasena']
        for campo in campos_requeridos:
            if campo not in body:
                return JsonResponse({'mensaje': f'Falta campo requerido: {campo}'}, status=400)

        email = body.get('email')
        contrasena = body.get('contrasena')

        usuario = Usuarios.objects.filter(email=email).first()
        if usuario is not None:
            if usuario.check_password(contrasena):
                payload = {
                    'usuario_id': usuario.id,
                    'usuario_nombre': usuario.nombre,
                    'usuario_email': usuario.email,
                }
                token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
                usuario.token = token
                usuario.save()
                return JsonResponse({'token': str(token)})
            else:
                return JsonResponse({'mensaje': 'Contraseña incorrecta'}, status=401)
        else:
            return JsonResponse({'mensaje': 'Email incorrecto'}, status=401)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class editar_Usuario(APIView):
    def get(self, request):
        usuario = request.Usuarios
        data = {
            'nombre': usuario.nombre,
            'descripcion': usuario.descripcion,
            'fotoperfil': usuario.fotoperfil.url
        }
        return JsonResponse(data)



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



   return view_func(*args, **kwargs)
TypeError: login() takes 1 positional argument but 2 were given



    return view_func(*args, **kwargs)
TypeError: login() got an unexpected keyword argument 'backend'

_______________________


    raise errorclass(errno, errval)s
django.db.utils.ProgrammingError: (1146, "Table 'ChefHome.django_session' doesn't exist")
----
ValueError: The following fields do not exist in this model, are m2m fields, or are non-concrete fields: last_login

"""
