---
permalink: /markdown/
title: "Guia de Instalação"
author_profile: true
redirect_from: 
  - /md/
  - /markdown.html
---

## Requisitos

* Java 
  * 1.8 ou superior
    * Download: 
      * [http://www.oracle.com/technetwork/pt/java/javase/downloads/index.html](http://www.oracle.com/technetwork/pt/java/javase/downloads/index.html)
* Maven
  * 3.5.3 ou supeior
    * Download: 
      * [https://maven.apache.org/download.cgi](https://maven.apache.org/download.cgi)
    * Como Instalar:
      * [Windows](https://www.mkyong.com/maven/how-to-install-maven-in-windows/)
      * [Linux](https://www.mkyong.com/maven/how-to-install-maven-in-ubuntu/)
* Git
  * Download: 
    * [https://git-scm.com/downloads](https://git-scm.com/downloads)
* Eclipse
  * Download: 
    * [https://www.eclipse.org/downloads/](https://www.eclipse.org/downloads/)


## Repositório do GIT

Organização - [https://github.com/OPLA-Tool-UEM](https://github.com/OPLA-Tool-UEM)

* Time de Desenvolvimento
  * **Fernando S. Godóy**
  * **João Choma**
  * **Pedro Barbiero**

* Versão 2.0
  * Repositório: [https://github.com/OPLA-Tool-UEM/opla-tool-choma-version2.0](https://github.com/OPLA-Tool-UEM/opla-tool-choma-version2.0)
  * Responsável: **João Choma**

* Versão em Desenvolvimento: 
  * Repositório: [https://github.com/OPLA-Tool-UEM/OPLA-Tool](https://github.com/OPLA-Tool-UEM/OPLA-Tool)
  * Responsável: **Fernando Godóy**
  * Branchs:
    * Master: Versão 1.0 
      * Aluno(s)
        * **Marcelo**
    * Develop: Branch de desenvolvimento
      * Aluno(s) 
        * **Fernando Godóy**
    * Documentation: Branch para desenvolvimento do documento de requisitos
      * Aluno(s)
        * **Diego Fernandes**
        * **Fernando Godóy**
        * **Mamoru Massago**
        * **Thiago Madrigar**
    * Nova Interface: Branch criado para desenvolvimento da versão contendo nova interface
      * Aluno(s)
        * **Fernando Godóy**
    * NSGAIII-Jmetal5: Branch criado para implementação da nova versão do algoritmo NSGA
      * Aluno(s)
        * **Pedro Barbiero**

## Modo Desenvolvedor

Clonar repositório: 
  ``` 
   git clone https://github.com/OPLA-Tool-UEM/OPLA-Tool
  ```

Criar branch local
  ```
   git checkout -b nome_do_seu_branch
  ```

Preparar importação para eclipse
  ``` 
   mvn eclipse:clean
  ```

Importar como projeto maven
  >  Arquivo > Importar > Maven Project> Existing Maven Project

Efetuar commit local
 ```
  git commit -m "Descrição da alteração efetuada"
 ```

Submeter para repositório remoto
  ```
   git push origin nome_do_seu_branch
  ```

Criar Pull Request para branch develop

## Modo Usuário

Clonar do repositório: 
  ``` 
   git clone https://github.com/OPLA-Tool-UEM/OPLA-Tool
  ```

Instalar dependências:

Executar arquivo buildDeps.sh localizado no diretório opla-architecture
*  Linux
 ```
  sh buildDeps.sh
 ```
* Windows
  * Abrir aquivo e copiar linha a linha para prompt de comando 

Build do Projeto
  
   Dentro do diretório opla-archicture
  ```
   mvn clean install
  ```
  
  Dentro do diretório opla-patterns
  ```
   mvn clean install
  ```
  
  Dentro do diretório opla-core
  ```
   mvn clean install
  ```
  
  Dentro do diretório opla-tool
  ```
   mvn clean install
  ```

Executar
  
  Dentro do diretório opla-tool
  ```
    java -jar target/opla-tool-0.0.1-jar-with-dependencies.jar
  ```