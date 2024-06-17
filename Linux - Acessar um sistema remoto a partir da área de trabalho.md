#Linux 
# Linux - Acessar um sistema remoto a partir da área de trabalho

Na área de trabalho GNOME, você acessa arquivos em outro computador na sua rede usando o aplicativo GNOME Files. Você deve ter uma conta de usuário no computador de destino, e o login remoto deve estar habilitado. O computador de destino pode ser chamado de servidor nesse contexto, e o computador que você está usando é o cliente.

## Habilitação do login remoto na área de trabalho

Para acessar um computador remoto usando o GNOME Files, você deve habilitar o login remoto no computador de destino. Nesse contexto o computador de destino é considerado um servidor porque fornece funcionalidade de acesso á máquina cliente.

Na área de trabalho GNOME, você habilita a funcionalidade de login remoto em GNOME Settings. Abra Settings no servidor remoto e clique em Sharing na coluna esquerda. no painel direito, defina Remote Login como ON.

![[Pasted image 20240617134103.png]]

## Login a partir da área de trabalho

Primeiro deve-se saber o endereço IP, em caso alternativo se o ambiente de rede tiver um servidor DNS, você poderá fazer login utilizando o hostname.

Para fazer login em um computador remoto, você deve saber seu endereço IP. Como alternativa, se o ambiente de rede tiver um servidor DNS, você poderá fazer login em um computador remoto usando seu nome de host. Um servidor DNS monitora os computadores na rede e converte endereços IP em nomes de host e vice-versa.

Para fazer login em um computador remoto a partir da área de trabalho GNOME, abra o aplicativo Files na máquina cliente. No painel esquerdo, selecione Other Locations. No campo Connect to Server, digite `ssh://` seguido pelo seu nome de usuário no computador remoto, a arroba (`@`) e o endereço IP ou nome de host do servidor no qual você deseja fazer login. Clique em Connect para fazer login.

![[Pasted image 20240617135149.png]]

Quando sua senha for solicitada, digite a senha da sua conta de usuário no servidor.

Se houver arquivos no computador remoto, eles serão exibidos na janela Files. Você pode usar os arquivos no computador remoto da mesma maneira que usa arquivos locais na máquina cliente.


