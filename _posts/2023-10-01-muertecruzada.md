---
title: '¿Es la Muerte Cruzada un Ancla o un Salvavidas?'
date: 2023-10-01
permalink: /posts/2023/10/muertecruzada/
tags:
  - Ecuador
  - Muerte Cruzada
---
<div style="text-align: justify;"><br>
La muerte cruzada es un mecanismo de destrucción mutua asegurada que busca resolver conflictos entre el Ejecutivo y el Legislativo a través de amenazas bilaterales de disolución. A pesar de las críticas conocidas —como el desequilibrio a favor del Ejecutivo debido a costos nulos de coordinación— este mecanismo tiene también implicaciones electorales que posiblemente no fueron anticipadas por los constituyentes.<br><br>


<div style="background-color: rgb(221, 221, 221); padding: 10px;">

<strong>TL;DR:</strong> La muerte cruzada produce retornos electorales no lineales en el corto mandato del candidato electo; exacerba el problema de selección adversa; y, en última instancia, favorece una presidencia *de facto* prolongada.

</div><br>


Examinemos el caso de Guillermo Lasso, el primer presidente en recurrir al mecanismo de la muerte cruzada. Su decisión se fundamenta en la confluencia de tres factores determinantes: (a) intentos de censura legislativa, (b) desafíos en la ejecución de su programa gubernamental, y (c) una crítica crisis de narcotráfico y violencia. Aunque legalmente los dos primeros elementos ofrecen justificación suficiente para activar el mecanismo de muerte cruzada y convocar a elecciones, es poco plausible que dicho recurso se hubiera ejercido sin la presencia del tercer factor. Este último actuó como un catalizador fulminante, precipitando la decisión ante el caos sin precedentes que instigó en el país.

En este escenario inestable, el período en el poder del nuevo mandatario será de 17 meses y 14 días, extendiéndose desde el 30 de noviembre de 2023 hasta el 13 de mayo de 2025. Teóricamente, el líder electo se encuentra en una especie de lotería electoral de winner-take-all: o bien consolida su reelección, ampliando su mandato a un total de 65 meses, o es depuesto después de los 17 meses iniciales. En las siguientes líneas, argumento que esta lotería está inclinada hacia su reelección.

Este sesgo se origina en el uso de métodos bayesianos para la toma de decisiones en contextos inciertos. Supongamos que estamos en la oscuridad respecto a la habilidad del candidato electo para gestionar una crisis. Sin embargo, partimos de una creencia inicial: su habilidad, $\theta$, es una variable aleatoria que puede tomar cualquier valor entre $-\infty$ e $\infty$. Desde nuestra perspectiva, la expectativa de $\theta$ es cero, expresada como una distribución normal $\theta\sim\mathcal{N}\left(0,\tau\cdot \sigma^2\right)$. Aquí, la varianza $(\tau\cdot \sigma^2)$ actúa como un indicador cuantitativo de nuestra incertidumbre a priori, que podría ser baja (para cualquier $\tau>1$) o alta (si $\tau=1$). La figura siguiente muestra que una varianza baja (panel izquierdo) concentra la densidad de probabilidad cerca de nuestra expectativa cero, mientras que una varianza alta (panel derecho) da lugar a una distribución más dispersa y, por ende, más "plana". 


![Figure 1](/images/t11.png)<br>


Al asumir su cargo, el candidato electo se enfrenta al reto de gobernar en medio del caos. Su desempeño se manifiesta a través de una señal informativa, $y$, que para nosotros sirve como un indicador de su competencia subyacente—y está modelado como una variable aleatoria normal $y\vert\theta \sim \mathcal{N}(\theta, \sigma^2)$. ¿Cómo actualizamos nuestras creencias iniciales en función de esta señal? Según el Teorema de Bayes, en contextos con elevada incertidumbre a priori, incluso señales ruidosas sobre la habilidad del candidato adquieren una relevancia comparativa mayor. Formalmente, las creencias posteriores, $\hat{\theta}$, son proporcionales al producto de nuestras creencias a priori y la verosimilitud de la señal observada. 

Para ilustrar este fenómeno, la figura siguiente muestra cómo una alta varianza en nuestras creencias iniciales puede resultar en disparidades significativas en la actualización de nuestras creencias, \emph{dadas las mismas señales de desempeño}. Específicamente, nuestra expectativa sobre la aptitud del candidato se desplaza levemente desde el punto de origen cuando la varianza inicial es baja (panel izquierdo), en contraposición a cuando la varianza inicial es alta (panel derecho).<br><br>

![Figure 2](/images/t2.png)<br>


El impacto sustancial de una señal informativa sobre nuestras creencias puede llevar, de manera natural, a retornos electorales no-lineales. Este fenómeno se vuelve particularmente relevante en el contexto del riesgo de selección adversa que enfrentan los votantes al (re)elegir un candidato en circunstancias caóticas. Una posible mitigación para este tipo de inferencias erróneas sería disponer de un mayor número de señales sobre el candidato electo—cuantas más señales tengamos, más precisa será nuestra inferencia. Sin embargo, este enfoque se encuentra obstaculizado por el mecanismo de muerte cruzada, que impone un mandato de duración extra-limitada y, en consecuencia, restringe el número de señales informativas que podrían generarse.

Para abordarlo de forma más rigurosa, introduzcamos una métrica específica de retorno electoral que evalúe el cambio en nuestra utilidad esperada cuando optamos por un candidato en dos escenarios distintos: el primero, caracterizado por nuestras creencias a priori de alta incertidumbre y sin información adicional; y el segundo, en el que disponemos de una serie histórica de desempeños del candidato, denotada como $(y_1,...,y_n)$. En este marco, definimos nuestra función de utilidad como $-y^2$. Esta elección refleja nuestra premisa de que el candidato ideal minimizaría el caos, lo cual se traduce en una competencia $\theta^*=0$. En contraposición, cualquier candidato con $\theta\neq 0$ nos causa desutilidad en tanto contribuye al caos en lugar de apagarlo. Formalmente, esta medida de retorno equivaldría a <br>

<div>

$$
\begin{align*}
\Delta_\theta(n,\tau) &=  \frac{\mathbb{E}[-y^2\mid  y_1,\ldots,y_n]-  \mathbb{E}[-y^2]}{\mathbb{E}[-y^2]} \\[3ex]
&= \frac{\mathbb{E}\left[\mathbb{E}\left[-y^2\vert \hat{\theta}\right]\right]-\mathbb{E}\left[\mathbb{E}\left[-y^2\vert \theta\right]\right]}{\mathbb{E}\left[\mathbb{E}\left[-y^2\vert \theta\right]\right]} \quad \text{ con } \hat{\theta}\sim\mathcal{N}\left( \frac{n\,\overline{y}}{\tau+n}, \frac{\sigma^2}{\tau+n} \right) \\[3ex]
&= \frac{n\,\left[\left(n+\tau\right)\,\sigma^2-n\,\tau\left(\overline{y}\right)^2\right]}{\left(n+\tau\right)^2(1+\tau)\,\sigma^2}
\end{align*}
$$

Con esta métrica de retorno electoral, $\Delta_\theta(n,\tau)$, podemos explorar cómo la longitud del mandato condiciona el volumen de señales generables y, en consecuencia, nuestra capacidad para realizar inferencias precisas. Para ilustrar este punto, la figura subsiguiente presenta la evolución de dicha métrica en función de una secuencia aleatoria de desempeños del candidato. Específicamente, la figura sintetiza los resultados de $j\in\{1,2,...100\}$ simulaciones individuales. En cada simulación se realiza lo siguiente: (a) se selecciona de forma aleatoria entre políticos con diversos grados de competencia, y (b) se genera una secuencia aleatoria de desempeños correspondiente al número de meses del mandato, dadas las competencias seleccionadas. [Nota: El código fuente, implementado en Wolfram Mathematica, se encuentra disponible al final de este artículo].<br>



</div>


</div>