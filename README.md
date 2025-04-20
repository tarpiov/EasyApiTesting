# Tutorial de  uso

Para usar este script lo primero que debemos hacer es instalar las dependencias, podemos hacerlo con el comando `pip install -r requirements.txt` o también con el archivo `setup.py` de esta manera:

```sh
# LINUX
$ python3 setup.py

# WINDOWS
$ python setup.py
```

> Este archivo ejecuta el comando de instalar los `requirements.txt` por vosotros.

Luego de esto, ejecutaremos el `main.py`

```sh
# LINUX
$ python3 main.py

# WINDOWS
$ python main.py
```

El programa nos pedirá una url de una API, deberéis pasarle la url donde comienzan los endpoints, no debéis pasarle directamente un endpoint ni nada diferente, ejemplo: 

```sh
> https://api.testing.io/api/
```

> Automáticamente el programa empezará a buscar rutas y os las reportará por pantalla cuando sean efectivas

