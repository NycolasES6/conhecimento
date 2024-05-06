#protocolo #redes 

# Aquisições de domínio e enumeração de subdomínios DNS

`Domain takeover`está registrando um nome de domínio inexistente para obter controle sobre outro domínio. Se os invasores encontrarem um domínio expirado, eles poderão reivindicá-lo para realizar ataques adicionais, como hospedar conteúdo malicioso em um site ou enviar um e-mail de phishing aproveitando o domínio reivindicado.

A aquisição de domínio também é possível com subdomínios chamados `subdomain takeover`. O registro de nome canônico (`CNAME`) de um DNS é usado para mapear domínios diferentes para um domínio pai. Muitas organizações usam serviços de terceiros como AWS, GitHub, Akamai, Fastly e outras redes de entrega de conteúdo (CDNs) para hospedar seu conteúdo. Nesse caso, costumam criar um subdomínio e fazê-lo apontar para esses serviços. Por exemplo,

```sh
sub.target.com.   60   IN   CNAME   anotherdomain.com
```

O nome de domínio (por exemplo, **sub.target.com**) usa um registro **CNAME** para outro domínio (por exemplo, **anotherdomain.com**). Suponha que **anotherdomain.com** expire e esteja disponível para qualquer pessoa reivindicar o domínio, já que o servidor DNS do **target.com** possui o registro **CNAME**. Nesse caso, qualquer pessoa que registrar anotherdomain.com terá controle total sobre **sub.target.com** até que o registro DNS seja atualizado.

## Enumeração de subdomínio

Antes de realizar uma aquisição de subdomínio, devemos enumerar subdomínios para um domínio de destino usando ferramentas como [Subfinder](https://github.com/projectdiscovery/subfinder) . Esta ferramenta pode extrair subdomínios de fontes abertas como [DNSdumpster](https://dnsdumpster.com/) . Outras ferramentas como [Sublist3r](https://github.com/aboul3la/Sublist3r) também podem ser usadas para subdomínios de força bruta, fornecendo uma lista de palavras pré-geradas:

```sh
NycolasES6@htb[/htb]$ ./subfinder -d inlanefreight.com -v       
                                                                       
        _     __ _         _                                           
____  _| |__ / _(_)_ _  __| |___ _ _          
(_-< || | '_ \  _| | ' \/ _  / -_) '_|                 
/__/\_,_|_.__/_| |_|_||_\__,_\___|_| v2.4.5                                                                                                                                                                                                                                                 
                projectdiscovery.io                    
                                                                       
[WRN] Use with caution. You are responsible for your actions
[WRN] Developers assume no liability and are not responsible for any misuse or damage.
[WRN] By using subfinder, you also agree to the terms of the APIs used. 
                                   
[INF] Enumerating subdomains for inlanefreight.com
[alienvault] www.inlanefreight.com
[dnsdumpster] ns1.inlanefreight.com
[dnsdumpster] ns2.inlanefreight.com
...snip...
[bufferover] Source took 2.193235338s for enumeration
ns2.inlanefreight.com
www.inlanefreight.com
ns1.inlanefreight.com
support.inlanefreight.com
[INF] Found 4 subdomains for inlanefreight.com in 20 seconds 11 milliseconds
```

Uma excelente alternativa é uma ferramenta chamada [Subbrute](https://github.com/TheRook/subbrute) . Esta ferramenta nos permite usar resolvedores autodefinidos e realizar ataques puros de força bruta de DNS durante testes de penetração internos em hosts que não têm acesso à Internet.

## Subbruto

```sh
NycolasES6@htb[/htb]$ git clone https://github.com/TheRook/subbrute.git >> /dev/null 2>&1
NycolasES6@htb[/htb]$ cd subbrute
NycolasES6@htb[/htb]$ echo "ns1.inlanefreight.com" > ./resolvers.txt
NycolasES6@htb[/htb]$ ./subbrute inlanefreight.com -s ./names.txt -r ./resolvers.txt

Warning: Fewer than 16 resolvers per process, consider adding more nameservers to resolvers.txt.
inlanefreight.com
ns2.inlanefreight.com
www.inlanefreight.com
ms1.inlanefreight.com
support.inlanefreight.com

<SNIP>
```

Às vezes, as configurações físicas internas são mal protegidas, o que podemos explorar para fazer upload de nossas ferramentas a partir de um pendrive. Outro cenário seria chegarmos a um host interno por meio de pivotamento e querermos trabalhar a partir daí. Claro que existem outras alternativas, mas não custa nada conhecer caminhos e possibilidades alternativas.

A ferramenta encontrou quatro subdomínios associados a `inlanefreight.com`. Usando o comando `nslookup` ou `host`, podemos enumerar os registros `CNAME` desses subdomínios.

```shell-session
NycolasES6@htb[/htb]# host support.inlanefreight.com

support.inlanefreight.com is an alias for inlanefreight.s3.amazonaws.com
```

O subdomínio `support`possui um registro de alias apontando para um bucket AWS S3.No entanto, o URL `https://support.inlanefreight.com` mostra um erro `NoSuchBucket` indicando que o subdomínio é potencialmente vulnerável a um controle de subdomínio. Agora, podemos assumir o controle do subdomínio criando um bucket AWS S3 com o mesmo nome de subdomínio.

![[s3.webp]]

O repositório [can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz) também é uma excelente referência para uma vulnerabilidade de controle de subdomínio. Mostra se os serviços alvo são vulneráveis ​​a uma aquisição de subdomínio e fornece orientações sobre a avaliação da vulnerabilidade.




