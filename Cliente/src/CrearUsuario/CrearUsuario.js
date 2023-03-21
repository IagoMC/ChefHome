import logo from "../Imagenes/Logo.PNG";
import React, { useState, useEffect } from "react";
import axios from "axios";
import BASE_URL from "../URL_SitioWeb";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import "./crearusuario.css";
const CrearUsuario = (props) => {
  const [email, setEmail] = useState("");
  const [nombre, setNombre] = useState("");
  const [contrasena, setContrasena] = useState("");
  const [confirmarContraseña, setConfirmarContraseña] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();

    if (contrasena !== confirmarContraseña) {
      alert("Las contraseñas no coinciden");
      return;
    }

    axios
      .post(`${BASE_URL}/crear_usuario`, {
        email,
        nombre,
        contrasena,
        confirmarContrasena: confirmarContraseña,
      })
      .then((response) => {
        alert(response.data.mensaje);
        console.log("okey");
      })
      .catch((error) => {
        alert(error.response.data.error);
      });
  };
  return (
    <div className="fondo">
      <div className="Principal_CrearUsuario">
        <Link className="logo" to="/home">
          <img  src={logo}></img>
        </Link>
        <div className="CrearUsuario">
          <form className="form_CrearUsuario" onSubmit={handleSubmit}>
            <b className="cu">Crear Usuario</b>
            <input
              className="email_CrearUsuario"
              type="text"
              placeholder="Email..."
              value={email}
              onChange={(event) => setEmail(event.target.value)}
            ></input>
            <input
              className="nombre_crearUsuario"
              type="text"
              placeholder="Nombre..."
              value={nombre}
              onChange={(event) => setNombre(event.target.value)}
            ></input>
            <input
              className="contraseña_CrearUsuario"
              type="password"
              placeholder="Contraseña..."
              value={contrasena}
              onChange={(event) => setContrasena(event.target.value)}
            ></input>
            <input
              className="ccontraseña_CrearUsuario"
              type="password"
              placeholder="Confirmar Contraseña"
              value={confirmarContraseña}
              onChange={(event) => setConfirmarContraseña(event.target.value)}
            ></input>
            <Link className="enlaceCrearCuenta" to="/login">
              Iniciar Sesion
            </Link>
            <button className="EnviarInicioSesion" type="submit">
              Crear Usuario
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default CrearUsuario;
