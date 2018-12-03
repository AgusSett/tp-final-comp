# Algoritmo de Fruchterman Reingold

### Dependencias

Para instalar las dependencias manualmente en caso de que el virtualenv no funcione:

```sh
$ pip install PyOpenGL
$ pip install PySDL2
$ apt-get install libsdl2-dev
```

### Ejecucion

Para ejecutarlo debemos hacer:

```sh
$ source bin/activate
$ python src/display2D.py # version 2D
$ python src/display3D.py # version 3D
```

### Controles

Click izquierdo y arrastra en los nodos para moverlos.
Click derecho y arrastra en cualquier parte para mover la cámara (solo en modo 3D).

### Linea de comandos

```sh
usage: display2D.py [-h] [-d] [-f FILE | -k K | -b A B]

optional arguments:
  -h, --help               show this help message and exit
  -d, --debug              modo debug
  -f FILE, --file FILE     carga el grafo desde un archivo
  -k K, --complete K       genera un grafo completo con K vertices
  -b A B, --bipartite A B  genera un grafo bipartito completo con A y B vertices cada componente
```
