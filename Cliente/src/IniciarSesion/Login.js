import "./login.css";
import logo from "../Imagenes/Logo.PNG";
import React, { useState, useEffect } from "react";
import axios from "axios";
import BASE_URL from "../URL_SitioWeb"

const Login = (props) => {
  const [form, setForm] = useState({
    email: "",
    contrasena: "",
  });

  const onContenidoCorreo = (e) => {
    setForm({
      email: e.target.value,
      contrasena: form.contrasena,
    });
  };

  const onContenidoContraseña = (e) => {
    setForm({
      email: form.email,
      contrasena: e.target.value,
    });
  };

  const enviarFormulario = (e) => {
    e.preventDefault();
    axios.post(BASE_URL+"/endpoint", {
        email: form.email,
        contrasena: form.contrasena
      })
      .then((response) => {
        console.log(response);
        localStorage.setItem("token", response.data.Token);
        console.log(localStorage.getItem)
        // Realiza alguna acción con la respuesta del servidor
      })
      .catch((error) => {
        if (error.response.status == 404) {
            alert("error")
        }
        // Maneja cualquier error que pueda surgir
      });
  };

  return (
    <div className="fondo">
      <div className="Principal">
        <div className="logo">
          <img src={logo}></img>
        </div>

        <div className="registro">
          <form onSubmit={enviarFormulario} className="form">
            <b className="is">Iniciar Sesion</b>
            <input
              onChange={onContenidoCorreo}
              className="email"
              type="text"
              placeholder="Email..."
            ></input>
            <input
              onChange={onContenidoContraseña}
              className="contraseña"
              type="text"
              placeholder="Contraseña..."
            ></input>
            <a className="enlaceCrearCuenta" href="#">
              Crear una nueva cuenta
            </a>
            <button className="EnviarInicioSesion" type="submit">
              Iniciar Sesion
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};
export default Login;