// Autores.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Autores = () => {
  const [autores, setAutores] = useState([]);
  const [nombre, setNombre] = useState('');
  const [idActualizar, setIdActualizar] = useState('');
  const [nuevoNombre, setNuevoNombre] = useState('');

  // Obtener la lista de autores
  const obtenerAutores = async () => {
    try {
      const response = await axios.get('http://localhost:5000/autores');
      setAutores(response.data);
    } catch (error) {
      console.error('Error al obtener autores:', error);
    }
  };

  // Agregar un nuevo autor
  const agregarAutor = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:5000/autores', { nombre });
      setNombre('');
      obtenerAutores(); // Actualizar la lista de autores
    } catch (error) {
      console.error('Error al agregar autor:', error);
    }
  };

  // Actualizar un autor
  const actualizarAutor = async (e) => {
    e.preventDefault();
    try {
      await axios.put(`http://localhost:5000/autores/${idActualizar}`, { nombre: nuevoNombre });
      setIdActualizar('');
      setNuevoNombre('');
      obtenerAutores(); // Actualizar la lista de autores
    } catch (error) {
      console.error('Error al actualizar autor:', error);
    }
  };

  useEffect(() => {
    obtenerAutores(); // Cargar autores al montar el componente
  }, []);

  return (
    <div>
      <h1>Gestión de Autores</h1>
      
      <form onSubmit={agregarAutor}>
        <input
          type="text"
          placeholder="Nombre del autor"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          required
        />
        <button type="submit">Agregar Autor</button>
      </form>

      <h2>Lista de Autores</h2>
      <ul>
        {autores.map((autor) => (
          <li key={autor.id}>
            {autor.nombre}
            <button onClick={() => {
              setIdActualizar(autor.id);
              setNuevoNombre(autor.nombre);
            }}>
              Editar
            </button>
          </li>
        ))}
      </ul>

      {idActualizar && (
        <form onSubmit={actualizarAutor}>
          <input
            type="text"
            placeholder="Nuevo nombre del autor"
            value={nuevoNombre}
            onChange={(e) => setNuevoNombre(e.target.value)}
            required
          />
          <button type="submit">Actualizar Autor</button>
        </form>
      )}
    </div>
  );
};

export default Autores;
