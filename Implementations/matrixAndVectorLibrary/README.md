## matrixAndVectorLibrary

En este programa se realizo la implementacion de operaciones para vectores y matrices  complejas, la cual es capaz de realizar las siguientes operaciones:

- Adición de vectores complejos.
- Inverso (aditivo) de un vector complejo.
- Multiplicación de un escalar por un vector complejo.
- Adición de matrices complejas.
- Inversa (aditiva) de una matriz compleja.
- Multiplicación de un escalar por una matriz compleja.
- Transpuesta de una matriz/vector
- Conjugada de una matriz/vector
- Adjunta (daga) de una matriz/vector
- Producto de dos matrices (de tamaños compatibles)
- Función para calcular la "acción" de una matriz sobre un vector.
- Producto interno de dos vectores
- Norma de un vector
- Distancia entre dos vectores
- Revisar si una matriz es unitaria
- Revisar si una matriz es Hermitiana
- Producto tensor de dos matrices/vectores


## Empezando

Antes de empezar se debe tener en cuenta la forma en que los numeros complejos seran representados, vectores complejos, matrices complejas .

**Numeros Complejos**
Como se sabe los numeros complejos se caracterizan por tener una parte real y una imaginaria como se observa en el siguiente ejemplo: 

```
1 + 2i
```
lo equivalente para la libreria sera una lista de longitud 2, cuya posicion 0 sera la parte real y la posicion 1 la parte imaginaria; con respecto al numero anterior el equivalente en la libreria  sera:

```
[ 1, 2]
```

**Vectores complejos**
El ejemplo principal de un espacio vectorial complejo es el conjunto de vectores de longitud fija con entradas complejas.

por ejemplo El conjunto de vectores de longitud 2 lo denominaremos como C2 =C×C, lo que nos recuerda que cada vector es una lista ordenada de 2 números complejos.

**Ejemplo de un vector en c2:**
```
 | 5 + 3i |
 | 3 + 6i |
```
lo equivalente para la libreria sera una lista de longitud de la dimension de c, cuya cada posicion sera un numero imaginario; con respecto al numero anterior el equivalente en la libreria  sera:
```
[ [ 5,3 ], [ 3, 6] ]
```

**Matrices  complejas**
 Las matrices compleajas se pueden ver como C m×n, el conjunto de todas las matrices m-por-n **(matrices bidimensionales)** con entradas complejas, es un espacio vectorial complejo


**Ejemplo de una matriz en c 2x2:**
```
 | 5 + 3i   8 + 9i |
 | 3 + 6i   3 - i  |
```
lo equivalente para la libreria sera una matriz, cuya cada posicion sera una lista de numeros imaginario; con respecto al numero anterior el equivalente en la libreria  sera:
```
[ [ [ 5,3 ], [ 8, 9 ] ], [ [ 3, 6], [3,- 1 ] ] ]
```

### Pre-requisitos

-Tener instalado una version mayor o igual a python 3
-Es opcional tener instalado git 


### Instalando y ejecucion del programa

En caso de no tener instalado python o tener python 2.7 ,este  se podra descargar del siguiente link 
https://www.python.org/downloads/ .

En caso de no tener instalado git, este  se podra descargar del siguiente link 
https://git-scm.com/downloads.





## Ejecutando Programa 

Para ejecutar el programa se deben seguir los siquientes pasos:

1) Descargar el repositorio en git usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/matrixAndVectorLibrary

```
3) ejecutar el archivo con el siguiente comando 

```
python matrixAndVectorLibrary.py
```

### Pruebas del programa 

Las pruebas en un programa son muy importantes, tanto es asi que estas permiten verificar que las funcionalidades del programa se cumplen en cada iteración correctamente.

Para este caso se usa la libreria de python  **unittest**; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es  importada con la linea de codigo **import unittest** que se encuentra en testMatrixandVector.py .

En este .py se encontraran 2 pruebas por cada una de las funciones implementadas de operaciones para vectores y matrices complejas.

A continuacion se mostrara un ejemplo de una prueba de la funcion suma la cual nos dice si el resultado de la suma entre los vectores a y b es igual a [ [ 2, 6 ], [ 4, 8 ] ] ,  de forma analoga sera para las demas funciones:

```
def testSumVect(self):
       
        self.assertEqual( sumVect( [ a, b ], [a ,b ] ),
                          [[2, 6], [4, 8]] )
```




## Ejecutando Pruebas

Para ejecutar las pruebas se deben seguir los siquientes pasos:

1) Descargar el repositorio en git hub usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/matrixAndVectorLibrary

```

3) ejecutar las pruebas  con el siguiente comando 

```
 python testMatrixandVector.py
```


## Autor

**Iván Camilo Rincón Saavedra** - *Latest Commmit* - [Rincon10](https://github.com/Rincon10)


## Referencias
El modelo que se siguio para diseñar el readme fue tomado del usuario:

[PurpleBooth](https://github.com/PurpleBooth)


