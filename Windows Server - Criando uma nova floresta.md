# Windows Server - Criando uma nova floresta

## Promoção de domínio
Depois de instalarmos o AD irá aparecer irá aparecer uma **exclamação**, ele está pedindo para promovermos o server a um controlador de domínio. O assistente de instalação irá aparecer.

![[Pasted image 20240620140528.png]]

Aqui teremos 3 opções:

- Adicionar o controlador de domínio a um domínio existente.
- Adicionar um domínio novo a uma floresta.
- Adicionar uma floresta

Como não temos um domínio ou uma floresta, vamos criar uma nova floresta, colocaremos o nome como, **empresa.local**

Em redes locais, é preferível que usemos o sufixo **.local**

## Opções de controlador

![[Pasted image 20240620145421.png]]

o nível funcional diz respeito a retro compatibilidade do AD com outros servidores.

Em especificar recursos do controlador de domínio, caso ele seja o **DNS Server**, podemos marcar.

E a senha pode ser uma qualquer.

## Opções DNS

![[Pasted image 20240620145739.png]]

Como não temos esse serviço ainda, ele mostrará um  alerta dizendo que irá instalar o serviço DNS.

## Opções Adicionais

![[Pasted image 20240620150032.png]]

Podemos configurar um nome para o domínio do serviço NetBios, normalmente é o primeiro nome do nosso domínio, nesse caso **EMPRESA**

## Caminhos

![[Pasted image 20240620150813.png]]

É correto que selecionemos esses caminhos em outro disco, para deixar o AD com mais performance e usar de backup, caso o HD com o AD falhe.

## Examinar opções

![[Pasted image 20240620151219.png]]
 
Ele mostrará um resumo das configurações que serão aplicadas.

## Verificação de requisitos

![[Pasted image 20240620151410.png]]

Mostrará os requisitos necessários, caso a opção de instalar apareça, todos os requisitos foram cumpridos.















