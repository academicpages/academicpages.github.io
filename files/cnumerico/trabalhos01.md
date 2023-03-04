# Trabalhos de Cálculo Numérico

### Atenção

O trabalho deverá ser entregue em arquivo pdf. Os códigos utilizados deverão ser encaminhados. encaminhar somente arquivos .jl. Arquivos do notebook Jupyter não serão aceitos. Um único membro do grupo deverá encaminhar o trabalho. Este encaminhamento deverá ser feito pelo Google Classroom em um formulário que será disponibilizado na época do envio. lembrem de colocar o nome de cada membro do grupo tanto no trabalho (arquivo pdf) quanto nos códigos que forem enviados.

#### Entregar até o dia 24/03/2023 (Essa data não será prorrogada!!)

___________________________________________

### Avaliação do Trabalho

O trabalho será avaliado considerando:

a) Sua organização;
b) Coerencia e coesão do texto.
c) Profundidade da abordagem do tema (Matemática e Computacional);
d) Qualidade e quantidade dos experimentos numéricos desenvolvidos e apresentados;
e) Informações corretas apresentadas;
f) Pertinência das referências apresentadas;



________________________________________________

# Trabalhos

## Trabalho 01

#### Grupo: Bruna e Poliana 

Considere uma sequência $\{x_n\}$ que convirja com ordem 1. A partir dessa sequência defina uma novo sequência pondo $$x_n'=x_n - \frac{(x_{n+1}-x_n)^2}{x_{n+2}-2x_{n+1}+x_n}.$$

Considere, como exemplo, a sequência definida por $$x_n = \frac{(-1)^n}{2} x_n; \quad x_0=1.$$ Implemente uma função em Julia que gere os termos dessa sequência. Implemente uma funçao em Julia que gere $\{x_n'\}$, a partir dessa sequência. Faça gráfico(s) comparando essas duas sequências. Verifique, por meio desses gráficos, que $\{x_n'\}$ converge mais rapidamente.

Agora, do ponto de vista teórico, mostre que:

Seja $\{x_n\}$ uma sequência que converge com ordem 1 ao limite $u$ tal que $e_n = x_n-u$ satisfaz $$e_{n+1}=(A+\delta_n)e_n, \quad e_n \ne 0,$$ onde $A$ é uma constante tal que $0 < A < 1$ e $\lim_{n \to +\infty}\delta_n = 0$. Então a sequência $\{x_n'\}$, definida acima, converge para $u$ mais rapidamente do que $\{x_n\}$, ou seja, $$\lim_{n \to +\infty} \frac{x_n'-u}{x_n-u}=0.$$

Construa mais exemplos que mostrem esse comportamento. Implemente, usando a linguagem Julia, cada um desses exemplos. Compare cada uma dessas sequências considerando a aceleração proposta neste exercício. Faça comentários. Use gráficos e tabelas.

______________________________

## Trabalho 2

#### Grupo: Maria Aparecida, Samuel Oliveira e Heitor

Implementar, em Julia, o **Método da Falsa Posição**. Fazer um estudo comparativo com o Método da Bisseção, Ponto Fixo e Newton. Esse estudo deve seguir a seguinte linha:

1. Escolher problemas testes adequados para o estudo;
2. Implementar os métodos acima mencionados;
3. Fazer gráficos e tabelas para analisar o comportamento desses métodos;
4. Com base nos resultados, comparar a velocidade de convergência desses métodos.
5. Faça comentários.

______________________________


## Trabalho 3
#### Grupo: Ana Clara e Murilo

Implementar, em Julia, o **Método da Secante**. Fazer um estudo comparativo com o Método da Bisseção, Ponto Fixo e Newton. Esse estudo deve seguir a seguinte linha:

1. Escolher problemas testes adequados para o estudo;
2. Implementar os métodos acima mencionados;
3. Fazer gráficos e tabelas para analisar o comportamento desses métodos;
4. Com base nos resultados, comparar a velocidade de convergência desses métodos.
5. Faça comentários.

______________________________


## Trabalho 04

#### Grupo: Naiara, Priscila e Aline

Considere o problema de determinar $x$ tal que $f(x)=0$. Seja $\phi$ uma função de iteração associada ao problema. Essa função de iteração gera a sequência $\{x_n\}$ converge para $u$. Considere o seguinte algoritmo:

#### Algoritmo

1. Dado $x_0$ na vizinhança de $u$ e $\epsilon > 0$; defina $$x_0^{(0)}=x_0, \quad x_1^{(0)}=\phi(x_0^{(0)}), \quad x_2^{(0)}=\phi(x_1^{(0)});$$
2. Para $k=0,1,2,\cdots$ calcule $$x_0^{(k+1)}=x_0^{(k)} - \frac{(x_1^{(k)}-x_0^{(k)})^2}{x_2^{(k)}-2x_1^{(k)}+x_0^{(k)}},$$ e $$x_1^{(k+1)}=\phi(x_0^{(k+1)}); \quad x_2^{(k+1)}=\phi(x_1^{(k+1)}).$$
3. Termina-se o processo, se $x_2^{(k)}-2x_1^{(k)}+x_0^{(k)}=0$ ou $|x_0^{(k+1)}-x_0^{(k)}| < \epsilon$.


Implemente o algoritmo acima, em Julia. Compare seu desempenho com o Método da Bissecção, Ponto Fixo e Newton. Use gráficos, tabelas, etc para fazer essa comparação. Faça testes com várias funções. Faça comentários.

______________________________


## Trabalho 05

#### Grupo: Ana Caroline, Arthur e Stefane

Implementar o **Método de Newton** para resolver um sistema de equações não lineares. Utilizar o método para encontrar pontos críticos de funções do tipo $f:\mathbb{R}^2 \to \mathbb{R}$. Fazer testes com várias funções. Construir gráficos que mostrem, para uma dada função, os pontos da sequência juntamente com as curvas de nível da função. Analise funções que tenham um único ponto crítico e funções que tenham mais de um ponto crítico. Escolha funções adequadas para avaliar o método. Faça comentários.

______________________________


## Trabalho 06

#### Grupo: Davi, Péricles e Samuel Carvalho

Os métodos clásicos para determinação de pontos mínimos locais (ou máximos locais) exigem como pré-requisito funções diferenciáveis. Contudo, existem métodos que são desenvolvidos para a classe de funções não-diferenciáveis. Inspirando-se no Método da Bissecção, desenvolva um algoritmo que determina o mínimo (ou máximo) de uma função não diferenciável. Implemente em Julia. Faça vários testes. Construa gráficos e tabelas. Analise o comportamento do algoritmo. Faça comentários.

______________________________


## Trabalho 07

#### Grupo: Thiago, Guilherme e James

Implementar, em Julia, o **Método de Newton adaptado**, ou seja, $$ x_{n+1} = x_n - \left( f' ( x_0 ) \right)^{ -1 } f(x_n) ,$$ para $x_0$ dado nos termos do Método de Newton. Fazer um estudo comparativo com o Método da Bisseção, Ponto Fixo e Newton. Esse estudo deve seguir a seguinte linha:

1. Escolher problemas testes adequados para o estudo;
2. Implementar os métodos acima mencionados;
3. Fazer gráficos e tabelas para analisar o comportamento desses métodos;
4. Com base nos resultados, comparar a velocidade de convergência desses métodos.
5. Faça comentários.

______________________________


## Trabalho 08

####  Grupo: Taíde, Gabriela Jade e Viviane
Neste trabalho, o grupo deverá desenvolver um algoritmo para resolver o problema $$f(x)=0.$$
Para isso, considere o seguinte procedimento:

#### Procedimento
1. Dados $f$, $[a,b]$, $\epsilon > 0$, $\eta > 0$.
2. A partir do intervalo $[a,b]$, use o Método da Bissecção (MB) para gerar um $x_0 \in \mathbb{R}$ tal que $\xi \in [a_k,b_k]$ com $|b_k-a_k| < \eta$.
3. Tome $x_0 \in [a_k,b_k]$ e a partir deste, use o Método de Newton para obter a solução do problema.

Construir e implementar o algoritmo acima. Fazer um estudo comparativo deste método com o Método da Bisseção, Ponto Fixo e Newton.

1. Escolher problemas testes adequados para o estudo;
2. Implementar os métodos acima mencionados;
3. Fazer gráficos e tabelas para analisar o comportamento desses métodos;
4. Com base nos resultados, comparar a velocidade de convergência desses métodos.
5. Faça testes variando o parâmetro $\eta$.
6. Utilize várias funções.
7. Faça comentários.








