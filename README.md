<h1>Curso de Python</h1>
<h4>Índice</h4>
<ol>
	<li><b><a href="#dia1">Día 1</a></b></li>
	<ul>
		<li><a href="#ej1">Soluciones ejercicios 1</a></li>
	</ul>
	<li><b><a href="#dia2">Día 2</a></b></li>
	<ul>
		<li><a href="#ej2">Soluciones ejercicios 2</a></li>
		<li><a href="#ej3">Soluciones ejercicios 3</a></li>
	</ul>
	<li><b><a href="#dia3">Día 3</a></b></li>
	<ul>
		<li><a href="#ej4">Soluciones ejercicios 4</a></li>
		<li><a href="#ej5">Soluciones ejercicios 5</a></li>
	</ul>
	<li><b><a href="#dia4">Día 4</a></b></li>
	<ul>
		<li><a href="#ej6">Soluciones ejercicios 6</a></li>
		<li><a href="#ej7">Soluciones ejercicios 7</a></li>
	</ul>
</ol>
<h4>Contenido</h4>
<ol>
	<li><b><a name="dia1">Día 1</a></b></li>
	<ul>
		<li><h3><a name="ej1">Soluciones ejercicios 1</a></h3></li>
	</ul>
	<h4>Ejercicio 1: potencias de 2</h4>
	<p>Escribe un sencillo programa en Python, llamado ejercicio1.py, que muestre las siguientes potencias de 2, una por línea:</p>
	<pre>21, 22, 23, 24, 25, 26, 27, 28</pre>
	<h4>Ejercicio 2: potencia de 2 elevado a un número</h4>
	<p>Escribe un programa en Python, ejercicio2.py, que solicite al usuario cualquier valor entero, y muestre el valor de 2 elevado a esa potencia. El programa debería funcionar como se muestra en el siguiente ejemplo:</p><pre>¿Qué potencia de 2?: 10
	2 elevado a la potencia 10 es 1024</pre>
	<h4>Ejercicio 3: potenciación</h4>
	<p>Escribe un programa de Python, llamado ejercicio3.py, que permita al usuario introducir una base entera y un exponente entero, y que muestre el valor de la base elevada a ese exponente. El programa debe funcionar como se muestra a continuación.</p>
	<pre>¿Qué base?: 10
¿Qué potencia de 10?: 4
10 elevado a la potencia 4 es 10000</pre>
	<h4>Ejercicio 4: conversión de binario a base 10</h4>
	<p>Escribe un programa Python, llamado ejercicio4.py, que permita al usuario introducir un número binario de cuatro dígitos y mostrar el valor en la base 10. Debe introducirse un dígito binario por línea, comenzando con el dígito más a la izquierda, como se muestra a continuación.</p>
	<pre>Escribe el dígito más a la izquierda: 0
Escribe el siguiente dígito: 1
Escribe el siguiente dígito: 0
Escribe el siguiente dígito: 1
El valor binario 0101 es 5 en base 10</pre>
	<h4>Ejercicio 5: Número de rutas</h4>
	<p>Escribe un programa de Python, llamado ejercicio5.py, que pida al usuario un cierto número de ciudades para el problema del viajante y que muestre el número total de rutas posibles que se pueden tomar. El programa debe funcionar como se muestra a continuación:</p>
	<pre>¿Cuántas ciudades? 10
Para 10 ciudades, hay 3628800 rutas posibles</pre>
	<h4>Ejercicio 6. Estimación del número de años para resolver el problema del Viajante</h4>
	<p>Desarrolla y prueba un programa de Python, llamado ejercicio6.py, que solicite al usuario un valor entero que indique el número de ciudades a resolver para el problema del viajante. El programa debe entonces mostrar el número de años que se necesitaría para resolver el problema usando un enfoque de fuerza bruta. Utiliza la función factorial del módulo math como se muestra en la figura 28. Supongamos que un ordenador puede calcular la longitud de un millón de rutas por segundo. A continuación se muestra una posible salida del programa:</p>
	<pre>Escribe el número de ciudades: 20
Número de rutas:  2432902008176640000
Número de rutas por año: 31536000000000
El tiempo necesario para resolver el problema del viajante
para 20 ciudades es aproximadamente de 77146.81659616438 años.</pre>
	<h4>Ejercicio 7. Estimación del número de años para todas las jugadas del ajedrez</h4>
	<p>Desarrolla y prueba un programa de Python, llamado ejercicio7.py, que determine cuántos años se necesitarían para que se jugaran todas las posibles partidas de ajedrez, si cada habitante de la Tierra (independientemente de su edad) jugara una partida de ajedrez al día. Datos aproximados:</p>
	<ul>
		<li>La población mundial actual es de 7500 millones.</li>
		<li>Hay 10<sup>120</sup> posibles partidas de ajedrez.</li>
	</ul>
	<pre>El número de años necesarios para jugar todas las partidas de ajedrez posibles
si cada humano juega una sola partida al día, es de 3.6529680365296805e+107</pre>
	<li><b><a name="dia2">Día 2</a></b></li>
	<ul>
		<li><a name="ej2">Soluciones ejercicios 2</a></li>
		<div id="content-main">
<!-- InstanceBeginEditable name="Cuerpo" -->
  <h4>Ejercicio 1 &mdash; división de enteros</h4>
  <p>Escribe un programa en Python (<em>ejercicio2.1.py</em>) que solicite al usuario dos valores enteros y que muestre el resultado del primer número dividido por el segundo, con exactamente dos decimales. El programa debería funcionar como se muestra en el siguiente ejemplo:</p>
  
<div class="codigo"><pre>Escribe el primer número entero: <strong>34</strong>
Escribe el segundo número entero: <strong>27</strong>
El cociente es:  1.26</pre></div>

<h4>Ejercicio 2 &mdash; División de números reales (I)</h4>
<p>Escribe un programa en Python (<em>ejercicio2.2.py</em>) que solicite al usuario dos valores reales (en punto flotante) y que muestre el resultado del primer número dividido por el segundo, con exactamente seis posiciones decimales. El programa debería funcionar como se muestra en el siguiente ejemplo:</p>

<div class="codigo"><pre>
Escribe el primer número real: <strong>23.5</strong>
Escribe el segundo número real: <strong>4.6</strong>
El cociente es: 5.108696</pre></div>

<h4>Ejercicio 3 &mdash; División de números reales (II)</h4>
<p> Escribe un programa en Python (<em>ejercicio2.3.py</em>) que pida al usuario dos valores reales (punto flotante) y que muestre el resultado del primer número dividido por el segundo, con exactamente seis posiciones decimales mostradas en notación científica. El programa debería funcionar como se muestra en el siguiente ejemplo:</p>
<div class="codigo">
<pre>
Escribe el primer número real: <strong>23.5</strong>
Escribe el segundo número real: <strong>4.6</strong>
El cociente es: 5.108696e+00</pre>
</div>

<h4>Ejercicio 2.4 &mdash; Letra en Unicode</h4>
  <p>Escribe un programa de Python (<em>ejercicio2.4.py</em>) que pida al usuario que introduzca una letra mayúscula o minúscula y muestre la codificación Unicode correspondiente. El programa debería funcionar como se muestra en el siguiente ejemplo:</p>
  <div class="codigo">
    <pre>
Escribe una letra (mayúscula o minúscula): <strong>g</strong>
El Unicode de la letra g es: 103</pre>
</div>
  
<h4>Ejercicio 2.5 &mdash; Operaciones aritméticas</h4>
<p> Escribe un programa de Python (<em>ejercicio2.5.py</em>) que permita al usuario introducir dos valores enteros y mostrar los resultados cuando se les aplican  los siguientes operadores aritméticos. Por ejemplo, si el usuario introduce los valores 7 y 5, la salida sería,<br>
</p>
<table class="tb-formula">
<tr><td>
<div>
<pre>7 + 5 = 12
7 – 5 = 2
7 * 5 = 35
7 / 5 = 1.40
7 // 5 = 1
7 % 5 = 2
7 ** 5 = 16,807</pre></div>
</td></tr></table>

<p>Todos los resultados de coma flotante deben mostrarse con dos decimales de precisión. Además, todos los valores deben mostrarse con comas, cuando corresponda.</p>
<h4>Ejercicio 6. Perder la cabeza por el ajedrez</h4>
<p>Cuenta la leyenda que hace mucho tiempo reinaba en cierta parte de la India un rey llamado Sheram. En una de las batallas en las que participó su ejército perdió a su hijo, y eso le dejó profundamente consternado. Nada de lo que le ofrecían sus súbditos lograba alegrarle.</p>
<p>Un buen día un tal Sissa se presentó en su corte y pidió audiencia. El rey la aceptó y Sissa le presentó un juego que, aseguró, conseguiría divertirle y alegrarle de nuevo: el ajedrez. Después de explicarle las reglas y entregarle un tablero con sus piezas el rey comenzó a jugar y se sintió maravillado: jugó y jugó y su pena desapareció en gran parte. Sissa lo había conseguido. Sheram, agradecido por tan preciado regalo, le dijo a Sissa que como recompensa pidiera lo que deseara.</p>
<p>   Sissa, inteligente, pidió un grano de trigo en el primer cuadrado, dos granos de trigo en el segundo cuadrado, cuatro granos de trigo en el tercer cuadrado, y así sucesivamente, duplicando la cantidad en cada cuadrado siguiente. El rey pensó que esto era una recompensa modesta para tal invención. Sin embargo, la cantidad total de trigo habría sido más de 1.000 veces la producción mundial actual. Cuando el rey se dio cuenta de que no podía cumplir su promesa, hizo que cortaran la cabeza a Sissa.</p>

<p>Desarrolla y prueba un programa de Python que muestre el número de granos en cada fila (con comas como separadores de miles), el número de granos en total, y el peso total de todo el trigo en kilogramos, utilizando el hecho de que un grano de trigo pesa aproximadamente 0.04 gramos. El programa debería funcionar como se muestra en el siguiente ejemplo:</p>

<table class="tb-formula">
<tr><td>
<div>
<pre>
Granos en fila 1:                            255
Granos en fila 2:                         65,280
Granos en fila 3:                     16,711,680
Granos en fila 4:                  4,278,190,080
Granos en fila 5:              1,095,216,660,480
Granos en fila 6:            280,375,465,082,880
Granos en fila 7:         71,776,119,061,217,280
Granos en fila 8:     18,374,686,479,671,623,680
  Granos totales:     18,446,744,073,709,551,615
Peso total del trigo: 737869762948382.12 kilogramos
Peso total del trigo: 7.378698e+14 kilogramos</pre></div>
</td></tr></table>

<h4>Ejercicio 7</h4>
<p>Desarrolla y prueba un programa de Python (<em>ejercicio2.7</em>) que determine cuánto tiempo se tendría que emplear  para descargar todas las palabras que se han hablado alguna vez. Toma como el tamaño de esta información 5x10<sup>18</sup> (5 HB, el que se  muestra en la figura 1 del tema <a href="../py78_Cap2.html">Datos y Expresiones</a>). Supongamos que cada palabra está codificada con 8 bits. </p>
<p>La velocidad de descarga debe ser introducida por el usuario en millones de bits por segundo (1 <em>Mbps</em> = 1000000 bits por segundo). Para encontrar la velocidad de conexión real, utiliza este sitio web u otro similar,</p>
<p style="text-align:center"><a href="http://beta.speedtest.net/es">http://beta.speedtest.net/es</a></p>
<p>  Dado que las velocidades de conexión pueden variar, ejecuta esta prueba de velocidad de conexión tres veces. Toma el promedio de tres resultados, y utilízalo como la velocidad de conexión para entrar en su programa. Finalmente, determina cuál es la unidad de tiempo apropiada para expresar los resultados del programa (¿minutos?, ¿horas?, ¿días?, ...). El programa debería funcionar como se muestra en el siguiente ejemplo:</p>

<table class="tb-formula">
<tr><td>
<div>
<pre>¿Velocidad de descarga (en Mbps)?: 96.25
Años:  1.317810e+10 ( 13,178,095,369 )</pre></div>
</td></tr></table>
<!-- InstanceEndEditable --><!-- End the content-main division -->
</div>

		<li><a name="ej3">Soluciones ejercicios 3</a></li>
		<div id="content-main">
<!-- InstanceBeginEditable name="Cuerpo" -->
 
  <h4>Ejercicio 1 &mdash; Frutas (I)</h4>
  <p>Escribe un programa Python (<em>ejercicio3.1.py</em>) en el que el usuario introduzca <code>'A'</code>, <code>'B'</code> o <code>'C'</code>. Si se introduce <code>'A'</code>, el programa debe mostrar:</p>
  <ul>
    <li> la palabra <code>'Aguacate'</code> si se introduce 'A' o <code>'a'</code>; </li>
    <li>la palabra <code>'Banana'</code> si se introduce <code>'B'</code> o <code>'b'</code>; y</li>
    <li>la palabra  <code>'Ciruela'</code> si se introduce <code>'C'</code> o <code>'c'</code>. </li>
  </ul>
  <p>Utiliza las sentencias <code>if</code> anidadas en este ejercicio (ver figura 13 del documento <a href="../py78_Cap3.html">Estructuras de Control</a>).</p>

<h4>Ejercicio 2 &mdash; Frutas (II)</h4>
  <p>Repite el ejercicio 1 utilizando una instrucción if con  cabeceras <code>elif</code>. El archivo se debe llamar <em>ejercicio3.2.py</em>.</p>

<h4>Ejercicio 3 &mdash; Créditos Universitarios</h4>
<p>Escribe un programa de Python (<em>ejercicio3.3.py</em>) en el que un estudiante ingrese el número de créditos universitarios obtenidos. Si el número de créditos es <strong>mayor o igual a</strong> 90, se muestra <code>'Senior'</code>; si <strong>es mayor o igual a</strong> 60, se muestra <code>'Junior'</code>; si es mayor que o igual a 30, se muestra <code>'Segundo curso'</code>; de lo contrario, se mostrará <code>'Primer curso'</code>.</p>

<h4>Ejercicio 4 &mdash; Suma de números</h4>
<p>Escribe un programa en Python (<em>ejercicio3.4.py</em>) que sume una serie de enteros (positivos) introducidos por el usuario, excluyendo todos los números que sean <strong>mayores que</strong> 100. El programa finaliza cuando el usuario introduce un número negativo.</p>
  
<h4>Ejercicio 5 &mdash; Cuenta números </h4>
  <p>Escribe un programa en Python (<em>ejercicio3.5.py</em>), en el que el usuario puede introducir cualquier número de valores enteros positivos y negativos, y que muestre el número total de  valores positivos introducidos, así como el número total de valores negativos. El programa finaliza cuando el usuario introduce <code>'f'</code>.</p>

<h4>Ejercicio 6 &mdash; Tabla de 100 números (I)</h4>
<p>Escribe un programa en Python (<em>ejercicio3.6.py</em>) que debe contener un par de bucles <code>while</code> anidados, y que muestre los valores enteros del intervalo [1, 100], diez números por fila, con las columnas alineadas como se muestra a continuación:</p>

<table class="tb-formula">
  <tr><td>
<div>
<pre>
   1   2   3   4   5   6   7   8   9  10
  11  12  13  14  15  16  17  18  19  20
  21  22  23  24  25  26  27  28  29  30
  31  32  33  34  35  36  37  38  39  40
  41  42  43  44  45  46  47  48  49  50
  51  52  53  54  55  56  57  58  59  60
  61  62  63  64  65  66  67  68  69  70
  71  72  73  74  75  76  77  78  79  80
  81  82  83  84  85  86  87  88  89  90
  91  92  93  94  95  96  97  98  99 100</pre></div>
</td></tr></table>

<h4>Ejercicio 7 &mdash; Tabla de 100 números (I)</h4>
  Escribe un programa en Python (<em>ejercicio3.7.py</em>) que muestre los valores enteros del intervalo [1, 100] utilizando solamente un bucle <code>while</code>.<br>
  </p>
  <h4>Ejercicio 8 &mdash; El primer crédito</h4>
  <p>    Desarrolla y prueba  un programa de Python (<em>ejercicio3.8.py</em>) que determine si un individuo cumple los requisitos  para obtener un crédito de 8000 euros para comprar su primera  vivienda. Los requisitos del crédito son:</p>
  <ul>
    <li> el precio de la vivienda es menor de 800,000€;</li>
    <li> los ingresos del solicitante no deben superar los  225,000€; y </li>
    <li>el solicitante  no ha poseído una residencia principal en los últimos tres años.</li>
</ul>

  <h5>&sect;&nbsp;Ejemplos:</h5>
  <div class="codigo"><pre>Este programa determina si una persona cumple los requisitos para
obtener un crédito de 8000 euros

Escriba precio de compra: 1000000

El precio de compra está limitado a 800000 €.
En consecuencia, se deniega el crédito.
</pre></div>

<div class="codigo"><pre>
Este programa determina si una persona cumple los requisitos para
obtener un crédito de 8000 euros

Escriba precio de compra: 180000
Escriba ingresos totales: 250000

Sus ingresos exceden el máximo permitido de 225000 €.
En consecuencia, se deniega el crédito.</pre></div>

<div class="codigo"><pre>Este programa determina si una persona cumple los requisitos para
obtener un crédito de 8000 euros

Escriba precio de compra: 180000
Escriba ingresos totales: 20000
¿Ha sido propietario de alguna vivienda anteriormente (s/n)? :n

¡ENHORABUENA!
En base a la información proporcionada, ha conseguido Vd. el crédito solicitado.</pre></div>

<div class="codigo"><pre>
Este programa determina si una persona cumple los requisitos para
obtener un crédito de 8000 euros

Escriba precio de compra: 180000
Escriba ingresos totales: 20000
¿Ha sido propietario de alguna vivienda anteriormente (s/n)? :s
¿Hace cuantos años que fue propietario de una vivienda?: 2

No cumple los requisitos del crédito, ya que Vd. ha sido propietario de una 
vivienda en los 3 últimos años.</pre></div>

<div class="codigo"><pre>
Este programa determina si una persona cumple los requisitos para
obtener un crédito de 8000 euros

Escriba precio de compra: 180000
Escriba ingresos totales: 20000
¿Ha sido propietario de alguna vivienda anteriormente (s/n)? :s
¿Hace cuantos años que fue propietario de una vivienda?: 6

¡ENHORABUENA!
En base a la información proporcionada, ha conseguido Vd. el crédito solicitado.</pre>
<!-- InstanceEndEditable --><!-- End the content-main division -->

</div>

	</ul>
	<li><b><a name="dia3">Día 3</a></b></li>
	<ul>
		<li><a name="ej4">Soluciones ejercicios 4</a></li>
		<div id="content-main">
<!-- InstanceBeginEditable name="Cuerpo" -->
 
  <h4>Ejercicio 1 &mdash; Lista de números (I)</h4>
  <p>Escribe un programa Python (<em>ejercicio4.1.py</em>) que solicite al usuario una lista de números enteros, que  almacene en una lista solamente los valores entre 1 y 100, y que muestre la lista resultante. La secuencia finaliza cuando el usuario pulsa &lt;return&gt; sin escribir ningún número.</p>
  <h4>Ejercicio 2 &mdash; Lista de números  (II)</h4>
  <p>Escribe un programa Python (<em>ejercicio4.2.py</em>) que solicite al usuario una lista de números enteros, que  almacene en una lista solamente los valores que están en una tupla denominada valores_validos, y que muestre la lista resultante. La secuencia finaliza cuando el usuario pulsa &lt;return&gt; sin escribir ningún número.</p>
  <h4>Ejercicio 3 &mdash; Lista de números (III)</h4>
<p>Escribe un programa Python (<em>ejercicio4.3.py</em>) que solicite al usuario una lista de números enteros, y los almacene en una lista. Para todos los valores mayores que 100, se debe almacenar la cadena 'pasa' en lugar del número. El programa finaliza mostrando la lista resultante. La secuencia finaliza cuando el usuario pulsa &lt;return&gt; sin escribir ningún número.</p>
<h4>Ejercicio 4 &mdash; Lista de nombres (I)</h4>
<p>Escribe un programa en Python (<em>ejercicio4.4.py</em>) que solicite al usuario una lista de nombres y que los almacene en una lista. El programa debe mostrar cuantas veces aparee la letra 'a' en la lista generada. La secuencia finaliza cuando el usuario pulsa &lt;return&gt; sin escribir nada.</p>
  
<h4>Ejercicio 5 &mdash; Lista de nombres (II) </h4>
  <p>Escribe un programa en Python (<em>ejercicio4.5.py</em>) que solicite al usuario una lista de nombres y que  almacene en una lista solamente aquellos nombres cuya primera letra se encuentre también dentro de la palabra (por ejemplo, <code>'Ana'</code>). El programa debe mostrar cuántas veces aparee la letra 'a' en la lista generada. La secuencia finaliza cuando el usuario pulsa &lt;return&gt; sin escribir nada.</p>
  <h4>Ejercicio 6 &mdash; Lista ordenada de frutas</h4>
<p>Escribe un programa en Python (<em>ejercicio4.6.py</em>) que pida al usuario que introduzca tipos de fruta, y cuantos kilos hay de cada tipo. Los datos introducidos se deben almacenar en una lista en la que cada elemento es una sublista con el tipo de fruta y su peso. El programa debe mostrar la lista ordenada por el tipo de fruta, en la forma <code>fruta</code>, <code>peso</code>, y con un tipo de fruta en cada línea, como se muestra en el siguiente ejemplo:</p>

<table class="tb-formula">
  <tr><td>
<div>
<pre>Tipo      Peso
Manzanas   6 kgs.
Peras     11 kgs.
...</pre></div>
</td></tr></table>

<h4>Ejercicio 7 &mdash; Dos listas de números</h4>
  Escribe un programa en Python (<em>ejercicio3.7.py</em>) que solicite al usuario números enteros para crear dos listas. El programa debe mostrar si las listas tienen la misma longitud (mismo número de elemento), si los números de cada lista suman el mismo valor, y si ambas listas comparten valores comunes.
 
<!-- InstanceEndEditable --><!-- End the content-main division -->

</div>
		<li><a name="ej5">Soluciones ejercicios 5</a></li>
		<div id="content-main">
<!-- InstanceBeginEditable name="Cuerpo" -->
 
  <h4>Ejercicio 1</h4>
  <p>Escribe un programa Python (<em>ejercicio5.1.py</em>) con una función llamada <code>buscaCero()</code> a la que se le pasan tres enteros, y devuelve <code>True</code> si alguno de los enteros 0, y <code>False</code> en caso contrario.</p>
  <h4>Ejercicio 2</h4>
  <p>Escribe un programa Python (<em>ejercicio5.2.py</em>) con una función llamada ordenados(), a la que se le pasan 3 enteros, y devuelve <code>True</code> si los tres enteros están en orden creciente; en cualquier otro caso devuelve <code>False</code>.</p>
  <h4>Ejercicio 3</h4>
<p>Escribe un programa Python (<em>ejercicio5.3.py</em>) con una función llamada  <code>modCount</code> a la que se le pasa un entero positivo, <code>n</code>, and un segundo entero positivo, <code>m</code>, tal que <code>m &lt;= n</code>, y devuelve cuántos números del intervalo entre 1 y <code>n</code> son divisibles por <code>m</code>.</p>
<h4>Ejercicio 4 &mdash; Hola Mundo</h4>
<p>Escribe un programa en Python (<em>ejercicio5.4.py</em>)  con una función llamada <code>HolaMundo()</code> que muestre el mensaje &quot;Hola mundo, mi nombre es <em>nombre</em>&quot;, para cualquier nombre que se le pase a dicha función.</p>
  
<h4>Ejercicio 5</h4>
<p>Escribe un programa en Python (<em>ejercicio5.5.py</em>) con una función llamada  <code>printAsteriscos()</code>, a la que se le pasa un entero positivo, <code>n</code>, e imprime en pantalla una línea de <code>n</code> asteriscos. Si n es mayor que 75, solamente muestra  75 asteriscos.</p>
<h4>Ejercicio 6</h4>
  <p>Escribe un programa en Python (<em>ejercicio5.6.py</em>) con una función llamada  <code>getContinue()</code> que muestra al usuario el mensaje “<em>¿Quiere continuar (s/n):</em> ”,; el mensaje se repetirá hasta que el usuario teclee <code>'s'</code> o <code>'n'</code> (tanto mayúsculas como minúsculas), y que devuelva  's' o <code>'n'</code> en minúsculas.</p>
  <h4>Ejercicio 7</h4>
  <p>Escribe un programa en Python (<em>ejercicio5.7.py</em>) con una función llamada umbral(), a la que se le pasa una lista de números y un valor umbral, y devuelve la lista con todos los valores inferiores al umbral con valor 0. La lista debe ser modificada como efecto lateralde la función, y no a través del valor de retorno.</p>
  <h4>Ejercicio 8</h4>
  <p>Implementa la función umbral() del ejercicio  7 de forma que la lista modificada sea el valor de retorno de la función, en lugar de hacerlo como efecto lateral. (ejercicio5.8.py).</p>
  <p>&nbsp;</p>
  <p>&nbsp;</p>
<!-- InstanceEndEditable --><!-- End the content-main division -->

</div>
	</ul>
	<li><b><a name="dia4">Día 4</a></b></li>
	<ul>
		<li><a name="ej6">Soluciones ejercicios 6</a></li>
		<div id="content-main">
<!-- InstanceBeginEditable name="Cuerpo" -->
 
  <h4>Ejercicio 1</h4>
  <p>Escribe un programa Python (<em>ejercicio6.1.py</em>) con  un conjunto de instrucciones para controlar a la tortuga que dibuje una línea desde la esquina superior izquierda de la pantalla hasta la esquina inferior derecha, y desde la esquina superior derecha hasta la esquina inferior izquierda, formando así una gran X en el pantalla. No debe haber otras líneas dibujadas en la pantalla.  </p>
  <h4>Ejercicio 2</h4>
  <p>Escribe un programa Python (<em>ejercicio6.2.py</em>) que utilice posicionamiento relativo para controlar a la tortuga, y que dibuje un triángulo equilatero en la pantalla.  </p>
  <h4>Ejercicio 3</h4>
<p>Escribe un programa Python (<em>ejercicio6.3.py</em>) que utilice posicionamiento relativo para controlar a la tortuga, y que dibuje una letra W.  </p>
<h4>Ejercicio 4</h4>
<p>Escribe un programa en Python (<em>ejercicio6.4.py</em>)  para controlar a la tortuga, y que dibuje tres círculos concéntricos de diferente color y anchura de línea..</p>
  
<h4>Ejercicio 5</h4>
<p>Escribe un programa en Python (<em>ejercicio6.5.py</em>) con un conjunto de instrucciones que fije la forma de la tortuga a turtle, y la mueva desde el fondo de la pantalla hacia la parte superior, haciendo cada vez más pequeña a medida que avanza.</p>
<h4>Ejercicio 6</h4>
  <p>Escribe un programa en Python (<em>ejercicio6.6.py</em>) con un conjunto de instrucciones que mueva la tortuga con forma de la tortuga, y la mueva desde el fondo de la pantalla hacia la parte superior, cambiando su color cuando cruce el centro de la pantalla.</p>
  <h4>Ejercicio 7</h4>
  <p>Escribe un programa en Python (<em>ejercicio6.7.py</em>) con un conjunto de instrucciones para controlar la tortuga y generar un interesante diseño.</p>
  <p><img class="image-center" src="diseno.jpg" alt="" width="263" height="271"></p>
 
  <p>&nbsp;</p>
<!-- InstanceEndEditable --><!-- End the content-main division -->

</div>
		<li><a name="ej7">Soluciones ejercicios 7</a></li>
		<div id="content-main">
<!-- InstanceBeginEditable name="Cuerpo" -->
 
  <h4>Ejercicio 1</h4>
  <p>Escribe una función llamada <code>convertStatus()</code> a la que  se le pasa el código de estado <code>'f'</code>, <code>'s'</code>, <code>'j'</code> o <code>'r'</code> y devuelve la cadena <code>'freshman'</code>, <code>'sophomore'</code>, <code>'junior'</code> o <code>'senior'</code>, respectivamente. Diseña tu función de forma que si recibe una letra inapropiada, devuelva un valor de error. Asegúrate de incluir un <em>docstring</em> apropiado para la función. Escribe un programa Python (<em>ejercicio7.1.py</em>) con la función <code>convertStatus()</code> y el código necesario para probar el correcto funcionamiento de dicha función.</p>
  <h4>Ejercicio 2</h4>
  <p>Escribe una función llamada <code>compruebaPalindromo()</code> que utilice iteración para  devolver <code>True</code> si una cadena proporcionada es un palíndromo, y <code>False</code> en caso contrario. Asegúrate de incluir la especificación <em> docstring</em> para la función. Escribe un programa Python (<em>ejercicio7.2.py</em>) con la función <code>compruebaPalindromo()</code> y el código necesario para probar el correcto funcionamiento de dicha función.</p>

<h4>Ejercicio 3</h4>
<p>Implementa un conjunto de funciones llamadas <code>getDatos()</code>, <code>extraeValores()</code> y <code>calcRatios()</code>. La función <code>getDatos()</code> debe solicitar al usuario que ingrese pares de enteros, dos por línea, con cada par leído como una sola cadena, por ejemplo,</p>

<table class="tb-formula">
  <tr><td>
<div>
<pre>Introduce una par de enteros (pulsa Enter para finalizar):
134 289 <em>(leído como '134 289')</em>
<em>etc</em></pre></div>
</td></tr></table>



<p>Estas cadenas se deben pasar una a la vez mientras se leen pasar a la función  <code>extraeValor()</code>, que está diseñada para devolver la cadena como una tupla de dos valores enteros,</p>

<table class="tb-formula">
<tr><td>
<div>
<pre>extraeValores('134 289')
<em>[...devuelve (134, 289)...]</em></pre></div>
</td></tr></table>


<p>Finalmente, cada una de estas tuplas se pasa a la función <code>calcRatios()</code> para calcular y devolver el ratio  de los dos valores. Por ejemplo,</p>
<table class="tb-formula">
<tr><td>
<div>
<pre>calcRatios((134, 289))
<em>[...devuelve 0.46366782006920415...]</em></pre></div>
</td></tr></table>

<p><br>
Implementa un programa completo (<code>ejercicio7.3.py</code>) que muestre una lista de ratios para una serie  de pares de valores enteros ingresados por teclado. Asegúrate de incluir la especificación de <code>docstring</code> para cada una de las funciones.</p>
<h4>Ejercicio 4</h4>
<p>Crea un módulo Python, llamado <code>misfunciones.py</code>, con las funciones del ejercicio 3. Después, implementa un programa Python (<em>ejercicio7.4.py</em>), similar al del ejercicio anterior, pero que en lugar de definir las funciones las importe del módulo <code>misfunciones</code>.</p>
 
  <p>&nbsp;</p>
<!-- InstanceEndEditable --><!-- End the content-main division -->

</div>
	</ul>
</ol>