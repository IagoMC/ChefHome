import logo from './logo.svg';
import './App.css';
import Cabecera from "./cabecera/Cabecera";
import {Route,Routes} from 'react-router-dom';
import Login from './IniciarSesion/Login';
import CrearUsuario from './CrearUsuario/CrearUsuario'
function App() {
  return (
    <Routes>
      <Route path='/' element={<Cabecera/>}></Route>
      <Route path='/login' element={<Login/>}></Route>
      <Route path='/crear_usuario' element={<CrearUsuario/>}></Route>

 </Routes>
  );
}

export default App;
