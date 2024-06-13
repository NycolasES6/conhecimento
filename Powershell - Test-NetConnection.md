# Powershell - Test-NetConnection

## Comando Test-NetConnection

```powershell
Test-NetConnection google.com
```
Realiza um ping e retorna se teve sucesso

---

```powershell
Test-NetConnection google.com -TraceRoute
```
Agora ele faz o ping e traça a rota do nosso host até o servidor de destino

```powershell
Test-NetConnection google.com -TraceRoute -Hope 2
```
Vali limitar o TraceRoute á 2 roteadores

---

```powershell
Test-NetConnection google.com -Port 80
```
O port valida se uma porta TCP está aberta

![[Pasted image 20240613183225.png]]

---

```powershell
Test-NetConnection google.com -Port 80 -WarningAction SilentlyContinue
```
Coloca o alerta em modo silencioso (mostra menos informações)

```powershell
Test-NetConnection google.com -Port 80 -WarningAction SilentlyContinue -InformationLevel Quit
```
**-InformationLevel Quit** - Ele só vai informar se consegui ou não

![[Pasted image 20240613184010.png]]

## Usando no if

```powershell
if (Test-NetConnection google.com -Port 81 -WarningAction SilentlyContinue -InformationLevel Quiet){
	echo "Porta aberta"
}else{
	echo "Porta fechada"
}
```