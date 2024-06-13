#Windows 
# Windows Server - Configurar protocolo SMB

1. Habilitar o SMB 1.0 no servidor membro. Habilite explicitamente o SMB 1.0 usando o cmdlet `Enable-WindowsOptionalFeature` do Windows PowerShell.
2. Detectar se o SMB 1.0 está habilitado. Habilite a auditoria de conexões SMB 1.0.
3. Auditar o uso do SMB 1.0. Use as ferramentas de linha de comando para transferir as funções mestre de operações de volta para o primeiro controlador de domínio.
4. Desabilitar o SMB 1.0. Desabilite o SMB 1.0 usando o cmdlet `Disable-WindowsOptionalFeature` do Windows PowerShell.
5. Configurar a criptografia do SMB. Imponha o uso da criptografia do SMB.

```powershell
Get-WindowsOptionalFeature -Online -FeatureName smb1protocol
```
Verifica os status do smb1protocol

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName smb1protocol
```
Habilita o smb1protocol

```powershell
Disable-WindowsOptionalFeature -Online -FeatureName smb1protocol
```
Desabilita o smb1protocol

```powershell
Set-SmbServerConfiguration -AuditSmb1Access $true
```
Faz uma auditoria para saber se ainda existe algum cliente

### Encriptação do SMB

```powershell
Get-SmbServerConfiguration | Select EncryptData
```
Verifica se a criptografia está habilitada

```powershell
Set-SmbServerConfiguration -EncryptData $true
```
Aqui ativamos a encriptação









