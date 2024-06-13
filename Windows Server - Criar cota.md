# Windows Server - Criar cota

Abrimos o **File Server Resource Manager**

Em **Quota management>Quota Management>Actions>Create Quota**

![[Pasted image 20240613155348.png]]

Nessa janela que se abre devemos especificar em qual local ficará a quota e seu tamanho em MB

![[Pasted image 20240613155421.png]]

Depois de terminarmos clicamos em **Create**

## Comandos de teste

```powershell

Invoke-Command -ComputerName WIN-Q3ULIUDB9L1 -ScriptBlock {
	fsutil file createnew C:\Users\Administrator\Documents\Data\file.txt 130
}


Invoke-Command -ComputerName WIN-Q3ULIUDB9L1 -ScriptBlock {
    fsutil file createnew C:\Users\Administrator\Documents\Data\file2.txt 120000000
}


Invoke-Command -ComputerName WIN-Q3ULIUDB9L1 -ScriptBlock {
    fsutil file createnew C:\Users\Administrator\Documents\Data\file3.txt 100000000
}


Invoke-Command -ComputerName WIN-Q3ULIUDB9L1 -ScriptBlock {
    fsutil file createnew C:\Users\Administrator\Documents\file4.txt 120000000
}


Invoke-Command -ComputerName WIN-Q3ULIUDB9L1 -ScriptBlock {
    Get-PSDrive C
}
```