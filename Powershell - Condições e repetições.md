#Windows #powershell 
# Powershell - Condições e repetições

## if

| Condição | Explicação       |
| -------- | ---------------- |
| -ge      | Maior ou igual à |
| -gt      | Maior quê        |

```powershell
$idade = Read-Host "Qual a sua idade: "

if ($idade -ge "18"){
	Write-Output "Com $idade anos, você pode dirigir."
}else{
    Write-Output "Com $idade anos, você não pode dirigir."
}
```

## foreach

```powershell
foreach ($var in 1..10){
	echo "192.168.0.$var"
}
```

## Pingando em toda a rede

```powershell
param($rede)

if(!$rede){
	Write-Output "Exemplo de uso: .\script 192.168.0"
}else{
    foreach ($ip in 1..254){
        Write-Output "$rede.$ip"

        ping -n 1 "$rede.$ip" | Select-String "bytes=32"
    }
}
```
























