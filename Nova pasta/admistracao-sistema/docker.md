# Docker

`docker run hello-world`

Nesse caso **hello-world** é uma imagemm que o docker baixou e gerou um container.

`docker ps`

Mostra todos os containers em execução

`docker ps -a`

Mostra todos os containers locais.

## ubuntu

Se amos rodar o ubuntu, provavelmente queremos acessar o terminal. Para isso temos que rodá-lo no modo interativo, i informar para o container que queremos no comunicar com o container de forma bidirecional

`docker run -it ubuntu bash`

 - `-it` - i: Rora no modo interativo, t: informa que queremos noc comunicar de forma bidirecional.
 - `bash` - Roda o bash ao iniciar o container.

## nginx

`docker run nginx`

Sobe um container com o nginx. Mas para podermos ter acesso, temos que publicar a porta, pois ele disponibiliza o nginx na porta 80 do container.

`docker run -p 8080:80 nginx`

 - `-p 8080:80` - Quando o container for publicado, ao acessar a porta 8080 do computador, será redirecionado paraa porta 80 do container.





