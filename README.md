# Wikiuma

## Setup

Para poder trabajar en el proyecto, se recomienda usar un entorno virtual de Python para que todos los desarrolladores tengan las mismas dependencias en las mismas versiones.

Para crear el entorno virtual, en la raíz del proyecto se debe ejecutar:

```bash
python -m venv <nombre>
```

Para nombre se recomienda usar `venv` ya que está incluído en [`.gitignore`](./.gitignore).

**¡Atención! No subir la carpeta del entorno virtual al repositorio**

El siguiente paso es activar el entorno. En la carpeta [`venv/bin`](venv/bin) ([venv/Scripts](./venv/Scripts) en Windows) están los scripts para cada tipo de terminal.

Por ejemplo, para powershell se ejecuta:

```bash
./venv/Scripts/Activate.ps1
```

Y en bash, zsh o similares:

```bash
source venv/bin/activate
```

Si se ha activado correctamente, en el terminal deberá salir el nombre del entorno:

```bash
(venv) Wikiuma$
```

El siguiente paso es instalar las dependencias, que se guardan por el gestor de paquetes [pip](https://pypi.org/project/pip/) en [requirements.txt](./requirements.txt).

Para instalar:

```bash
pip install -r ./requirements.txt
```

Si se añade una nueva dependencia, se deberá actualizar el archivo [requirements.txt](./requirements.txt).

```bash
pip freeze > requirements.txt
```

Este comando guarda la lista de dependencias con sus versiones del entorno virtual. **Usar con cuidado.**

## Ejecución

Para lanzar el servidor:

```bash
python ./manage.py runserver
```

Para crear un usuario administrador:

```bash
python ./manage.py migrate
python ./manage.py createsuperuser
```

Seguir las indicaciones del CLI.
