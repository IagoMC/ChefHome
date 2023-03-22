import logo from './logo.svg';
import './App.css';
import Cabecera from "./cabecera/Cabecera";
import {Route,Routes} from 'react-router-dom';
import Login from './IniciarSesion/Login';
import CrearUsuario from './CrearUsuario/CrearUsuario'
import VisualizarUsuario from './Visualizar_Usuario/VisualizarUsuario';
import EditarUsuario from './Editar_Usuario/EditarUsuario';
function App() {
  return (
    <Routes>
      <Route path='/' element={<Cabecera/>}></Route>
      <Route path='/login' element={<Login/>}></Route>
      <Route path='/crear_usuario' element={<CrearUsuario/>}></Route>
      <Route path='/visualizar_usuario' element={<VisualizarUsuario/>}></Route>
      <Route path='/editar_usuario' element={<EditarUsuario/>}></Route>

 </Routes>
  );
}

export default App;
