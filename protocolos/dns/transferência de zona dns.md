#protocolo #redes 

# Transferência de zona DNS

Uma zona DNS é uma parte do namespace [[DNS]] gerenciada por uma organização ou administrador específico. Como o DNS compreende múltiplas zonas DNS, os servidores DNS utilizam transferências de zona DNS para copiar uma parte do seu banco de dados para outro servidor DNS. A menos que um servidor DNS esteja configurado corretamente (limitando quais IPs podem realizar uma transferência de zona DNS), qualquer pessoa pode solicitar a um servidor DNS uma cópia das informações de sua zona, pois as transferências de zona DNS não exigem nenhuma autenticação. Além disso, o serviço DNS geralmente é executado em uma porta UDP; entretanto, ao realizar a transferência de zona DNS, ele usa uma porta TCP para transmissão confiável de dados.

Um invasor pode aproveitar essa vulnerabilidade de transferência de zona DNS para aprender mais sobre o namespace DNS da organização alvo, aumentando a superfície de ataque. Para exploração, podemos usar o utilitário `dig` com opção `AXFR` de tipo de consulta DNS para despejar todos os namespaces DNS de um servidor DNS vulnerável:

### DIG - Transferência de Zona AXFR

```sh
NycolasES6@htb[/htb] dig AXFR @ns1.inlanefreight.htb inlanefreight.htb

; <<>> DiG 9.11.5-P1-1-Debian <<>> axfr inlanefrieght.htb @10.129.110.213
;; global options: +cmd
inlanefrieght.htb.         604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
inlanefrieght.htb.         604800  IN      AAAA    ::1
inlanefrieght.htb.         604800  IN      NS      localhost.
inlanefrieght.htb.         604800  IN      A       10.129.110.22
admin.inlanefrieght.htb.   604800  IN      A       10.129.110.21
hr.inlanefrieght.htb.      604800  IN      A       10.129.110.25
support.inlanefrieght.htb. 604800  IN      A       10.129.110.28
inlanefrieght.htb.         604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
;; Query time: 28 msec
;; SERVER: 10.129.110.213#53(10.129.110.213)
;; WHEN: Mon Oct 11 17:20:13 EDT 2020
;; XFR size: 8 records (messages 1, bytes 289)
```

Ferramentas como [o Fierce](https://github.com/mschwager/fierce) também podem ser usadas para enumerar todos os servidores DNS do domínio raiz e procurar uma transferência de zona DNS:

```sh
NycolasES6@htb[/htb]$ fierce --domain zonetransfer.me
```





