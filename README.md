# Proyecto-Flask
## Debemos crear una aplicación dinámica en python flask con las siguientes características:

1. Escogemos una plantilla html5 gratuita y la usamos para crear una plantilla base.html.
	- La plantilla que hemos escogido es [strata en html5up.net](https://html5up.net/strata)
2. La aplicación nos va a permitir mostrar información de libros. Esa información está guardada en el fichero books.json.
3. La página principal debe mostrar una página donde ponga vuestro nombre, un título con la palabra "Biblioteca" y una lista de enlaces donde se vean los nombres de todos los libros y que nos lleve a una ruta del tipo /libro/<isbn> o /libro?isbn=xxxxxx. Es decir si el libro 1 tienes ISBN 1933988673 el enlace nos llevara a la ruta /libro/1933988673 o a la URL /libro?isbn=1933988673. Elige la manera de enviar información (URL con parámetros o rutas dinámicas).
4. Página detalle del libro. La ruta será /libro/*<isbn>* o /libro, que mostrará un título con el nombre del libro, una imagen del libro (campo thumbnailUrl) y la siguiente información del libro: Número de páginas, descripción, autores y categorías.
	- Si el ISBN no existe se devolverá un error 404.
	- Si el valor del campo status es igual a MEAP mostraremos un mensaje que diga "ESTE LIBRO NO SE HA PUBLICADO" (usar un if dentro de la plantilla).

### Posible mejora
- Cuando se muestra el detalle de un libro y se muestran las categorías, estás son un enlace a la ruta /categoria/<categoria>. Por ejemplo, si el primer libro tiene una categoría  Mobile, al pulsar sobre el enlace nos lleva a la página /categoria/Mobile o /categora?id=Mobile
- Libros por categoría: Esta página está en la ruta /categoria/*<categoria>* o en la ruta /categoria: Es muy similar a la página principal, pero sólo muestra la los libros de esa categoría. Además debe a aparecer un título con la categoría.
