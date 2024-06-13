#Windows #powershell 
# Powershell - Introdução

## Escrevendo na tela

```powershell
Write-Output "Desec"
```

```powershell
Write-Host "Desec"
```

```powershell
echo "Desec"
```
*Não é recomendado*

## Algumas variáveis

```powershell
Write-Output " Meu diretório atual é: $(pwd)"
```
**$(pwd)** - Imprime o diretório atual

```powershell
Write-Output "Meu usuário atual é: $(whoami)"
```
**$(whoami)** - Imprime o usuário atual

## Declarando variáveis

```powershell
$ip = "192.168.0.10"
Write-Output "Varrendo o i: $ip"
```
Quando formos usar a variável, temos de usar o **$** na frente, para dizer que é uma variável.

## Input

```powershell
$ip = Read-Host "Digite o IP: "
Write-Output "Varrendo o ip: $ip"
```

## Fazendo um ping

```powershell
$ip = Read-Host "Digite o ip: "

ping $ip
```

## Filtrando conteúdo

```powershell
$ip = Read-Host "Digite o ip da busca: "

Write-Output "Executando Ping no host $ip"

ping -n 7 $ip | Select-String "bytes=32"
```

`ping -n 7 $ip | Select-String "bytes=32"` - Filtra a saída do comando ``ping`` e retorna somente as linhas que contém "bytes=32"

## Parâmetros

```powershell
param($ip, $filtro)

Write-Output "Efetuando ping no host: $ip"

ping -n 5 $ip | Select-String $filtro
```

## if com parâmetros

```powershell
param($ip)

if(!$ip){
    Write-Output "Exemplo de uso: .\script.ps1 <ip>"
}else{
    Write-Output "Efetuando ping no host: $ip"

    ping -n 2 $ip | Select-String "bytes=32"
}
```










