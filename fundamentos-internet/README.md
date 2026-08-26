# Fundamentos de Internet 

## 1. Del Cliente al Servidor

El cliente busca la direccion ip asociada al dominio que estamos buscando
Se conecta al servidor DNS para obtener esa ip
El DNS funciona como un traductor o interprete que tiene las direcciones ip mas conocidas
utilizando nuestra busqueda para averiguar cual ip es la que buscamos
Ya con la ip el navegador se conecta al servidor correcto y envia una request usando el protocolo http con GET como metodo
El servidor recibe esa request, el routing la envia el endpoint correspondiente y devuelve una response con el contenido de hyper texto en el body del request, html en este caso
El navegador recibe el response y procesa el contenido html para renderizar el video en pantalla

## 2. Frontend y Backend en acción

La parte correspondiente del frontend es lo grafico, el diseño de la pagina web, botones, colores, imagenes, etc...
Suele ser la parte que el cliente ve las opcciones o apartados de la pagina
El backend corresponde a como por ejemplo la base de datos donde se almacena la informacion de los pacientes 
A lo que sucede a nivel interno al darle a crear cuenta o a añadir cita medica

Tecnologias para Backend:
1- Java Spring Boot
2- MySQL
3- Python

Tecnologias para Frontend:

1- HTML
2- CSS
3- JavaScript

El FrontEnd y el Backend se conectan mediante una API
El usuario realiza un cambio mediante el FrontEnd
Ejecuta el codigo JavaScript y realiza una request http
La request va al BackEnd
El BackEnd hace su trabajo en funcion del request como el de realizar una consulta a la base de datos
El BackEnd devuelve la response al FrontEnd para que reciba los datos

## 3. REST vs SOAP vs GraphQL

|Tipo de API  |Formato de datos usado  |Nivel de flexibilidad        |Dificultad de implementación      |Uso actual (Alta / Media / Baja)   |
|-------------|------------------------|-----------------------------|----------------------------------|-----------------------------------|
|REST         |JSON                    |El servidor-Flexibilidad Alta|Baja dificultad de implementacion |Alta                               |
|SOAP         |XML                     |El servidor-Flexibilidad Baja|Alta dificultad de implementacion |Media-Baja                         |
|GraphQL      |JSON                    |El cliente-Flexibilidad Alta |Media dificultad de implementacion|Alta                               |

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**

De acuerdo con el tipo de sistema considero que lo mas apropiado para este caso es utilizar REST
Un sistema de reservas puede tener cosas como usuarios, habitaciones, reservaciones, etc...
Y las operaciones http como get o delete encajan bien con lo que un sistema asi puede querer realizar
Ademas de que es relativamente sencillo de implementar lo que seria ideal al tratarse de una startup donde los requerimientos pueden cambiar rapidamente

## 4. Explorando APIs con Postman

### 4.1 Selección de la API
- **Nombre de la API:**
Restfull-api.dev
- **Descripción:**
Servicio funcional con base de datos real que permite publicar, almacenar y eliminar datos a traves de
peticiones HTTP reales.
Dando una experiencia similar a la de trabajar con una produccion real de BackEnd

### 4.2 Configuración en Postman
- **Nombre de la colección:**
Restfull-api.dev
- **Solicitudes agregadas:**
- GET - GET items
- POST - POST item
- PUT/PATCH/DELETE - DELETE item

### 4.3 Ejecución y análisis

| Solicitud | Método | Endpoint                                                            | Código de estado  | Notas                                                                                                                                          |
|-----------|--------|---------------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|getitems   |GET     |https://api.restful-api.dev/objects                                  |200                |Ofrece tambien un query parameter "string[]" con el cual se pueden especificar mas de un id para que la respuesta retorne una coleccion de items|
|postitem   |POST    |https://api.restful-api.dev/objects                                  |200                |La API permite cualquier estructura de datos siempre y cuando este en formato JSON, solo tiene un header requerido Content-Type-application/json|
|deleteitem |DELETE  |https://api.restful-api.dev/objects/ff8081819ff5b11001a03a6b8be72012 |200                |Se utiliza un path parameter requerido en el que enviaremos el id del objeto que queremos eliminar                                              |


### 4.4 Explicación técnica

#### [GetItems]
- **Método HTTP:**
GET
- **Endpoint:**
https://api.restful-api.dev/objects
- **Parámetros / body:**
Parametros: /objects
- **Descripción de la respuesta:**
En la respuesta obtenemos todos los objetos que existen listados en la base de datos
fragmento JSON:
[
    {
        "id": "1",
        "name": "Google Pixel 6 Pro",
        "data": {
            "color": "Cloudy White",
            "capacity": "128 GB"
        }
    },
    {
        "id": "2",
        "name": "Apple iPhone 12 Mini, 256GB, Blue",
        "data": null
    },
    {
        "id": "3",
        "name": "Apple iPhone 12 Pro Max",
        "data": {
            "color": "Cloudy White",
            "capacity GB": 512
        }
    },
    {
        "id": "4",
        "name": "Apple iPhone 11, 64GB",
        "data": {
            "price": 389.99,
            "color": "Purple"
        }
    },
    {
        "id": "5",
        "name": "Samsung Galaxy Z Fold2",
        "data": {
            "price": 689.99,
            "color": "Brown"
        }
    },
]

#### [PostItem]
- **Método HTTP:**
POST
- **Endpoint:**
https://api.restful-api.dev/objects
- **Parámetros / body:**
Body:
{
  "name": "Yeshua Rodriguez Valverde",
  "data": {
    "age": 23
  }
}
- **Descripción de la respuesta:**
En el response nos retorna una copia del body que enviamos en el request con informacion extra, en este caso el id del objeto creado y una fecha de creacion
Fragmento JSON:
{
    "id": "ff8081819ff5b11001a03a6b8be72012",
    "name": "Yeshua Rodriguez Valverde",
    "createdAt": 1787686521831,
    "data": {
        "age": 23
    }
}

#### [DeleteItem]
- **Método HTTP:**
DELETE
- **Endpoint:**
https://api.restful-api.dev/objects/{id}
- **Parámetros / body:**
Como path parameter se utiliza el {id} en el cual tiene que ir un int que corresponda al id del item que queremos eliminar
- **Descripción de la respuesta:**
En la response nos retorna un mensaje con el id del item que eliminamos para confirmar que el proceso se ejecuto con exito
Fragmento JSON:
{
    "message": "Object with id = ff8081819ff5b11001a03a6b8be72012 has been deleted."
}

**¿Qué aprendiste del proceso?**
Entendi mejor como interactuan el cliente y el servidor usando el protocolo HTTP y REST,
tambien la utilidad de los path parameters y los query parameters

### 4.5 Reflexión final

De las API entendi mejor la funcion que cumplen entre la comunicacion del backend y el frontend y las maneras en las que se pueden utilizar
No lograba comprender bien la forma en la que el protocolo http enviaba request usando apis y la forma en la que funciona el protocolo
ya que hay un flujo de request/response entre el cliente y el servidor pero tambien entre el backend y frontend y me confundia
Es un tema bastante conceptual dificil de visualizar de forma clara lo que hace que me cueste un poco entenderlo bien
Ahora diferencio mejor entre HTTP y las api, las confundia un poco ya que rest y http son muy similares por lo que tambien me confundio un poco al inicio creyendo que todas las api funcionaban igual que http
pero ya tengo una idea mas clara y entiendo que en el caso de rest esa es una de sus ventajas, entender http hace que entender rest sea mucho mas facil por sus similitudes

Todas estas ideas me quedaron mas claras tambien gracias a postman ya que al practicar con apis que simulan un ambiente de trabajo mas real
logre entender mejor la diferencia entre api y htttp, tambien el proceso con el cual el servidor manipula las request para enviarlas al endpoint correcto
Tambien el concepto de endpoint en si me quedo claro ya que antes de iniciar con este tema no tenia ni idea de lo su definicion y funcionamiento


