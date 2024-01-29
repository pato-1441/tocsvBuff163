# toCSVBUFF163
v0.1 (28/01/24)
Proyecto basando sobre: https://github.com/perrebser/buff163Prices.
Este programa te va a permitir trasladar los precios de BUFF163, desde una lista de items de CSGO en un .txt, a un archivo CSV. La idea es que en versiones proximas se puede trasladar directamente a un Google Sheet, asi tambien rellenar el .txt desde ahi también.

## Características
- Verificar precios de venta para artículos específicos
- Revisar órdenes de compra
- Convertidor de moneda (CNY to USD)
- Búsqueda por rango de float
- Información sobre registros de comercio en la página

## Requisitos

Antes de utilizar este programa, asegúrate de tener los siguientes requisitos:

1. Python: Necesitarás tener [Python](https://www.python.org/) instalado en tu sistema.

## Instalación

Sigue estos pasos para instalar y configurar el programa:

1. Clona o descarga este repositorio en tu máquina local.

2. Navega a la carpeta del proyecto.

3. Instala las dependencias necesarias utilizando el siguiente comando:</br>
   `pip install -r requirements.txt`

## Uso

Para utilizar el programa, sigue estos pasos:

1. Ejecuta el archivo main.py desde la línea de comandos o utilizando tu IDE favorito.
2. Se te pedirá que ingreses cuántas ofertas para un artículo quieres revisar. (1,2,3... Para la oferta más barata, las dos ofertas más baratas...)
3. Los nombres de los articulos a revisar seran extraidos de items.txt, con un formato como el siguiente: "★ M9 Bayonet | Bright Water (Field-Tested)".
4. Puedes especificar si quieres información sobre órdenes de compra para los artículos especificados.
5. El programa generará un archivo CSV en la carpeta  "results/prices.csv" con el nombre de los artículos, su precio y otros atributos relevantes como la fase en Dopplers o el porcentaje de fade en Fades.

### Ejemplo
Capturas de pantalla para la entrada y su correspondiente respuesta en el archivo CSV:

## Configuración de cookies de Buff163

Ve a [buff163](https://buff.163.com), obtén los valores de tu cookie (necesarios para ciertas funciones, como la búsqueda por rango de float). Sigue estos pasos (necesitas iniciar sesión primero):

1. Presiona F12 para abrir la consola de desarrollador
2. Ve a la pestaña Network y refresca la web (F5)
3. Encuentra el archivo con nombre similar a "v2" en la lista, haz click en él y en el apartado "Cookies" vas a encontrar la configuración de tu cuenta
4. Copia el valor de Device-Id, session y csrf_token y pégalo en tu `.env` (necesitas el valor de **Device-Id**; **session**; **csrf_token**)
5. Tu `.env` debería verse así si quieres buscar por float mínimo y máximo

---

## Créditos

Quisiera expresar mi gratitud principalmente a [perrebser](https://github.com/perrebser) por proporcionar la estructura base para el proyecto, asi como a [ModestSerhat](https://github.com/ModestSerhat) por proporcionar el repositorio [buff163-ids](https://github.com/ModestSerhat/buff163-ids) que fue instrumental para obtener los IDs de artículos de CS:GO para este proyecto. Sus trabajos han contribuido enormemente a la funcionalidad de este programa.
