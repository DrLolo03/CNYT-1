
# complexNumberLibrary

En este programa se realizo la implementacion de una libreria sobre numeros complejos, la cual es capaz de calcular:

- Suma 
- Producto
- Resta
- División
- Módulo
- Conjugado
- Conversión entre representaciones polar y cartesiano
- Retornar la fase de un número complejo.

## Empezando

Antes de empezar se debe tener en cuenta la forma en que los numeros complejos seran representados, como se sabe los numeros complejos se caracterizan por tener una parte real y una imaginaria como se observa en el siguiente ejemplo: 

```
1 + 2i
```
lo equivalente para la libreria sera una lista de longitud 2, cuya posicion 0 sera la parte real y la posicion 1 la parte imaginaria; con respecto al numero anterior el equivalente en la libreria  sera:

```
[ 1, 2]
```

### Lenguaje
El lenguaje en el que se desarrollo la libreria es

- python 3


### Pre-requisitos

-Tener instalado una version mayor o igual a python 3
-Es opcional tener instalado git 


### Instalando y ejecucion del programa

En caso de no tener instalado python o tener python 2.7 ,este  se podra descargar del siguiente link https://www.python.org/downloads/ .

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
cd Implementations/complexNumberLibrary

```
3) ejecutar el archivo con el siguiente comando 

```
python complexNumberLibrary.py
```

### Pruebas del programa 

Las pruebas en un programa son muy importantes, tanto es asi que estas permiten verificar que las funcionalidades del programa se cumplen en cada iteración correctamente.

Para este caso se usa la libreria de python  **unittest**; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es  importada con la linea de codigo **import unittest** que se encuentra en testComplexNumber.py .

En este .py se encontraran 3 pruebas por cada una de las funciones implementadas de numeros complejos.

A continuacion se mostrara un ejemplo de una prueba de la funcion suma la cual nos dice si el resultado de la suma entre los numeros complejos a y b es igual a [ 4, 3  ] ,  de forma analoga sera para las demas funciones:

```
def testSuma(self):
        a, b = [ 3, -1 ],  [ 1, 4 ]
        
        self.assertEqual( suma( a, b ), [ 4, 3  ] )
```




## Ejecutando Pruebas

Para ejecutar las pruebas se deben seguir los siquientes pasos:

1) Descargar el repositorio en git hub usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd /Implementations/complexNumberLibrary

```

3) ejecutar las pruebas  con el siguiente comando 

```
 python testComplexNumber.py
```


## Autor

**Iván Camilo Rincón Saavedra** - *Latest Commmit* - [Rincon10](https://github.com/Rincon10)


## Referencias
El modelo que se siguio para diseñar el readme fue tomado del usuario:

[PurpleBooth](https://github.com/PurpleBooth)

