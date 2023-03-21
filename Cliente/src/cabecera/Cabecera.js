import { useNavigate } from "react-router-dom";
import "./cabecera.css";
import usuario from "./ImagenesCabecera/usuario.png";
import logo1 from "./ImagenesCabecera/Logo1.PNG";

const Cabecera = (props) => {
  const navigate = useNavigate();

  return (
    <div className="fondocabecera">
      <div className="cabecera">
        <div className="logo">
          <img src={logo1}></img>
        </div>
        <div className="navegacion">
          <div className="barraBusqueda">
            <form>
              <input type="text" placeholder="Buscar..." />
              <button type="submit">Buscar</button>
            </form>
          </div>
          <div className="menu">
            <a href="#" onClick={navigate("/")}>
              Platos
            </a>
            <a onClick={navigate("/")}>Entrantes</a>
            <a onClick={navigate("/")}>Bebidas</a>
            <a onClick={navigate("/")}>Postres</a>
          </div>
        </div>

        <div className="Contenedor1">
          <div className="seguidores">
            <a className="aseguidores" href="#">
              Seguidores
            </a>
          </div>
          <div className="SubirPublicaion"><a>+ Publicaion</a></div>
        </div>
        <div className="IconoSesion">
          <img src={usuario}></img>
        </div>
      </div>
    </div>
  );
};

export default Cabecera;
