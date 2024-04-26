# Enumeração de banco de dados SQL

Por padrão, o MSSQL usa portas `TCP/1433`e `UDP/1434`, e o [[MySQL]] usa `TCP/3306`. Porém, quando o[[ MSSQL]] opera em modo "oculto", ele utiliza a porta `TCP/2433`. Podemos usar a opção do [[Nmap]] de scripts padrão `-sC` para enumerar serviços de banco de dados em um sistema de destino:

## Agarrando banner

```shell
NycolasES6@htb[/htb]$ nmap -Pn -sV -sC -p1433 10.10.10.125

Host discovery disabled (-Pn). All addresses will be marked 'up', and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-26 02:09 BST
Nmap scan report for 10.10.10.125
Host is up (0.0099s latency).

PORT     STATE SERVICE  VERSION
1433/tcp open  ms-sql-s Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-ntlm-info: 
|   Target_Name: HTB
|   NetBIOS_Domain_Name: HTB
|   NetBIOS_Computer_Name: mssql-test
|   DNS_Domain_Name: HTB.LOCAL
|   DNS_Computer_Name: mssql-test.HTB.LOCAL
|   DNS_Tree_Name: HTB.LOCAL
|_  Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2021-08-26T01:04:36
|_Not valid after:  2051-08-26T01:04:36
|_ssl-date: 2021-08-26T01:11:58+00:00; +2m05s from scanner time.

Host script results:
|_clock-skew: mean: 2m04s, deviation: 0s, median: 2m04s
| ms-sql-info: 
|   10.10.10.125:1433: 
|     Version: 
|       name: Microsoft SQL Server 2017 RTM
|       number: 14.00.1000.00
|       Product: Microsoft SQL Server 2017
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
```

A varredura do Nmap revela informações essenciais sobre o alvo, como a versão e o nome do host, que podemos usar para identificar configurações incorretas comuns, ataques específicos ou vulnerabilidades conhecidas. Vamos explorar algumas configurações incorretas comuns e ataques específicos de protocolo.












































