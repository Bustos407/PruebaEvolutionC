import React, { useState, useEffect } from 'react';
import axios from 'axios';

const BookForm = () => {
    const [titulo, setTitulo] = useState('');
    const [autorId, setAutorId] = useState('');
    const [categoria, setCategoria] = useState('');
    const [cantidadDisponible, setCantidadDisponible] = useState('');
    const [books, setBooks] = useState([]);
    const [authors, setAuthors] = useState([]);
    const [editBookId, setEditBookId] = useState(null);

    useEffect(() => {
        fetchBooks();
        fetchAuthors();
    }, []);

    // Función para obtener libros
    const fetchBooks = async () => {
        const response = await axios.get('http://localhost:5000/libros');
        setBooks(response.data);
    };

    // Función para obtener autores
    const fetchAuthors = async () => {
        const response = await axios.get('http://localhost:5000/autores');
        setAuthors(response.data);
    };

    // Manejar el envío del formulario
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (editBookId) {
            await axios.put(`http://localhost:5000/libros/${editBookId}`, {
                titulo,
                autor_id: autorId,
                categoria,
                cantidad_disponible: cantidadDisponible
            });
            setEditBookId(null);
        } else {
            await axios.post('http://localhost:5000/libros', {
                titulo,
                autor_id: autorId,
                categoria,
                cantidad_disponible: cantidadDisponible
            });
        }
        // Reiniciar campos
        setTitulo('');
        setAutorId('');
        setCategoria('');
        setCantidadDisponible('');
        fetchBooks(); // Actualizar la lista de libros
    };

    // Manejar la edición de un libro
    const handleEdit = (book) => {
        setTitulo(book.titulo);
        setAutorId(book.autor_id);
        setCategoria(book.categoria);
        setCantidadDisponible(book.cantidad_disponible);
        setEditBookId(book.id);
    };

    // Manejar la eliminación de un libro
    const handleDelete = async (id) => {
        await axios.delete(`http://localhost:5000/libros/${id}`);
        fetchBooks(); // Actualizar la lista de libros
    };

    // Efecto para actualizar autores en tiempo real
    useEffect(() => {
        const interval = setInterval(() => {
            fetchAuthors(); // Actualiza la lista de autores cada 5 segundos
        }, 5000);

        return () => clearInterval(interval); // Limpiar el intervalo al desmontar
    }, []);

    return (
        <div>
            <h2>{editBookId ? 'Actualizar Libro' : 'Añadir Libro'}</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={titulo}
                    onChange={(e) => setTitulo(e.target.value)}
                    placeholder="Título del libro"
                    required
                />
                <select
                    value={autorId}
                    onChange={(e) => setAutorId(e.target.value)}
                    required
                >
                    <option value="">Seleccionar autor</option>
                    {authors.map((author) => (
                        <option key={author.id} value={author.id}>
                            {author.nombre}
                        </option>
                    ))}
                </select>
                <input
                    type="text"
                    value={categoria}
                    onChange={(e) => setCategoria(e.target.value)}
                    placeholder="Categoría"
                    required
                />
                <input
                    type="number"
                    value={cantidadDisponible}
                    onChange={(e) => setCantidadDisponible(e.target.value)}
                    placeholder="Cantidad disponible"
                    required
                />
                <button type="submit">{editBookId ? 'Actualizar Libro' : 'Agregar Libro'}</button>
            </form>
            <h3>Lista de Libros</h3>
            <ul>
                {books.map((book) => (
                    <li key={book.id}>
                        {book.titulo}
                        <button onClick={() => handleEdit(book)}>Actualizar</button>
                        <button onClick={() => handleDelete(book.id)}>Eliminar</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default BookForm;
