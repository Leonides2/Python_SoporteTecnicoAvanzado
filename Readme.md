# Propósito

Este repositorio fue creado con el fin de compartir el funcionamiento interno de
la programación incluida de un proyecto de robótica de un curso de soporte
técnico en la Universidad Nacional de Costa Rica.

## Requisitos para ejecutar el script

Para instalar librerias:

- Pip

Para ejecutar el script necesitas las siguientes librerías de python:

- evdev
- pybluez

Comando para instalar:

``` bash
python -m pip install [libreria]
```

Todas las instrucciones se encuentran explicadas con bash, debido a que
el proyecto fue realizado en un equipo linux. Sin embargo, con la correcta
configuración deberia de funcionar en Windows o MacOS

## Errores comunes (Linux)

Si al tratar de instalar un paquete, no encuentra, pip, puede ser que la instalación
de python que posees haya eliminado el modulo pip. Puedes tratar de instalar el modulo
usando el modulo integrado (si no se encuentra removido) de `ensurepip` de la siguiente forma

```bash
python -m ensurepip
```

Si esto no funciona, puedes hacer uso del script de python que se provee oficialmente para instalar
pip

El script se encuentra en [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py),
o si deseas observarlo directamente de la documentación de python, la página es la siguiente:

[https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

Ahora deberías de poder instalar las dependecias sin ningún problema.

Este repositorio incluye una versión del script `get-pip.py`, sin embargo puede que no sea la más
actualizada al momento de lectura de este README

Si sigue sin funcionar, puedes utilizar el gestor de paquetes de tu distro para instalar
pip
