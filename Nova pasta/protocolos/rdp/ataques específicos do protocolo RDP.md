#protocolo #redes #hacking 

# Ataques específicos do protocolo RDP

Vamos imaginar que obtivemos acesso a uma máquina e temos uma conta com privilégios de administrador local. Se um usuário estiver conectado via RDP à nossa máquina comprometida, podemos sequestrar a sessão de área de trabalho remota do usuário para aumentar nossos privilégios e personificar a conta. Em um ambiente do Active Directory, isso pode resultar na assunção de uma conta de administrador de domínio ou na promoção de nosso acesso dentro do domínio.

## Sequestro de sessão RDP

Conforme mostrado no exemplo abaixo, estamos logados como o usuário **juurena**(UserID = 2) que possui privilégios de Administrador. Nosso objetivo é sequestrar o usuário **lewen**(UserID = 4), que também está logado via RDP.

![[Pasted image 20240502091208.jpg]]

Para representar com sucesso um usuário sem sua senha, precisamos ter privilégios de sistema e usar o binário [tscon.exe](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/tscon) da Microsoft que permite aos usuários se conectarem a outra sessão de desktop. Funciona especificando qual `SESSION ID`( `4` para a sessão de `lewen` em nosso exemplo) gostaríamos de conectar a qual nome de sessão ( `rdp-tcp#13`, que é nossa sessão atual). Assim, por exemplo, o seguinte comando abrirá um novo console conforme especificado `SESSION_ID` em nossa sessão RDP atual:

```cmd
C:\htb> tscon #{TARGET_SESSION_ID} /dest:#{OUR_SESSION_NAME}
```

Se tivermos privilégios de administrador local, podemos usar vários métodos para obter privilégios de SYSTEM, como`` PsExec`` ou`` Mimikatz``. Um truque simples é criar um serviço do Windows que, por padrão, será executado como Sistema Local e executará qualquer binário com privilégios de SYSTEM. Usaremos o binário ``Microsoft sc.exe``. Primeiro, especificamos o nome do serviço (``sessionhijack``) e o ``binpath``, que é o comando que queremos executar. Assim que executarmos o comando a seguir, um serviço chamado ``sessionhijack`` será criado.

```cmd
C:\htb> query user

 USERNAME              SESSIONNAME        ID  STATE   IDLE TIME  LOGON TIME
>juurena               rdp-tcp#13          1  Active          7  8/25/2021 1:23 AM
 lewen                 rdp-tcp#14          2  Active          *  8/25/2021 1:28 AM

C:\htb> sc.exe create sessionhijack binpath= "cmd.exe /k tscon 2 /dest:rdp-tcp#13"

[SC] CreateService SUCCESS
```

![[Pasted image 20240502094330.jpg]]

Para executar o comando, podemos iniciar o serviço `sessionhijack`:

```cmd
C:\htb> net start sessionhijack
```

Assim que o serviço for iniciado, um novo terminal com a sessão do usuário `lewen` aparecerá. Com esta nova conta, podemos tentar descobrir que tipo de privilégios ela possui na rede, e talvez tenhamos sorte, e o usuário seja membro do grupo Help Desk com direitos de administrador para muitos hosts ou até mesmo um Administrador de Domínio .

![[Pasted image 20240502094433.jpg]]

**Nota: Este método não funciona mais no Server 2019.**




