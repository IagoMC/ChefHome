import React, { useState, useEffect } from "react";
import axios from "axios";
import BASE_URL from "../URL_SitioWeb";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import "./EditarUsuario.css";
const EditarUsuario = (props) => {
  const navigate = useNavigate();

  return (
    <div className="Fondo_EditarUsuario">
      <div className="Contenedor_EditarUsuario">
        <img className="ImagenUsuario_EditarUsuario"></img>
        <div className="Nombre_y_Descripcion_EditarUsuario">
          <p className="NombreUsuario_EditarUsuario">Nombre</p>
          <p className="DescripcionUsuario_EditarUsuario">Descripcion</p>
        </div>

        <div className="Botones_EditarUsuario">
          <button className="BotonCambiarContraseña_EditarUsuario">
            Cambiar Contraseña
          </button>
          <button className="BotonCrearPublicacion_EditarUsuario">
            Crear Publicacion
          </button>
        </div>
      </div>
    </div>
  );
};

export default EditarUsuario;
