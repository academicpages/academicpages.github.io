---
title: "Usando Ansible para instalar pacotes do Samba e Python para validar tudo."
collection: teaching
permalink: /projects/2020-samba-project
date: 2020-07-01
location: "Brasil"
---

O repositório/projeto foi criado para aprender e estudar mais sobre IaC, e processos de testes automatizado.

## Obejtivo: ##
Utilizar Ansible para instalar pacotes do Samba e Python para validar/Testar tudo.

## Pré requisitos:

```bash
$ dpkg -l | grep --color "vagrant\|virtualbox\|python3-pip\|ansible"
ansible                                    2.9.6
python3-pip                                20.0
vagrant                                    2.2
virtualbox                                 6.1
```

**Python libs**
```python
$ pip3 freeze | grep --color "test\|infra"
pytest==5.4.3
testinfra==5.2.1
```

Neste caso rodei em uma máquina Ubuntu versão 20.

## O Playbook


|Playbook|Descrição
|-|-
samba.yml|Instala, inicia o serviço e executa o script de testes em Python.

## O script em Python

|Script|Descrição|
|-|-
|test_infra.py|Checa se os pacotes do Samba está instalado e se os serviços estão rodando.

## Como rodar o Playbook? ##

```bash
$ ansible-playbook -i inventory samba.yml
```
**Observação:** Caso necessário acrescentar o parâmetro **--ask-pass** para adequar a senha do SSH.

<a class="download-button" href="https://github.com/piholiveira/samba-with-ansible-and-python" target="blank">Github Repository</a>

## Referências

- [philpep-testinfra-python](https://github.com/philpep/testinfra)
- [doc-ansible](https://docs.ansible.com/ansible/latest/index.html)
- [doc-vagrant](https://www.vagrantup.com/docs/)
- [Ainda precisamos falar sobre teste de infraestrutura - Rafael Gomes](https://www.youtube.com/watch?v=ZVHlKWLEyhE&list=PLKo-modECX-ZdlHkvkHGkFYgb3wwt6ssl&index=24&t=1524s)
