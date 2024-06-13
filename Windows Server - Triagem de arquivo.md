#Windows 
# Windows Server - Triagem de arquivo

Abrimos o **File Server Resource Manager**

Em **File Screen Management>Files Screens>Actions>Create File Screen**

Na tela que se abrir, devemos colocar o **path** e o tipo de arquivo que queremos bloquear

![[Pasted image 20240613161019.png]]

Por final clicamos em **Create**


```powershell
Invoke-Command -ComputerName WIN-Q3ULIUDB9L1 -ScriptBlock {
    fsutil file createNew C:\Users\Administrator\Documents\Data\file.png 1300
}
```