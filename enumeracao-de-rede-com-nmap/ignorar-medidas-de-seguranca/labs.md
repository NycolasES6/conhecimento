# Labs
]
# Fácil

sudo nmap <ip> -sV -Pn

## Médio

sudo nmap <ip> -sSU -p 53 --script dns-nsid

## Hard

nc <ip> -nv -p 53 50000
