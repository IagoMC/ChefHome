import logo from './logo.svg';
import './App.css';
import Cabecera from "./cabecera/Cabecera";
import {Route,Routes} from 'react-router-dom';
import Login from './IniciarSesion/Login';
function App() {
  return (
    <Routes>
      <Route path='/' element={<Cabecera/>}></Route>
      <Route path='/login' element={<Login/>}></Route>
 </Routes>
  );
}

export default App;
