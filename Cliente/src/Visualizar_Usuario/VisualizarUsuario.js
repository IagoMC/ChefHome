import React, { useState, useEffect } from "react";
import axios from "axios";
import BASE_URL from "../URL_SitioWeb";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import './VisualizarUsuario.css'
const VisualizarUsuario = (props) => {


  const navigate = useNavigate();

  return <div className="Fondo_VisualizarUsuario">
    <div className="Contenedor_visualizarUsuario">
    <img className="ImagenUsuario_VisualizarUsuario"></img>
    <p className="NombreUsuario_VisualizarUsuario">Nombre</p>
    <p className="DescripcionUsuario_VisualizarUsuario">Descripcion</p>

    </div>
  </div>;
};

export default VisualizarUsuario;
