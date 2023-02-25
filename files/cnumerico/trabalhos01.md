# Trabalhos de Cálculo Numérico


## Trabalho 01


Considere uma sequência $\{x_n\}$ que convirja com ordem 1. A partir dessa sequência defina uma novo sequência pondo $$x_n'=x_n - \frac{(x_{n+1}-x_n)^2}{x_{n+2}-2x_{n+1}+x_n}.$$

Considere, como exemplo, a sequência definida por $$x_n = \frac{(-1)^n}{2} x_n; \quad x_0=1.$$ Implemente uma função em Julia que gere os termos dessa sequência. Implemente uma funçao em Julia que gere $\{x_n'\}$, a partir dessa sequência. Faça gráfico(s) comparando essas duas sequências. Verifique que $\{x_n'\}$ converge mais rapidamente.

Agora, do ponto de vista teórico, mostre que:

Seja $\{x_n\}$ uma sequência que converge com ordem 1 ao limite $u$ tal que $e_n = x_n-u$ satisfaz $$e_{n+1}=(A+\delta_n)e_n, \quad e_n \ne 0,$$ onde $A$ é uma constante tal que $0 < A < 1$ e $\lim_{n \to +\infty}\delta_n = 0$. Então a sequência $\{x_n'\}$, definida acima, converge para $u$ mais rapidamente do que $\{x_n\}$, ou seja, $$\lim_{n \to +\infty} \frac{x_n'-u}{x_n-u}=0.$$

Construa mais exemplos que mostram esse comportamento.


## Trabalho 2

Implementar, em Julia, o Método da Falsa Posição. Fazer um estudo comparativo com o Método da Bisseção, Ponto Fixo e Newton. Esse estudo deve seguir a seguinte linha:

1. Escolher problemas testes adequados para o estudo;
2. Implementar os métodos acima mensionados;
3. Fazer gráficos e tabelas para analisar o comportamento desses métodos;
4. Com base nos resultados, comparar a velocidade de convergência desses métodos.


## Trabalho 3

Implementar, em Julia, o Método da Tangente. Fazer um estudo comparativo com o Método da Bisseção, Ponto Fixo e Newton. Esse estudo deve seguir a seguinte linha:

1. Escolher problemas testes adequados para o estudo;
2. Implementar os métodos acima mensionados;
3. Fazer gráficos e tabelas para analisar o comportamento desses métodos;
4. Com base nos resultados, comparar a velocidade de convergência desses métodos.