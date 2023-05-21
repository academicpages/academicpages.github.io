# Trabalhos de Cálculo Numérico (Terceiro)

### Atenção

O trabalho deverá ser entregue em arquivo pdf. Os códigos utilizados deverão ser encaminhados (encaminhar somente arquivos .jl). Arquivos do notebook Jupyter não serão aceitos. Um único membro do grupo deverá encaminhar o trabalho (Não há necessidade dos outros membros do grupo encaminharem algo). Este encaminhamento deverá ser feito pelo Google Classroom em um formulário que será disponibilizado na época do envio. Lembrem de colocar o nome de cada membro do grupo tanto no trabalho (arquivo pdf) quanto nos códigos que forem enviados. O formulário aceitará somente um arquivo. Logo, vocês devem compactar os arquivos a serem enviados e enviar o arquivo compactado (zip ou winrar).


#### Entregar até o dia 05/06/2023 (Essa data não será prorrogada!!)

___________________________________________

# Sobre os trabalhos

Estudar o método proposto neste trabalho. Escrever um trabalho que apresente estudos do ponto de vista teórico e computacional. Cada grupo receberá um método para resolver uma equação diferencial. No trabalho, cada grupo deverá comparar os resultados numéricos obtidos pelo método estudado com o Método de Euler, Taylor de  Segunda Ordem e Método do Trapézio. Essa comparação deverá ser realizada por meio do erro entre a solução aproximada e a solução exata da equação diferencial. Cada grupo deverá escolher uma equação diferncial apropriada para os testes. Para os testes use gráficos e tabelas. Escrever uma análise dos resultados comparando os métodos. 

___________________________________________

### Avaliação do Trabalho

O trabalho será avaliado considerando:

a) Sua organização;
b) Coerência e coesão do texto.
c) Profundidade da abordagem do tema (Matemática e Computacional);
d) Qualidade e quantidade dos experimentos numéricos desenvolvidos e apresentados;
e) Informações corretas apresentadas;
f) Pertinência das referências apresentadas.



________________________________________________

# Trabalhos

## Trabalho 01

#### Grupo: Bruna e Poliana 
Tema: Método de Simpson

______________________________

## Trabalho 2

#### Grupo: Maria Aparecida, Samuel Oliveira e Heitor
Tema: Método de Adams-Moulton


______________________________


## Trabalho 3
#### Grupo: Ana Clara e Murilo
Tema: Método de Nystrom


______________________________


## Trabalho 04

#### Grupo: Naiara, Priscila e Aline
Tema: Método de Adams-Bashforth


______________________________


## Trabalho 05

#### Grupo: Ana Caroline, Arthur e Stefane
Tema: Método de Heun


______________________________


## Trabalho 06

#### Grupo: Davi, Péricles e Samuel Carvalho
Tema: Método de Runge-Kutta de Quarta Ordem dado por
$$y_{n+1} - y_n = \frac{h}{6}[k_1+2(k_2+k_3)+k_4],$$
onde $k_1 = f(x_n,y_n)$, $k_2=f(x_n+0.5h,y_n+0.5hk_1)$, $k_3=f(x_n+0.5h,y_n+0.5hk_2)$ e $k_4=f(x_n+h,y_n+hk_3)$.

______________________________


## Trabalho 07

#### Grupo: Thiago, Guilherme e James
Tema: Método de Runge-Kutta de Quarta Ordem dado por
$$y_{n+1}-y_n=\frac{h}{8}[k_1+3(k_2+k_3)+k_4],$$ onde $k_1=f(x_n,y_n)$, $k_2=f(x_n+h/3,y_n+hk_1/3)$, $k_3 = f(x_n+2h/3,y_n-hk_1/3+hk_2)$ e $k_4=f(x_n+h,y_n+hk_1-hk_2+hk_3)$.

______________________________


## Trabalho 08

####  Grupo: Taíde, Gabriela Jade e Viviane

Tema: Estudar o seguinte método:
$$y_{i+1} = y_i+\frac{h}{2}\Big[ f(t_i,y_i)+f(t_{i+1},y_i+h f(t_i,y_i)\Big]$$









