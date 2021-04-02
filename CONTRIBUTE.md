# Cómo contribuir
En GDUMA nos ❤️ las contribuciones: Comentarios, sugerencias, ideas, correcciones, traducciones, revisiones de código, diseño, 
la implementación de una nueva característica, entre otras contribuciones, todas son bienvenidas 🤓

## Contribuciones al repositorio
Como norma general trabajaremos sobre la rama master. A continuación se explica el proceso.
### Paso 1: [Fork](https://github.com/GDUMA/Wikiuma/fork)
Haz un [fork](https://github.com/GDUMA/Wikiuma/fork) del proyecto y clónalo localmente:
```
git clone https://github.com/username/Wikiuma.git
cd Wikiuma
git remote add upstream https://github.com/GDUMA/Wikiuma.git
git fetch upstream
```
Puedes encontrar más información en la [documentación de GitHub](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks).

### Paso 2: Nueva rama
Para mantener una organización, crea una rama localmente para realizar los cambios. La rama siempre se creará a partir de la rama _master_ original:

```
git checkout -b my-branch -t upstream/master
```

### Paso 3: Cambios y commit
Una vez creada la nueva rama ya puedes realizar los cambios y aplicarlos. Cuando estén listos, haz lo siguiente:
```
git add .
git commit -m "Mensaje descriptivo"
```
Los mensajes de commit deben empezar con mayúscula y no ser muy largos, por lo general de entre 50 y 70 caracteres.
Para evitar errores no usaremos tildes ni otros caracteres especiales en los mensajes. 
Deben explicar qué cambios se han hecho. Puedes hacer todos los commits que consideres necesarios.
>Con el comando `git status` y `git diff` puedes ver los cambios que se han realizado.

### Paso 4: Rebase
Se recomienda utilizar `git rebase` (no `git merge`) para sincronizar tu trabajo con el repositorio principal.

```
git fetch upstream
git rebase upstream/master
```

### Paso 5: Push y Pull Request
Cuando estén todos los cambios listos y hayas realizado las pruebas necesarias puedes subir los cambios a tu repositorio.
```
git push origin my-branch
```

Una vez subidos los cambios puedes realizar un pull request desde tu rama a la rama master del repositorio original.
Deberás indicar qué issue resuelve tu pull request rellenando la plantilla. Puedes referenciar issues en la descripción usando
el carácter almoadilla `#`.

### Paso 6: Revisión y cambios
En el nuevo pull request se comentarán las modificaciones y en caso de requerirlo se solicitarán nuevos cambios.
Para realizar nuevos cambios sobre el pull request simplemente hay que realizarlos en tu repositorio local repitiendo el paso 3:
```
git add .
git commit -m "Mensaje descriptivo"
git push origin my-branch
```
Los cambios se reflejarán automáticamente en el pull request.

En el caso de no entender qué o cómo realizar los cambios, siéntete libre de responder y preguntar, o de pedir ayuda para que otro u otra
te eche una mano.

### Paso 7: Merge
Antes de juntar los cambios al repositorio principal es necesario recibir la aprobación de al menos una persona del grupo.


Guías de referencia:
- [Working with issues and pull requests](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests).
- [Working with forks](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks).
- [Forking projects](https://guides.github.com/activities/forking/).
