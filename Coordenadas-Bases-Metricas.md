---
documentclass: extarticle
fontsize: 12pt
geometry: margin=2.5cm
header-includes:
    - \usepackage{dsfont}
    - \usepackage{amsmath}
    - \usepackage{amsfonts}
    - \usepackage{unicode-math}
    - \usepackage[dvipsnames]{xcolor}
    - \setlength{\fboxrule}{2pt}
title: Bases Vectoriales Cartografía
author: Javier J. Clavijo
---

# Guia para Clase 3: borrador uso interno.

Autor: Javier Clavijo, Utilizar bajo los términos de la licencia CC-By-SA-4.0:
https://creativecommons.org/licenses/by-sa/4.0/

## Coordenadas $\ne$ Bases Vectoriales.

El primer paso para la elaboración de una carta es la adopción de un sistema de coordenadas para decribir los puntos en $\mathds{R}^3$ que serán objeto de la transformación que se construirá.

Al adoptar un sistema de coordenadas, lo que se está haciendo es tomar una parametrización del espacio completo, y para poder analizar el comportamiento de las transformaciones a aplicar, debemos conocer la relación de esta parametrización con respecto al sistema cartesiano.

Adoptaremos el sistema de coordenadas esféricas, que se relaciona con el sistema cartesiano segun las siguientes ecuaciones:

\begin{align*}
x &= R\, cos\, \varphi cos\, \lambda \\
y &= R\, cos\, \varphi seno\, \lambda \\
z &= R\, seno\, \varphi 
\end{align*}

Cada sistema de coordenadas tiene asociado una base vectorial, que es un conjunto de vectores (campos vecoriales), uno por cada coordenada, que en cada punto del espacio toman la dirección de la linea coordenada correspondiente, y cuya magnitud corresponde a la escala con la que se traduce un desplazamiento en dicha coordenada al espacio parametrizado.

----

Notacion:

En lo que sigue, denominaremos a los vectores con letra negrita mientras que con letra simple se designara coordenadas. Por ejemplo $\symbf{\varphi}$ es el vector base que se genera al avanzar por la coordenada $\varphi$. 

----

Siendo $\symbf{r}$ el vector posición, y $\{x,y,z\}$ las coordenadas del sistema cartesiano, la base vectorial cartesiana queda formada por los vectores $\symbf{i},\, \symbf{j},\, \symbf{k}$ que son:

\begin{align*}
\symbf{e_x} &= \frac{\partial \symbf{r}}{\partial x} \\
\symbf{e_y} &= \frac{\partial \symbf{r}}{\partial y} \\
\symbf{e_z} &= \frac{\partial \symbf{r}}{\partial z}
\end{align*}

## Componentes de un vector

Las componentes de un vector $\symbf{v}$ en una base determinada $\{ \theta_1,\theta_2,\theta_3 \}$ --- Denotados como $v_i$ --- son los coeficientes que permiten expresar $\symbf{v}$ como una suma del tipo

$$\symbf{v} = \sum_{i=1,2,3} v_i \theta_i,$$

donde por ejemplo, para la base cartesiana $$\theta_1 = x\, , \theta_1 = y\, , \theta_3 = z$$

Dado un sistema de coordenadas $\theta$ , si son conocidas las derivadas parciales de las coordenadas cartesianas con respecto al nuevo sistema, es posible hallar las componentes de la base vectorial de $\theta$ como:

$$\symbf{\theta_i} = \sum_{j=x,y,z} \frac{\partial j}{\partial \theta_i} \symbf{e_j}$$

----

### NOTA:

Para realizar la conversion de bases, pueden expresarse los vectores de una base en funcion de la otra utilizando la matriz jacobiana como

\begin{align}
 \symbf{J} &= \begin{bmatrix}
    \dfrac{\partial \symbf{\theta_1}}{\partial \theta^*_1} & \cdots & \dfrac{\partial \symbf{\theta_1}}{\partial \theta^*_n}\\
    \vdots & \ddots & \vdots\\
    \dfrac{\partial \symbf{\theta_n}}{\partial \theta^*_1} & \cdots & \dfrac{\partial \symbf{\theta_n}}{\partial \theta^*_n} \end{bmatrix}\\
\begin{bmatrix} \symbf{\theta^*_1} & \symbf{\cdots}  & \symbf{\theta^*_n} 
\end{bmatrix} &= \begin{bmatrix} \symbf{\theta_1} & \symbf{\cdots}  & \symbf{\theta_n} 
\end{bmatrix} \begin{bmatrix}
    \dfrac{\partial \symbf{\theta_1}}{\partial \theta^*_1} & \cdots & \dfrac{\partial \symbf{\theta_1}}{\partial \theta^*_n}\\
    \vdots & \ddots & \vdots\\
    \dfrac{\partial \symbf{\theta_n}}{\partial \theta^*_1} & \cdots & \dfrac{\partial \symbf{\theta_n}}{\partial \theta^*_n} \end{bmatrix}
\end{align} 

----

La nueva base vectorial construida no es necesariamente ortogonal --- cada vector es ortogonal a todos los otros --- ni normal --- los vectores base tienen todos norma 1 ---

Para verificar esto, puede utilizarse el producto interno, dado que cumple con las propiedades de que $$\symbf{a} \cdot \symbf{b} = \|\symbf{a}\|\, \|\symbf{b}\| cos\alpha,$$ donde $\alpha$ es el ángulo comprendido entre ambos vectores, y que $$\|\symbf{a}\| = \symbf{a}\cdot\symbf{a}.$$

Por ejemplo, la base del sistema de coordenadas esféricas puede expresarse como 

\begin{align}
\symbf{r} &=& cos\varphi\, cos\lambda\, \symbf{e_x} &+& cos\varphi\, sen\lambda\, \symbf{e_y} &+& sen\varphi\, \symbf{e_z} \\
\symbf{\varphi} &=& -R sen\varphi\, cos\lambda\, \symbf{e_x} &-& R sen\varphi\, sen\lambda\, \symbf{e_y} &+& R cos\varphi\, \symbf{e_z} \\
\symbf{\lambda} &=& -R cos\varphi\, sen\lambda\, \symbf{e_x} &+& R cos\varphi\, cos\lambda\, \symbf{e_y} &+& 0\, \symbf{e_z} 
\end{align}

Luego, para verificar la ortogonalidad debemos verifica si se cumple que $$\symbf{\varphi}\cdot\symbf{\lambda} = 0,\,\symbf{\varphi}\cdot\symbf{r} = 0,\,\symbf{r}\cdot\symbf{\lambda} = 0.$$

----

NOTA: Introducimos aqui el convenio de sumación de einstein. En el mismo, cada vez que aparecen dentro del mismo término subíndices repetidos, significa que este término representa la sumatória de ese término sobre todos los valores posibles de ese subindice. Por ejemplo $$\symbf{a} = a_i \symbf{e_i} = \sum_{i=x,y,z} a_i \symbf{e_i},$$ es la representación de un vector \textbf{a} segun sus componentes sobre la base $\{\symbf{e_x},\symbf{e_y},\symbf{e_z}\}.$

----

Debemos tener en cuanta que el producto interno entre dos vectores se expresa como $$\symbf{a}\cdot\symbf{b} = a_i\symbf{e_i}\cdot b_j\symbf{e_j} = a_i b_j \symbf{e_i}\cdot \symbf{e_j},$$ debido a la bilinealidad del producto interno. Luego, si los vectores están expresados en una base ortogonal, $$\symbf{e_i} \cdot \symbf{e_j} = 0, \forall i \ne j, $$ es decir que de los 9 términos de la sumatoria solo se conservan aquellos donde $i=j$. Luego, $$\symbf{a}\cdot\symbf{b} = a_i\symbf{e_i}\cdot b_i\symbf{e_i} = a_i b_i \symbf{e_i}\cdot\symbf{e_i} = a_i b_i \|\symbf{e_i}\|^2.$$

En adición, si la base vectorial utilizada es también normal, es decir que $\|\symbf{e_i}\|^2 = 1 \forall i,$ $$\symbf{a}\cdot\symbf{b} = a_i b_i,$$ que es la forma que utilizamos para definir el producto interno cuando trabajamos con la base cartesiana de $\mathds{R}^2$.

Volviendo ahora a nuestros vectores de la base $\{\symbf{\varphi},\symbf{\lambda},\symbf{r}\}$, vemos que 
\begin{align*}
\symbf{\varphi} \cdot \symbf{\lambda} =& (-R sen\varphi\, cos\lambda)\,(-R cos\varphi\, sen\lambda)\, \symbf{e_x} \cdot \symbf{e_x} + \\
                                       &+ (- R sen\varphi\, sen\lambda)\, (R cos\varphi\, cos\lambda)\, \symbf{e_y} \cdot \symbf{e_y} + \\
									   &+ (R cos\varphi)\, 0\, \symbf{e_z} \cdot \symbf{e_z} \\
								      =& R^2 sen\varphi\, cos\varphi\, sen\lambda\, cos\lambda\, - R^2 sen\varphi\, cos\varphi\, sen\lambda\, cos\lambda = 0 \\
\symbf{\varphi} \cdot \symbf{r} =& (-R sen\varphi\, cos\lambda)\,(cos\varphi\, cos\lambda)\, \symbf{e_x} \cdot \symbf{e_x} + \\
                                       &+ (- R sen\varphi\, sen\lambda)\, (cos\varphi\, sen\lambda)\, \symbf{e_y} \cdot \symbf{e_y} + \\
									   &+ (R cos\varphi)\, (sen\varphi)\, \symbf{e_z} \cdot \symbf{e_z} \\
								      =& -R sen\varphi\, cos\varphi\, cos^2\lambda\, -R sen\varphi\, cos\varphi\, sen^2\lambda\, + 
									     R cos\varphi\, sen\varphi = 0\\
\symbf{\lambda} \cdot \symbf{r} =& (-R cos\varphi\, sen\lambda\,)\,(cos\varphi\, cos\lambda)\, \symbf{e_x} \cdot \symbf{e_x} + \\
                                       &+ (R cos\varphi\, cos\lambda)\, (cos\varphi\, sen\lambda)\, \symbf{e_y} \cdot \symbf{e_y} + \\
									   &+ 0\, (sen\varphi)\, \symbf{e_z} \cdot \symbf{e_z} \\
								      =& -R cos^2\varphi\, sen\lambda\, cos\lambda\, + R cos^2\varphi\, sen\lambda\, cos\lambda\,
									     = 0
\end{align*}

Queda demostrado entonces que la nueva base vectorial es ortogonal. Queda comprobar los modulos de los vectores para verificar la normalidad.

\begin{align*}
\symbf{\varphi} \cdot \symbf{\varphi} =& (-R sen\varphi\, cos\lambda)\,(-R sen\varphi\, cos\lambda)\, \symbf{e_x} \cdot \symbf{e_x} + \\
                                       &+ (- R sen\varphi\, sen\lambda)\, (- R sen\varphi\, sen\lambda)\, \symbf{e_y} \cdot \symbf{e_y} + \\
									   &+ (R cos\varphi)\, (R cos\varphi)\, \symbf{e_z} \cdot \symbf{e_z} \\
								      =& R^2 sen^2\varphi\, cos^2\lambda\, + R^2 sen^2\varphi sen^2\lambda\, + R^2 cos^2\varphi = R^2 \\
\symbf{\lambda} \cdot \symbf{\lambda} =& (-R cos\varphi\, sen\lambda\,)\,(-R cos\varphi\, sen\lambda\,)\, \symbf{e_x} \cdot \symbf{e_x} + \\
                                       &+ (R cos\varphi\, cos\lambda)\, (R cos\varphi\, cos\lambda)\, \symbf{e_y} \cdot \symbf{e_y} + \\
									   &+ 0\, \symbf{e_z} \cdot \symbf{e_z} \\
								      =& R^2 cos^2\varphi\, sen^2\lambda\, + R cos^2\varphi\, cos^2\lambda\, = R^2 cos^2\varphi\\
\symbf{r} \cdot \symbf{r} =& (cos\varphi\, cos\lambda)\,(cos\varphi\, cos\lambda)\, \symbf{e_x} \cdot \symbf{e_x} + \\
                                       &+ (cos\varphi\, sen\lambda)\, (cos\varphi\, sen\lambda)\, \symbf{e_y} \cdot \symbf{e_y} + \\
									   &+ (sen\varphi)\, (sen\varphi)\, \symbf{e_z} \cdot \symbf{e_z} \\
								      =& cos^2\varphi\, cos^2\lambda\, + cos^2\varphi\, sen^2\lambda\, + sen^2\varphi = 1
\end{align*}

Se verifica que los modulos de los vectores base no son todos iguales, por lo tanto la base no es normal.

----

NOTA: Esto significa que la métrica de este sistema de coordenadas es distinta a la identidad y no es constante. En consecuencia, si se construye una carta del subespacio $r=k$ sobre el plano $\mathds{R}^2$, utilizando la transformación que resulta intuitiva $\varphi \rightarrow x,\, \lambda \rightarrow y$, la escala se verá afectada en forma diferente para cada punto (metrica variable) y para cada dirección (metrica distinta a la identidad). En forma intuiva, si la magnitud de los vectores base varia en cada punto del espacio, y la relación entre ellos no se mantiene, al aplicarlos a una base de $\mathds{R}^2$ que sí cumple con estas carácterísticas, existiran deformaciones en todos los sentidos descriptos.

----

Una transformación cualquiera $$\theta_x=f(\varphi,\lambda),\theta_y=g(\varphi,\lambda)$$ que sea continua y biyectiva, definida sobre un subespacio continuo de $\mathds{R}^3$ descripto por las ecuaciones $$r=k;\,a < \varphi < b;\,c < \lambda < d, \mid a,b \in [-\frac{\pi}{2};-\frac{\pi}{2}]; c,d \in [-\pi;\pi],$$ puede interpretarse como un nuevo sistema de coordenadas del subespacio definido, que genera una base vectorial $\symbf{\theta_x},\symbf{\theta_y}$. Las componentes de estos vectores pueden calcularse conociendo las derivadas parciales de la transformación inversa, de manera que 

\begin{align}
\symbf{\theta_x} = & \dfrac{\partial \symbf{r}}{\partial x} = & \dfrac{\partial \symbf{r}}{\partial \varphi} \dfrac{\partial \varphi}{\partial x} + \dfrac{\partial \symbf{r}}{\partial \lambda} \dfrac{\partial \lambda}{\partial x} = \symbf{\varphi} \dfrac{\partial \varphi}{\partial x} + \symbf{\lambda} \dfrac{\partial \lambda}{\partial x} \\
\symbf{\theta_y} = & \dfrac{\partial \symbf{r}}{\partial y} = & \dfrac{\partial \symbf{r}}{\partial \varphi} \dfrac{\partial \varphi}{\partial y} + \dfrac{\partial \symbf{r}}{\partial \lambda} \dfrac{\partial \lambda}{\partial y} = \symbf{\varphi} \dfrac{\partial \varphi}{\partial y} + \symbf{\lambda} \dfrac{\partial \lambda}{\partial y} \\
\end{align}

Un vector $\symbf{a} = a_i \symbf{\theta_i}, i\in\{x,y\}$ expresado en esta base vectorial, cumple que $$\|a\|^2 = a_i a_j \symbf{\theta_i} \cdot \symbf{\theta_j}$$

Para poder hallar una expresion general es de práctica utilidad hallar las cantidades $\symbf{\theta_x} \cdot \symbf{\theta_x}, \symbf{\theta_x} \cdot \symbf{\theta_y}, \symbf{\theta_y} \cdot \symbf{\theta_x},\symbf{\theta_y} \cdot \symbf{\theta_y}$, de los cuales el segundo y el tercero son iguales, por propiedad conmutativa del producto interno. Estas cantidades se denominan componentes de la metrica del sistema de coordenadas, y se notan $g_{ij} , i,j \in {x,y}$. 

\begin{align}
g_{xx} = & \dfrac{\partial \varphi}{\partial x}^2 \|\symbf{\varphi}\|^2 + \dfrac{\partial \lambda}{\partial x}^2 \|\symbf{\lambda}\|^2 \\
g_{yy} = & \dfrac{\partial \varphi}{\partial y}^2 \|\symbf{\varphi}\|^2 + \dfrac{\partial \lambda}{\partial y}^2 \|\symbf{\lambda}\|^2 \\
g_{xy} = & \dfrac{\partial \varphi}{\partial x}\dfrac{\partial \varphi}{\partial y} \|\symbf{\varphi}\|^2 + \dfrac{\partial \lambda}{\partial x}\dfrac{\partial \lambda}{\partial y} \|\symbf{\lambda}\|^2
\end{align}

Notamos que ahora el producto interno de vectores expresados en la nueva base vectorial puede ser reescrito como $$\symbf{a} \cdot \symbf{b} = a_i b_j g_{ij}$$

Podemos ver que, en caso de que los vectores $\theta_x,\theta_y$ fueran ortogonales, la componente $g_{xy}$ se anula, por tanto el producto interno en la base vectorial expresada queda escrito como $$\symbf{a} \cdot \symbf{b} = a_i b_i g_{ii}$$.

A las componentes de la métrica de un sistema de coordenadas definido sobre un subespacio de dimension dos se las llama también términos gaussianos, por ser Carl Gauss quien primero los estudió, y se los suele denominar E,F y G, tal que $E= g_{xx}, F=g_{xy}=g_{yx}, G=g_{yy}$

----

NOTA:
Cuando se genera un sistema de coordenadas partiendo de aplicar una transformación sobre un subespacio plano parametrizado por $\symbf{u}\,\symbf{v}$, tal que $\|\symbf{u}\|=1$, $\|\symbf{v}\|=1$, $\symbf{u} \cdot \symbf{v}=0$. Las componentes de la métrica, si nombramos $\theta_1,\theta_2$ a las nuevas coordenadas queda expresada como 

\begin{align}
E = & \dfrac{\partial u}{\partial \theta_1}^2 + \dfrac{\partial u}{\partial \theta_2}^2 \\
G = & \dfrac{\partial v}{\partial \theta_1}^2 + \dfrac{\partial v}{\partial \theta_2}^2 \\
F = & \dfrac{\partial u}{\partial \theta_1}\dfrac{\partial v}{\partial \theta_1} + \dfrac{\partial u}{\partial \theta_2}\dfrac{\partial v}{\partial \theta_2},
\end{align}

----

Tal como mencionamos mas arriba, no hay garantias de que para una transformacion genérica $\mathds{R}^2 \rightarrow \mathds{R}^2$, la base $\symbf{\theta_x};\symbf{\theta_y}$ generada sea ortogonal aun cuando la base del sistema de coordenadas de origen lo fuera, sin embargo podemos hacer la siguiente observación.

**Observacion:** En general se cumple que $\symbf{a} \cdot \symbf{-a} = - \|\symbf{a}\|^2$, lo que reemplazando en $cos\alpha = \frac{\|\symbf{a}\|\|\symbf{b}\|}{\symbf{a}\cdot\symbf{b}}$ nos indica que el angulo entre un vector y el mismo vector con su signo invertido es siempre $\pi$. 

**Planteo:** Dados los vectores a,b ortogonales entre si se les aplica a ambos la misma transformación, obteniendo los vectores $\symbf{a^\star},\symbf{b^\star}$, no necesariamente ortogonales. Por definición, el ángulo $\hat{ab} = \frac{\pi}{2}$ y luego, $\hat{-ba)} = \frac{\pi}{2}$. También sabemos que $\hat{\symbf{-b^\star},\symbf{a^\star}}+\hat{\symbf{a^\star},\symbf{b^\star}} = \pi$, y por tanto si $\hat{\symbf{-b^\star},\symbf{a^\star}} > \frac{\pi}{2}$, entonces $\hat{\symbf{a^\star},\symbf{b^\star}} < \frac{\pi}{2}$.

Considerense todos los posibles vectores $\symbf{a'},\symbf{b'}$, que surgen de rotar a y b un angulo fijo menor a $\frac{\pi}{2}$. Vemos que al aplicar una rotación de $\frac{\pi}{2}$, quedará $\symbf{a'} = \symbf{b},\symbf{b'}=\symbf{-a}$, y por ende $\symbf{a^{\star'}}=\symbf{b^\star},\symbf{b^{\star'}}=\symbf{-a^\star}$ de manera que bajo el mismo supuesto del parrafo anterior $\hat{\symbf{-b^{\star'}},\symbf{a^{\star'}}} < \frac{\pi}{2}$, y $\hat{\symbf{a^{\star'}},\symbf{b^{\star'}}} > \frac{\pi}{2}$, es decir que las desigualdades se invirtieron.

Como la transformación de rotación aplicada es continua y suave, el de angulo entre $\symbf{a^\star}$ y $\symbf{b^\star}$ también lo es, y existe un valor intermedio que cumple que $\hat{\symbf{a^\star},\symbf{b^\star}} = \frac{\pi}{2}$

----

Trasladando esta observación a nuestro ejemplo, vemos que dada una transformacion $f(\varphi,\lambda),g(\varphi,\lambda)$, podemos encontrar una base vectorial $\symbf{\varphi'},\symbf{\lambda'}$, que se transforma a un par de vectores ortogonales. Si tomamos este nuevo par como base, vemos que en ese sistema de coordenadas las componentes de la metrica $g_{ij} = 0 \forall i \ne j$, de manera que el módulo de un vector expresado en esa base queda definido como $$\|\symbf{a}\|^2 = a_i a_i g_ii = a_x^2 g_{xx} + a_y^2 g_{yy}$$, de manera que, independientemente de cual sean los valores de $g_{yy}$ y $g_{xx}$, si no son iguales, y consideramos el circulo unitario en el plano xy, los modulos de los vectores en el espacio original tendran sus valores extremos en las direcciones de los ejes x e y, y se cumplirá además que $$ \frac{a_x^2 g_{xx}}{g_{xx}} + \frac{a_y^2 g_{yy}}{g_{xx}} = 1$$, de modo que el circulo unitario del plano xy corresponde a una elipse en el espacio original.

----

Hallaremos ahora una forma de encontrar la rotación necesaria para hayar estas direcciones a las que llamaremos fundamentales.

Construimos $\symbf{\varphi'},\symbf{\lambda'}$ de manera que, con un parámetro A, de manera que $\symbf{\varphi'} \cdot \symbf{\varphi} = cosA \|\symbf{\varphi'}\| \|\symbf{\varphi}\|$ de modo que con $A\in (-\pi,\pi]$ puedan barrerse todas las orientaciones posibles, y que $\symbf{\varphi'}\cdot\symbf{\lambda'}=0$, $\|\symbf{\varphi'}\|=\|\symbf{\varphi}\|$ y $\|\symbf{\lambda'}\|=\|\symbf{\lambda}\|$

$$\symbf{\varphi'} = \frac{senA \|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} \symbf{\lambda} + cosA \symbf{\varphi}$$

$$\symbf{\lambda'} = cosA \symbf{\lambda} - \frac{senA \|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} \symbf{\varphi}$$

Notación: dada la transformación $\theta^\star_1(\theta_1,\theta_2), \theta^\star_2(\theta_1,\theta_2)$, anotamos las derivadas parciales utilizando una coma y luego un subindice, por ejemplo $$\theta^\star_{1,\theta_2} = \dfrac{\partial \theta^\star_{1}}{\partial \theta_2}$$

Luego, si aplicamos sobre los vectores construidos la transformación $x = f(\varphi,\lambda), y=g(\varphi,\lambda)$, podemos expresar $\symbf{\varphi}, \symbf{\lambda}$ en funcion de los nuevos vectores $\symbf{x}, \symbf{y}$.


$$\symbf{\varphi'} = \left[ \frac{senA \|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} \theta_{x,\lambda} + cosA \theta_{x,\varphi} \right] \symbf{x} 
                     \left[ \frac{senA \|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} \theta_{y,\lambda} + cosA \theta_{y,\varphi} \right] \symbf{y} $$

$$\symbf{\lambda'} = \left[cosA \theta_{x,\lambda} - \frac{senA \|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} \theta_{x,\varphi} \right] \symbf{x} +
                     \left[cosA \theta_{y,\lambda} - \frac{senA \|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} \theta_{y,\varphi} \right] \symbf{y} $$

La condición que buscamos es que, en el plano xy, generado por la base ortonormal $\{\symbf{x},\symbf{y}\}$, $\symbf{\varphi'}$ y $\symbf{\lambda'}$ sean ortogonales. 

----

NOTA: Hacemos notar que en general $\|\symbf{x}\|\ne1$, $\|\symbf{y}\|\ne1$ y $\symbf{x} \cdot \symbf{y}$ en el espacio de origen, sin embargo, estamos evaluando la ortogonalidad en el plano xy, donde $\symbf{x},\symbf{y}$ es la base ortonormal canónica del plano. Es decir, que nuestra transformación se da entre dos espacios distintos. Por ello, calcularemos el producto interno entre ambos vectores, pero en lugar de utilizar la métrica $g_{ii}$ calculada en $\mathds{R}^3$, utilizaremos la identidad, que es la métrica del sistema cartesiano del plano XY.

----

En el plano xy entonces, el producto escalar queda expresado como $$\symbf{\varphi'} \cdot \symbf{\lambda'} = \varphi'_x\lambda'_y + \lambda'_x\varphi'_y$$

\begin{align*}
\symbf{\varphi'} \cdot \symbf{\lambda'} &= \frac{senA \|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} {\theta_{x,\lambda}}^2 cosA - \frac{senA \|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} \frac{senA \|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} \theta_{x,\lambda} \theta_{x,\varphi} + cos^2A \theta_{x,\lambda} \theta_{x,\varphi} - cosA \frac{senA \|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} {\theta_{x,\varphi}}^2 +  \\
                                      &+ \frac{senA \|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} {\theta_{y,\lambda}}^2 cosA - \frac{senA \|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} \frac{senA \|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} \theta_{y,\lambda} \theta_{y,\varphi} + cos^2A \theta_{y,\lambda} \theta_{y,\varphi} - cosA \frac{senA \|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} {\theta_{y,\varphi}}^2 \\
									  &= senA\,cosA \left[\frac{\|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} {\theta_{x,\lambda}}^2 - \frac{\|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} {\theta_{x,\varphi}}^2 \right] + \theta_{x,\lambda} \theta_{x,\varphi} (cos^2A-sen^2A) +  \\
									  &+ senA\,cosA \left[\frac{\|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} {\theta_{y,\lambda}}^2 - \frac{\|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} {\theta_{y,\varphi}}^2 \right] + \theta_{y,\lambda} \theta_{y,\varphi} (cos^2A-sen^2A) \\
									  &= \underbrace{senA\,cosA}_{\frac{1}{2}sen(2A)} \left[\frac{\|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} \underbrace{({\theta_{x,\lambda}}^2+{\theta_{y,\lambda}}^2)}_{\text{G}} - \frac{\|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} \underbrace{({\theta_{x,\varphi}}^2+{\theta_{x,\varphi}}^2)}_{\text{E}} \right] + \underbrace{(\theta_{x,\lambda} \theta_{x,\varphi} + \theta_{y,\lambda} \theta_{y,\varphi})}_{\text{F}} \underbrace{(cos^2A-sen^2A)}_{cos(2A)}
\end{align*}

Recordamos aqui que los modulos que aparecen en la formula, $\|\symbf{\varphi}\|$ y $\|\symbf{\lambda}\|$ se refieren al espacio de origen, es decir que $$\frac{\|\symbf{\lambda}\|}{\|\symbf{\varphi}\|} = cos\varphi\,;\,\frac{\|\symbf{\varphi}\|}{\|\symbf{\lambda}\|} = cos^-1\varphi$$

Reemplazando en la ecuacion de $\symbf{\varphi'} \cdot \symbf{\lambda'}$ en el espacio objetivo, e igualandolo a 0 nos queda

\begin{align}
0 &= \frac{sen(2A)}{2} \left(\frac{\text{G}}{cos\varphi} - \text{E}cos\varphi\right) + \text{F} cos(2A) \\
\frac{sen(2A)}{cos(2A)} = tan(2A) &= \frac{2\text{F}\, cos\varphi}{-\text{G} + \text{E}cos^2\varphi}
\end{align}

Si la primera de estas dos expresiones no se anula en forma general, la segunda de ellas presenta cuatro soluciones de la forma $A+k\frac{\pi}{2},\, k \in \{1,2,3,4\}$. En los casos en que la primera expresion se anula en general, resulta que cualquier par de vectores ortogonales en el espacio de origen lo son en el espacio objetivo, lo cual quiere decir que estamos ante una transformación conforme.

----

Ejercicio:

comprobar que para la transformacion de mercator la formula se anula en general

----

No es casual que hallamos dado los nombres E, G, y F a los términos que aparecen en la formula. Estos términos corresponden a la métrica del sistema de coordenadas $\varphi,\lambda$ definido sobre el plano xy -- nuestro espacio objetivo en la transformacion $f,g$ analizada --, que se define como $\varphi = h(x,y)\,;\, \lambda = i(x,y)$ donde $h$ e $y$ son funciones tales que $h(f(\varphi_1,\lambda_1),g(\varphi_1,\lambda_1) = \varphi_1\,;\,i(f(\varphi_1,\lambda_1),g(\varphi_1,\lambda_1) = \lambda_1$

Esta métrica nos permite definir el producto interno y la norma en el espacio objetivo, con vectores expresados en el sistema de coordenadas $\varphi,\lambda$. Es decir que estamos ahora interpretando a $\varphi,\lambda$ como una parametrizacion alternativa de $\mathds{R}^2$

Por ejemplo, $$\|\symbf{a}\|^2 = a_\varphi^2 E + a_\lambda^2 G + 2 F a_\lambda a_\varphi$$ nos permite calcular, a partir de las coordenadas $\varphi,\lambda$, la norma del vector resultante en la carta -- espacio objetivo --.

----

Observación:

En caso de que hallar las funciones $h',i'$ que generan las coordenadas $\varphi',\lambda'$, de tal manera que $\symbf{\varphi} \cdot \symbf{\lambda} = 0$, que corresponden a las direcciones fundamentales halladas anteriormente, la métrica generada, descripta por los valores E', G' y F', es tal que $F'=0$. Luego, el producto interno en esta base queda expresado como $$\|\symbf{a}\|^2 = a_{\varphi'}^2 E' + a_{\lambda'}^2 G'$$. De modo que, sean cuales sean los valores de E y G, si no son iguales, se da la misma situación descripta anteriormente, donde partiendo de un circulo en el plano $\varphi'\lambda'$, se llega a una elipse en el plano xy, con los ejes mayor y menor orientados segun los ejex x e y. Demostrando que las direcciones de $\symbf{\varphi'},\symbf{\lambda'}$ son las direcciones de maxima y minima deformacion de escala, y los factores $\sqrt{E'}$ y $\sqrt{G'}$ son los factores de escala máximo y mínimo, también llamados módulos de deformación lineal.

----

Si queremos hallar el factor de escala en una dirección arbitraria, debemos comparar la norma de un vector en el espacio origen y en el espacio objetivo. Tomaremos el vector $\symbf{\varphi'}$, definido como dijimos, de tal forma que en el espacio geográfico $\symbf{\varphi'} \cdot \symbf{\varphi} = cosA \|\symbf{\varphi'}\| \|\symbf{\varphi}\|$ y $\|\symbf{\varphi'}\|^2=\|\symbf{\varphi}\|^2 = R^2$.

Las componentes de este vector son $$ \varphi'_\varphi = cosA ,\, \varphi'_\lambda = \frac{cosA}{cos\varphi},$$ de manera tal que, en el espacio objetivo se da 

$$\|\symbf{\varphi'}\|^2 = {\varphi'_\varphi}^2 E + {\varphi'_\lambda}^2 G + 2 F \varphi'_\lambda \varphi'_\varphi$$

$$\|\symbf{\varphi'}\|^2 = cos^2A E + \frac{sen^2A}{cos^2\varphi} G + 2 F \frac{cosAsenA}{cos\varphi}$$

Luego, el factor de escala en una dirección queda expresado como

$${m^l_A}^2 =\frac{\|\symbf{\varphi'}\|^2_{\text{espacio objetivo}}}{\|\symbf{\varphi'}\|^2_{\text{espacio origen}}} = \frac{cos^2A E + \frac{sen^2A}{cos^2\varphi} G + 2 F \frac{cosAsenA}{cos\varphi}}{R^2}$$

----

Ejercicio:

a. Se pueden hallar las direcciones fundamentales a partir de hallar los puntos extremos de ${m^l_A}^2$ considerada como una funcion del azimut A.

----
