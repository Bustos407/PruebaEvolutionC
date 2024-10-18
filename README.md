# Prueba Tecnica Evolution Consulting
## Consulta SQL
SELECT 
    L.titulo AS Titulo,
    C.nombre AS Categoria
FROM 
    Libros L
JOIN 
    Categorias C ON L.categoria_id = C.id
WHERE 
    L.autor_id = "ID del Autor";

## Optimización de Consulta:
1. Crear índices en las columnas que utilizo en las cláusulas JOIN y WHERE. En este caso:
  - `autor_id` en la tabla `Libros` para acelerar la búsqueda de libros por autor.
  - `categoria_id` en la tabla `Libros` para mejorar la unión con la tabla `Categorias`.
  - `nombre` en la tabla `Autores`, especialmente si se utiliza el nombre del autor para poder filtrar.

2. Si la tabla Libros se vuelve muy grande, se puede particionar para mejorar el rendimiento
