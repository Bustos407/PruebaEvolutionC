import React from 'react';
import AuthorForm from './Components/AuthorForm';
import BookForm from './Components/BookForm';

const App = () => {
    return (
        <div>
            <h1>Biblioteca</h1>
            <AuthorForm />
            <BookForm />
        </div>
    );
};

export default App;
