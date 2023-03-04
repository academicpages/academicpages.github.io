# Curso de Física
# 2022.2
# 3<sup>a</sup> Lista de Cálculo Numérico

_______________________________

1. Verifique que no Método do Ponto Fixo, se a função de iteração $\phi$ for tal que $\phi'(x)<0$ em $I$, onde $I$ é um intervalo centrado em $\xi$ (solução do problema), então, dado $x_0 \in I$, a sequência $\{x_k\}$, onde $x_{k+1}=\phi(x_k)$ oscila em torno de $\xi$.


1. Se a função do de iteração do Método do Ponto Fixo for tal que as condições do teorema de convergência estão satisfeitas:
a. Mostre que $$|\xi- x_k| \leq \frac{M}{1-M} |x_k - x_{k-1}|.$$
b. Para que valores de $M$ teremos então que $|\xi - x_k| <  \epsilon$ se $|x_k-x_{k-1}| < \epsilon$.


1. Considerando a função $f:\mathbb{R} \to \mathbb{R}$ dada por $f(x)=x^3-x-1$. Resolva-a pelo Método do Ponto Fixo com a função de iteração $\phi(x) = \frac{1}{x}+\frac{1}{x^2}$ e $x_0=1$. Justifique seus resultados.

1. Considere o Método de Newton para encontrar $\sqrt{a}$, para $a>0$. Mostre que $$x_{n+1}=\frac{1}{2}\left( x_n + \frac{a}{x_n} \right).$$

1. Faça todos os outros exercícios do Capítulo 2 do livro da Ruggiero.
