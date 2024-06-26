Um dos servidores web mais utilizados e difundidos, além do IIS e do Nginx, é o Apache.

Para um servidor web Apache, podemos usar módulos apropriados, que podem criptografar a comunicação entre o navegador e o servidor web (mod_ssl), usar como servidor proxy (mod_proxy) ou realizar manipulações complexas de dados de cabeçalho HTTP (mod_headers) e URLs (mod_rewrite ).

### Instalando o Apache

```bash
sudo apt install apache2 -y
```

Depois de iniciá-lo, podemos navegar usando nosso navegador até a página padrão (http://localhost).

![[apache-default.webp]]

Esta é a página padrão após a instalação e serve para confirmar se o servidor web está funcionando corretamente.

## CURL

`cURL`é uma ferramenta que nos permite transferir arquivos do shell por meio de protocolos como `HTTP`, `HTTPS`, `FTP`, `SFTP`, `FTPS`ou `SCP`.Esta ferramenta dá-nos a possibilidade de controlar e testar sites remotamente

```bash
curl http://localhost

#<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
#<html xmlns="http://www.w3.org/1999/xhtml">
#  <!--
#    Modified from the Debian original for Ubuntu
#    Last updated: 2016-11-16
#    See: https://launchpad.net/bugs/1288690
#  -->
#  <head>
#    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
#    <title>Apache2 Ubuntu Default Page: It works</title>
#    <style type="text/css" media="screen">
#...SNIP...
```

Na tag de título, podemos ver que é o mesmo texto do nosso navegador. Isso nos permite inspecionar o código-fonte do site e obter informações dele.

## Wget

Uma alternativa ao curl é a ferramenta `wget`. Com esta ferramenta podemos baixar arquivos de servidores FTP ou HTTP diretamente do terminal, e ela serve como um bom gerenciador de downloads.

Se usarmos o wget da mesma forma, a diferença para o curl é que o conteúdo do site é baixado e armazenado localmente, conforme mostrado no exemplo a seguir.

```bash
wget http://localhost

#--2020-05-15 17:43:52--  http://localhost/
#Resolving localhost (localhost)... 127.0.0.1
#Connecting to localhost (localhost)|127.0.0.1|:80... connected.
#HTTP request sent, awaiting response... 200 OK
#Length: 10918 (11K) [text/html]
#Saving to: 'index.html'

#index.html                 100%[=======================================>]  10,66K  --.-KB/s   # in 0s      
#
#2020-05-15 17:43:52 (33,0 MB/s) - ‘index.html’ saved [10918/10918]
```

## Python3

Outra opção que é frequentemente usada quando se trata de transferência de dados é o uso do Python 3. Neste caso, o diretório raiz do servidor web é onde o comando é executado para iniciar o servidor.

Agora, vamos iniciar o servidor web Python 3 e ver se podemos acessá-lo usando o navegador.

```bash
python3 -m http.server

#Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

![[python3-browser.webp]]

Podemos ver quais solicitações foram feitas se olharmos agora para os eventos do nosso servidor web Python 3.

```bash
python3 -m http.server

#Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
#127.0.0.1 - - [15/May/2020 17:56:29] "GET /readme.html HTTP/1.1" 200 -
#127.0.0.1 - - [15/May/2020 17:56:29] "GET /wp-admin/css/install.css?ver=20100228 HTTP/1.1" 200 -
#127.0.0.1 - - [15/May/2020 17:56:29] "GET /wp-admin/images/wordpress-logo.png HTTP/1.1" 200 -
#127.0.0.1 - - [15/May/2020 17:56:29] "GET /wp-admin/images/wordpress-logo.svg?ver=20131107 HTTP/1.1" 200 -
```






















































