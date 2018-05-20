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
    * Download: [http://www.oracle.com/technetwork/pt/java/javase/downloads/index.html](http://www.oracle.com/technetwork/pt/java/javase/downloads/index.html)
* Maven
  * 3.5.3 ou supeior
    * Download: [https://maven.apache.org/download.cgi](https://maven.apache.org/download.cgi)
    Como Instalar:
      * [Windows](https://www.mkyong.com/maven/how-to-install-maven-in-windows/)
      * [Linux](https://www.mkyong.com/maven/how-to-install-maven-in-ubuntu/)
* Git
  * Download: [https://git-scm.com/downloads](https://git-scm.com/downloads)
* Eclipse
  * Download: [https://www.eclipse.org/downloads/](https://www.eclipse.org/downloads/)


## Repositório do GIT

A OPLA-Tool possui um repositório utilizando o recurso de organização
* [https://github.com/OPLA-Tool-UEM](https://github.com/OPLA-Tool-UEM)

* Time de desenvolvimento
  * Fernando S. Godóy
  * João Choma
  * Pedro Barbiero


* Versão em desenvolvimento: 
  * Responsável: Fernando Godóy
  * [Repositório](https://github.com/OPLA-Tool-UEM/OPLA-Tool)
  * Branchs:
    * Master: Branch estável 
      * Aluno(s): Marcelo
    * Develop: Branch de desenvolvimento
    * Documentation: Branch para desenvolvimento do documento de requisitos
      * Aluno(s): Diego Fernandes, Fernando Godóy, Mamoru Massago, Thiago Madrigar
    * Nova Interface: Branch criado para desenvolvimento da versão contendo nova interface
      * Aluno(s): Fernando Godóy
    * NSGA-III-Jmetal-5: Branch criado para implementação da nova versão do algoritmo NSGA
      * Aluno(s): Pedro Barbiero

* Versão Estável
  * Responsável: João Choma
  * [Repositório](https://github.com/OPLA-Tool-UEM/opla-tool-choma-version2.0)


## Contribuir como desenvolvedor

Efetue o clone do repositório: 
  * git clone https://github.com/OPLA-Tool-UEM/OPLA-Tool
Crie um branch local
  * git checkout -b nome_do_seu_branch
Preparar para importar em sua IDE
  * mvn eclipse:clean
Importar no eclipse como projeto maven
  *  Arquivo > Importar > Maven Project> Existent Maven 
Efetuar comite localmente
  * git commit -m "Descrição da alteração efetuada"
Submeter ao repositório remoto
  * git push origin nome_do_seu_branch
Criar Pull Request para branch develop
