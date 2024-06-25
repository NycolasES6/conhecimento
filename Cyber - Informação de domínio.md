# Cyber - Informação de domínio

As informações de domínio são um componente central de qualquer teste de penetração e não se trata apenas dos subdomínios, mas de toda a presença na Internet.

Este tipo de informação é coletada passivamente, sem verificações diretas e ativas.
Ou seja, permanecemos ocultos e navegamos como “clientes” ou “visitantes” para evitar conexões diretas com a empresa que possam nos expor.

Prestamos atenção ao que `we see`e `we do not see`. Vemos os serviços, mas não sua funcionalidade. No entanto, os serviços estão vinculados a certos aspectos técnicos necessários à prestação de um serviço.

## Presença online

Depois de termos um conhecimento básico da empresa e dos seus serviços, podemos ter uma primeira impressão da sua presença na Internet.

O primeiro ponto de presença na Internet pode ser o `SSL certificate`site principal da empresa que podemos examinar.
Muitas vezes, esse certificado inclui mais do que apenas um subdomínio, e isso significa que o certificado é usado para vários domínios, e estes provavelmente ainda estão ativos.

![[Pasted image 20240625093954.png]]

Outra fonte para encontrar mais subdomínios é [crt.sh](https://crt.sh/) . Esta fonte são logs [de transparência de certificados](https://en.wikipedia.org/wiki/Certificate_Transparency) . A Transparência de Certificados é um processo que visa permitir a verificação de certificados digitais emitidos para conexões criptografadas à Internet.

![[DomInfo-2.webp]]

## Transparência do certificado

```bash
curl -s https://crt.sh/\?q\=inlanefreight.com\&output\=json | jq .

[
  {
    "issuer_ca_id": 23451835427,
    "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
    "common_name": "matomo.inlanefreight.com",
    "name_value": "matomo.inlanefreight.com",
    "id": 50815783237226155,
    "entry_timestamp": "2021-08-21T06:00:17.173",
    "not_before": "2021-08-21T05:00:16",
    "not_after": "2021-11-19T05:00:15",
    "serial_number": "03abe9017d6de5eda90"
  },
  {
    "issuer_ca_id": 6864563267,
    "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
    "common_name": "matomo.inlanefreight.com",
    "name_value": "matomo.inlanefreight.com",
    "id": 5081529377,
    "entry_timestamp": "2021-08-21T06:00:16.932",
    "not_before": "2021-08-21T05:00:16",
    "not_after": "2021-11-19T05:00:15",
    "serial_number": "03abe90104e271c98a90"
  },
  {
    "issuer_ca_id": 113123452,
    "issuer_name": "C=US, O=Let's Encrypt, CN=R3",
    "common_name": "smartfactory.inlanefreight.com",
    "name_value": "smartfactory.inlanefreight.com",
    "id": 4941235512141012357,
    "entry_timestamp": "2021-07-27T00:32:48.071",
    "not_before": "2021-07-26T23:32:47",
    "not_after": "2021-10-24T23:32:45",
    "serial_number": "044bac5fcc4d59329ecbbe9043dd9d5d0878"
  },
  { ... SNIP ...
]
```

Se necessário, também podemos filtrá-los por subdomínios exclusivos.

```bash
curl -s https://crt.sh/\?q\=inlanefreight.com\&output\=json | jq . | grep name | cut -d":" -f2 | grep -v "CN=" | cut -d'"' -f2 | awk '{gsub(/\\n/,"\n");}1;' | sort -u

account.ttn.inlanefreight.com
blog.inlanefreight.com
bots.inlanefreight.com
console.ttn.inlanefreight.com
ct.inlanefreight.com
data.ttn.inlanefreight.com
*.inlanefreight.com
inlanefreight.com
integrations.ttn.inlanefreight.com
iot.inlanefreight.com
mails.inlanefreight.com
marina.inlanefreight.com
marina-live.inlanefreight.com
matomo.inlanefreight.com
next.inlanefreight.com
noc.ttn.inlanefreight.com
preview.inlanefreight.com
shop.inlanefreight.com
smartfactory.inlanefreight.com
ttn.inlanefreight.com
vx.inlanefreight.com
www.inlanefreight.com
```

A seguir, podemos identificar os hosts diretamente acessíveis pela Internet e não hospedados por provedores terceirizados. Isso ocorre porque não temos permissão para testar os hosts sem a permissão de fornecedores terceirizados.

### Servidores hospedados pela empresa

```bash
for i in $(cat subdomainlist);do host $i | grep "has address" | grep inlanefreight.com | cut -d" " -f1,4;done
```

Depois de vermos quais hosts podem ser investigados mais detalhadamente, podemos gerar uma lista de endereços IP com um pequeno ajuste no `cut`comando e executá-los `Shodan`.

O `Shodan` pesquisa na Internet portas TCP/IP abertas e filtra os sistemas de acordo com termos e critérios específicos. Por exemplo, portas HTTP ou HTTPS abertas e outras portas de servidor para `FTP`, `SSH`, `SNMP`, `Telnet`, `RTSP`ou `SIP`são pesquisadas.

Como resultado, podemos encontrar dispositivos e sistemas, como `surveillance cameras`,,,,, e , e vários componentes de rede `servers`.`smart home systems``industrial controllers``traffic lights``traffic controllers`

### Shodan - Lista de IPs

```bash
for i in $(cat subdomainlist);do host $i | grep "has address" | grep inlanefreight.com | cut -d" " -f4 >> ip-addresses.txt;done
```

```bash
for i in $(cat ip-addresses.txt);do shodan host $i;done
```

Lembramos o IP `10.129.127.22`( `matomo.inlanefreight.com`) para futuras investigações ativas que desejamos realizar. Agora podemos exibir todos os registros DNS disponíveis onde podemos encontrar mais hosts.
























































