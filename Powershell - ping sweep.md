#powershell #Windows 
# Powershell - ping sweep

```powershell
param($p1)

if(!$p1){
	Write-Output "Exemplo de uso: \.script.ps1 192.168.0"
}else{
	foreach ($ip in 1..254){
		try{
			$resp = ping -n 1 "$p1.$ip" | Select-String "bytes=32"
			$resp.Line.split(' ')[2] -replace ":",""
		}catch{}
	}
}
```

`if(!$p1)` - Testa se a variável **$p1** foi declarada

`$resp.Line.split(' ')[2]` - Divide a string em partes usando o character **" "**, e seleciona a terceira coluna.

`... -replace ":",""` - Pega a string e troca os characteres **" "** por *""*