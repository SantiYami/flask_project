# README

## Database

La base de datos usada es PostgreSQL 12.

Para crear la base de datos ingrese a postgres ejecute el siguiente [archivo](db.sql), adicional ejecute los inserts de ejemplo.

En el archivo [.env](.env) coloque las credenciales para su base de datos.

Para dar inicio al proyecto use los siguientes comandos

```bash
#Crear entorno virtual
python -m venv .venv

#Activar entorno virtual Windows
.venv/Scripts/activate

#Activar entorno virtual Linux
.venv/bin/activate

#Desactivar Entorno virtual
deactivate

#Instalación inicial: 
pip install -r requirements.txt

#Ejecutar la aplicación: 
flask run
```

### Acceder a la aplicación

Abrir la siguiente URL en su navegador: [http://localhost:5000/](http://localhost:5000/)
