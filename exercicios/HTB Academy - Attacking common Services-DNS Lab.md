#exercicio #protocolo #redes 

# HTB Academy: Attacking Common Services - DNS Lab

**Question:** Encontre todos os registros DNS disponíveis para o domínio "inlanefreight.htb" no servidor de nomes de destino e envie o sinalizador encontrado como um registro DNS como resposta.

**ip:** 10.129.203.6

**host:** inlanefreight.htb

### Adicionar ao arquivo de host

```sh
sudo vim /etc/hosts

10.129.203.6 ns1.inlanefreight.htb

```

### Adicionando ao resolvers

```sh
cd subbrute
echo "ns1.inlanefreight.htb" > ./resolvers.txt
```

### Enumeração de subdomínios

```sh
sudo ./subbrute.py inlanefreight.htb -s ./names.txt -r ./resolvers.txt

# hr.inlanefreight.htb
```

### Transferência de zona

```sh
dig AXFR @ns1.inlanefreight.htb hr.inlanefreight.htb
```



























