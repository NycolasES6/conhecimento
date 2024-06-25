# Windows Server - Adicionando um host ao domínio

## Configurações de rede

**Control Panel > Network and Internet > NetWork Conncetions**

Selecione sua interface de rede e clique em **Properties**
![[Pasted image 20240625160744.png]]

Então selecione **IPv4 > Properties**
![[Pasted image 20240625160952.png]]

Agora vamos definir as configurações de IP do host
![[Pasted image 20240625161057.png]]

O endereço IP tem que estar dentro da rede do servidor com o **AD**

E o servidor DNS tem de ser o endereço do servidor com o **AD**

## Testando conectividade

Vamos ao terminal e pingamos no  **SERVIDOR** a partir do **HOST**.

![[Pasted image 20240625161516.png]]

Para testarmos o serviço DNS, temos que pingar pelo nome do servidor.

![[Pasted image 20240625161825.png]]
## Ingressando no domínio

**Host:**

Em **Settings > System > About > System Protection**
![[Pasted image 20240625164529.png]]

Na janela que se abrir vá em **Computer Name > Change...**
![[Pasted image 20240625165004.png]]

- Mude o nome do computador - opcional
- Coloque o nome do domínio do **AD**

Ele irá pedir um usuário e senha - Pode ser qualquer um configurado no servidor **AD**

## Movendo usuários

**Servidor:**

Em **Active Directory Users and Computers**
![[Pasted image 20240625170244.png]]

Basta usar o comando **ctrl + x** para pegar um computador ou usuário e com o comando **ctrl + v** colocá-lo em outra pasta.

Ou apenas arraste-o com o mouse para outra pasta.





























































