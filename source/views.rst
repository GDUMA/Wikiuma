Creación de vistas
===================

Cada app contiene el archivo ``views.py`` y una carpeta llamada ``templates``.

Dentro de ``templates`` se encuentran los archivos `html` con la estructura de la página.

Dentro de ``<app>/views.py`` se definen las vistas en forma de funciones. Por ejemplo:

.. code-block:: python

	from datetime import datetime

	def date_view(request):
		context = {
			'date': datetime.now()
		}
		return render(request, 'index.html', context)


Esta vista devolvería la plantilla ``index.html`` con la variable ``context``, la cual en este caso tiene la fecha y la hora actual.

Esa variable es un diccionario, el cual se puede acceder desde el archivo ``html`` mediante ``{{ date }}``.

.. code-block:: html

	<body>
	<p>El dia es {{date}}</p>
	</body>

Para terminar de configurar la vista, en los archivos de configuración globales, concretamente en ``Wikiuma/urls.py``, se deberá definir la ruta a la que responde esta vista. En el caso de ejemplo se quiere que responda a la raíz o ``/``. En este caso haría falta añadir:

.. code-block:: python

	from WikiumaApp.views import home_view

	urlpatterns = [
		path('admin/', admin.site.urls),
		path('', home_view)
	]


En este caso se importa la vista, y se le asigna a la ruta ``''`` la vista ``home_view`` que se definió antes.
