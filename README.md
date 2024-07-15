# Night Club by Zona Sur

## Repositorio de:
- (Nombre) - (Legajo)
- Dopacio Ricardo Tomas - 111097  
- Matías Ezequiel Kornuta - 110742
- Martín Ignacio Rossi - 111448

## Requerimiento
- Posgresql version : 14.12
- pip install requierements.txt 

## Descripción

Night Club es un proyecto realizado para la materia de "Introducción al desarrollo de software" de la FIUBA (Facultad de Ingeniería de Buenos Aires).   
Dicho proyecto consiste en realizar una página web implementando lo visto en clase.   
Nuestro proyecto consta de un menú para un club nocturno/bar para que a la hora de acceder, los precios estén disponibles de manera digital y los clientes puedan consultar el menú sin necesidad de acceder físicamente al club. Esto facilitaría a los clientes el proceso de pedido, ya que no tendrían que consultar los precios ni acceder a un menú físico, permitiendo un servicio más rápido y eficiente.   
Esta demostración está dedicada al empleador para que pueda probar cómo se crean, leen, actualizan y eliminan productos.

### Responsabilidades

Para el desarrollo de este proyecto dividimos las tareas en tres partes: manejo del backend, frontend dividido en la página principal y los formularios.

## Funcionamiento

### Página Principal (Frontend)

Comenzaremos explicando el funcionamiento del frontend, que constará con la página principal donde se mostrarán los productos actuales. La página incluirá un encabezado con una barra de navegación que contendrá el logo, las categorías, un botón para crear productos y unb boton para crear combos. Este botón redireccionará a un formulario para la creación de productos y a un formulario para la creacion del combo.   
Luego, en el contenido principal (main), se mostrarán los productos separados semánticamente por secciones, y cada sección incluirá artículos.   
Cada artículo mostrará el nombre, la descripción, el precio y dos botones: uno para eliminar y otro para editar el producto.   
El botón de eliminar llamará a una función (`function eliminar_producto(id, tabla)`) que enviará al backend el id del producto a eliminar mediante el método `DELETE`, junto con la tabla donde se encuentra el producto.   
El botón de editar simplemente redireccionará a un formulario para editar los datos del producto.
Los combos solo tendran la opcion de eliminarlos, pero no la opcion de editarlos.
Se manejó dinámicamente con JavaScript la información recibida del backend para mostrar los productos en la página principal con HTML de manera semántica. Los productos obtuvieron sus estilos a través de un archivo CSS, y Bootstrap solo se utilizó para aplicar un modo oscuro.


## Formularios (Frontend)

En el apartado de los formularios se encuentran los siguientes formularios:

- Formulario de creación: Este formulario consta de etiquetas a completar que indican el nombre del producto, tipo de producto, descripción, precio y la imagen. Se ejecuta una función que toma el formulario y sus datos, crea una nueva instancia con los datos del formulario en pares clave-valor. Luego, se realiza una solicitud con el método `PUT` y el cuerpo del formulario en formato clave-valor para manipularlo en el backend como un diccionario en Python. Finalmente, el producto creado se agrega a la base de datos y una vez relizado el formulario, el producto ya se encuentra en la pagina principal.

- Formulario de Edición: El siguiente formulario, a diferencia del de creación de combo, realiza una solicitud al backend del tipo `GET` con la información del tipo de producto a editar y su ID correspondiente. Esto se hace con el propósito de encontrar el producto mediante una consulta y devolver la información necesaria para la edición. Una vez recibida la información, se ejecuta una función que completa los campos del formulario con los datos del producto a editar. Una vez que se editan los campos y se clikea el voton `ENVIAR`, se realiza otra solicitud al backend con el método `PUT`, enviando la nueva información del formulario con el producto editado para actualizarlo en la base de datos.

- Formulario de Creacion de Combo: El siguiente formulario lleva a cabo la creación de un combo con los productos disponibles que fueron subidos a la página principal. Primero, se realiza una solicitud al backend del tipo `GET` para obtener los datos de todas las tablas de comidas, bebidas y tragos. Estos datos se manipulan de manera que, al seleccionar el tipo de producto que conformará el combo, aparezcan las opciones disponibles para su creación. Una vez que se envía el formulario haciendo clic en el botón `ENVIAR`, se ejecuta una función que envía el formulario al backend para luego agregarlo a la página principal.

## BACKEND 

El backend consta de dos archivos: uno llamado `models.py`, donde se crean las tablas en la base de datos, y otro llamado `app.py`, donde está la lógica de los endpoints y la gestión de la base de datos.


La base de datos consta de 4 tablas:
- Comidas
- Bebidas
- Tragos
- Combos

Las tablas tienen los siguientes campos:

- Id
- Nombre
- Descripción
- Precio
- Imagen

Además, la tabla `Combos` tiene como foreign keys los IDs de una comida, una bebida y un trago. Estos IDs se utilizan para establecer y actualizar las descripciones y precios de los combos que los contienen.

La API consta de 3 endpoints diferentes:
1. El primer endpoint `@app.route("/")` obtiene todos los elementos de la base de datos mediante el método `GET`. Esto permite recibirlos en el frontend y mostrar los productos en la página principal.

2. El segundo endpoint `@app.route("/modificar", methods=["DELETE", "PUT", "GET"])` permite acceder con 3 métodos diferentes (`GET`, `DELETE` y `PUT`):
   - Con `GET`, se obtiene un solo elemento con sus datos.
   - Con `DELETE`, se borra un elemento y todos los combos que lo contenían.
   - Con `PUT`, se actualiza el producto y los combos que lo contienen.

3. Por último, está el endpoint `@app.route("/crear/<producto>", methods=["POST"])` que se utiliza para crear un producto o un combo utilizando el método POST.
