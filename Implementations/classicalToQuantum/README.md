## classicalToQuantum

En este programa se realizo la implementacion sobre los diferentes experimentos sobre sistemas, como :
- Experimento del sistema determinista cuyo valor de las canicas son de tipo **Booleanos**
- Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
- Experimento de las múltiples rendijas cuántico.


de manera adicional, la libreria poseera una funcion que sera capaz de graficar con un diagrama de barras  las probabilidades de un vector de estados de un sistema.


## Empezando

Antes de empezar se debe tener en cuenta la forma en que los sistemas seran representados, cada sistema tendra una matriz de adyacencia asociada y un vector el cual representara el estado inicial del sistema, donde sus posiciones representaran el peso de  una  conexion especifica entre componentes del sistema, a continuacion se mostrar un ejemplo de un sistema deterministico.

## Sistema 
![image](https://user-images.githubusercontent.com/53798019/75600835-61b93f00-5a82-11ea-9b08-d9b01abfdc87.png)

## Matriz asociada al sistema
![image](https://user-images.githubusercontent.com/53798019/75600862-cbd1e400-5a82-11ea-9aba-1d3151e20887.png)

## Estado inicial del sistema 
![image](https://user-images.githubusercontent.com/53798019/75600871-e1dfa480-5a82-11ea-974d-5d833c298ba9.png)

## Representacion en la libreria
- Representacion de la matriz en la libreria corresponde a :
```
matrix = [   [ [0, 0], [0, 0] , [0, 0] ,[0, 0] ,[0, 0]    ],
             [  [0, 0], [0, 0] , [0, 0] ,[0, 0] ,[0, 0]  ],
	     [  [0, 0], [1, 0] , [0, 0] ,[0, 0] ,[1, 0]   ],
	     [  [0, 0], [0, 0] , [0, 0] ,[0, 0] ,[0, 0]  ],
	     [  [0, 0], [0, 0] , [1, 0] ,[0, 0] ,[0, 0] ],
	     [  [1, 0], [0, 0] , [0, 0] ,[1, 0] ,[0, 0]   ]]
```

- Representacion del vector en la libreria corresponde a :
```
vector = [ [6, 0],
 	   [2, 0],
	   [1, 0],
	   [5, 0] ,
	   [3, 0] ,
	   [10, 0]]
```

### Pre-requisitos

- Tener instalado una version mayor o igual a python 3
- Tener instalado las librerias numpy, scipy y matplotlib - python
- Es opcional tener instalado git 



### Instalando y ejecucion del programa

En caso de no tener instalado python o tener python 2.7 ,este  se podra descargar del siguiente link 
https://www.python.org/downloads/ .

En caso de no tener instalado git, este  se podra descargar del siguiente link 
https://git-scm.com/downloads.

En caso de no tener instalado numpy, scipy y matplotlib - python, seguir los pasos del siguiente video https://www.youtube.com/watch?v=oE4KeuVNqcQ&list=LLwZJu6f8CavefyakHGC1HEw





## Ejecutando Programa 

Para ejecutar el programa se deben seguir los siquientes pasos:

1) Descargar el repositorio en git usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/classicalToQuantum

```
3) ejecutar el archivo con el siguiente comando 

```
python classicalToQuantum.py
```

### Pruebas del programa 

Las pruebas en un programa son muy importantes, tanto es asi que estas permiten verificar que las funcionalidades del programa se cumplen en cada iteración correctamente.
Para este caso se usa la libreria de python  **unittest**; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es  importada con la linea de codigo **import unittest** que se encuentra en classicalToQuantumTest.py ,en este .py se encontraran  pruebas por cada una de las funciones implementadas sobre sistemas.

- **Primer prueba**: Prueba asociada al experimentos #1, la cual dada una matriz de elementos booleanos y un vector de estado inicial de un sistema deterministico, calcula el estado final que este se encontrara dado un numero de veces que este cambiara.

```
def testExperimentBooleanMatrix( self  ):
        booleanMatrix = [...]

        self.assertEqual(experimentBooleanMatrix( 1 ,booleanMatrix[:], vectIni[:]  ),
                         [False, True, True, False, False, False] )

        self.assertEqual(experimentBooleanMatrix( 3 ,booleanMatrix[:], vectIni[:]   ),
                         [False, False, False, False, True, False] )

        self.assertEqual(experimentBooleanMatrix( 5 ,booleanMatrix[:], vectIni[:]   ),
                         [False, True, False, False, False, False] )
```

- **Segunda prueba**: Prueba asociada al experimento #2, la cual dada una matriz de elementos que representa una probabilidad y un vector de estado inicial de un sistema probabilistico ( ** experimento de las multiples rendijas ** ), calcula el estado final que este se encontrara dado un numero de veces que este cambiara.

```
def testMultipleSlitQuantumExperiment( self ):
	matrix = [...]
	vectIni = [...]
        self.assertEqual( probabilisticSystem( matrix[:], vectIni[:], 1 ), [[0, 0], [0.33,0], [0.0,0]],
                                                                            [0.33, 0.0], [0.33,0], [0.0,0]],
                                                                            [0.0, 0.0], [0.0, 0.0],[0.0, 0.0], [0.0, 0.0]] )
```


- **Tercera prueba**:  Prueba asociada al experimento #3, la cual dada una matriz de elementos de numeros imaginarios y un vector de estado inicial de un sistema probabilistico cuantico  ( ** experimento de las multiples rendijas ** ), calcula el estado final que este se encontrara dado un numero de veces que este cambiara.

```
def testExperimentBooleanMatrix( self  ):
	matrix = [...]
	vectIni = [...]

        self.assertEqual(experimentBooleanMatrix( 1 ,booleanMatrix[:], vectIni[:]  ),
                         [False, True, True, False, False, False] )
```



- **Cuarta prueba**:   Prueba asociada a la funcion #4, la cual dado un vector de estado de un sistema probabilistico, logre graficar la probabilidad en cada uno de los estados.

```
def testGraphProbabilitiesVector( self ):
         graphProbabilitiesVector( [ [0,0] ,[0,0]  ,[0,0] ,
                                     [1/6,0],[1/6,0], [1/3,0],
                                     [1/6,0],[1/6,0] ]  )
```



## Ejecutando Pruebas

Para ejecutar las pruebas se deben seguir los siquientes pasos:

1) Descargar el repositorio en git hub usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/classicalToQuantum

```

3) ejecutar las pruebas  con el siguiente comando 

```
 python testClassicalToQuantum.py
```


## Autor

**Iván Camilo Rincón Saavedra** - *Latest Commmit* - [Rincon10](https://github.com/Rincon10)


## Referencias
El modelo que se siguio para diseñar el README	fue tomado del usuario:

[PurpleBooth](https://github.com/PurpleBooth)


