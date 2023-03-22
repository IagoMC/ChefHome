import "./login.css";
import logo from "../Imagenes/Logo.PNG";
import React, { useState, useEffect } from "react";
import axios from "axios";
import BASE_URL from "../URL_SitioWeb";
import { navigate, useNavigate } from 'react-router-dom';
import { Link } from "react-router-dom";

const Login = (props) => {
  const [email, setEmail] = useState("");
  const [contrasena, setContrasena] = useState("");
  const navigate = useNavigate()
  const enviarFormulario = (e) => {
    e.preventDefault();
    axios
      .post(
        BASE_URL + "/login",
        {
          email,
          contrasena,
        },
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      )
      .then((response) => {
        alert(response.data.mensaje);
        console.log(response);
        localStorage.setItem("token", response.data.token);
        let valor = localStorage.getItem("token");
        console.log("Valor del token del usuarios:",valor)

        console.log(email);
        console.log(contrasena);
        navigate('/')

        // Realiza alguna acción con la respuesta del servidor
      })
      .catch((error) => {
        if (error.response) {
     
          if (error.response.status === 401) {
            alert("Credenciales inválidas");
          } else if (error.response.status === 404) {
            alert("No se encontró la página");
          } else {
            alert("Ocurrió un error al procesar la solicitud");
          }
        } else {
          alert("No se pudo conectar con el servidor");
        }
      });
  };

  return (
    <div className="fondo">
      <div className="Principal">
      <Link className="logo" to="/home">
          <img  src={logo}></img>
        </Link>

        <div className="registro">
          <form onSubmit={enviarFormulario} className="form">
            <b className="is">Iniciar Sesion</b>
            <input
              onChange={(event) => setEmail(event.target.value)}
              className="email"
              type="email"
              placeholder="Email..."
              required 
            ></input>
            <input
              onChange={(event) => setContrasena(event.target.value)}
              className="contraseña"
              type="password"
              placeholder="Contraseña..."
              required 
            ></input>
            <Link to="/crear_usuario">
              Crear una nueva cuenta
            </Link>
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
