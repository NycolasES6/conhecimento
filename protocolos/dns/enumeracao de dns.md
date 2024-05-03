#protocolo #hacking #enumeracao

# Enumeração de DNS

Podemos enumerar o [[dns]] com alguns programas, sendo o principal o [[nmap]]

O DNS contém informações interessantes para uma organização. Conforme discutido na seção Informações do Domínio no [módulo Footprinting](https://academy.hackthebox.com/course/preview/footprinting) , podemos entender como uma empresa opera e os serviços que ela fornece, bem como provedores de serviços terceirizados, como e-mails.

As opções Nmap `-sC`(scripts padrão) e `-sV`(verificação de versão) podem ser usadas para realizar a enumeração inicial nos servidores DNS de destino:

```sh
$ nmap -p53 -Pn -sV -sC 10.10.110.213

Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-29 03:47 EDT
Nmap scan report for 10.10.110.213
Host is up (0.017s latency).

PORT    STATE  SERVICE     VERSION
53/tcp  open   domain      ISC BIND 9.11.3-1ubuntu1.2 (Ubuntu Linux)
```
















