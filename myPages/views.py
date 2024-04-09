from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('''
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Inicio</title>
    <style>
        body {
            font-family: Arial, sans-serif; /* Estilo de fuente para el cuerpo del documento */
            margin: 40px; /* Margen alrededor del contenido de la página */
            background-color: #f4f4f9; /* Color de fondo de la página */
            color: #333; /* Color del texto */
        }
        h1 {
            color: #4a67a1; /* Color del texto del encabezado */
        }
        p {
            font-size: 16px; /* Tamaño del texto del párrafo */
            line-height: 1.6; /* Espaciado entre líneas */
        }
    </style>
</head>
<body>
    <h1>Bienvenido a Nuestra Página</h1>
    <p>Este es un texto de relleno para mostrar cómo aparecerá el contenido en tu página de inicio. Aquí puedes incluir información relevante sobre tu sitio web o cualquier tema de interés general. Este párrafo sirve para dar una breve introducción y captar la atención del lector.</p>
</body>
</html>
  '''
  )

def about(request):
  return HttpResponse('''
  <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Acerca de Nosotros</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Usa una fuente clara y legible */
            margin: 40px; /* Margen para dar espacio alrededor del contenido */
            background-color: #f0f4f8; /* Un color de fondo suave */
            color: #333; /* Color del texto oscuro para contrastar con el fondo */
        }
        h1 {
            color: #0056b3; /* Un color de encabezado distintivo */
        }
        p {
            font-size: 18px; /* Un tamaño de fuente ligeramente mayor para el texto */
            line-height: 1.8; /* Espaciado de línea para mejorar la legibilidad */
        }
    </style>
</head>
<body>
    <h1>Acerca de Nosotros</h1>
    <p>En esta página encontrarás información relevante sobre nuestra empresa y nuestros valores. Nuestra misión es proporcionar productos y servicios de la más alta calidad a nuestros clientes, manteniendo un compromiso firme con la sostenibilidad y la innovación.</p>
    <p>Nuestro equipo está compuesto por profesionales apasionados y dedicados que trabajan incansablemente para superar las expectativas de nuestros clientes. Estamos orgullosos de nuestra historia y emocionados por el camino que tenemos por delante.</p>
</body>
</html>


  '''
  )

def contact(request):
  return HttpResponse('''
  <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contacto</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 20px;
            background-color: #f0f2f5;
            color: #333;
        }
        form {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: #ffffff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            font-weight: bold;
            display: block;
            margin-top: 20px;
        }
        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            box-sizing: border-box; /* Makes sure the padding doesn't affect the overall width */
        }
        textarea {
            height: 120px;
            resize: vertical; /* Allows the user to vertically resize the textarea (not horizontally) */
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            margin-top: 20px;
            border: none;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Contacto</h1>
    <form action="#" method="POST">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>

        <label for="company">Empresa:</label>
        <input type="text" id="company" name="company" required>

        <label for="position">Cargo:</label>
        <input type="text" id="position" name="position">

        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Mensaje:</label>
        <textarea id="message" name="message"></textarea>

        <button type="submit">Enviar</button>
    </form>
</body>
</html>

  '''
  )




