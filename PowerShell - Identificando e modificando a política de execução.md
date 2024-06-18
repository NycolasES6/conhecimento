# PowerShell - Identificando e modificando a política de execução

A política de execução no PowerShell destina-se a minimizar a possibilidade de um usuário executar scripts do PowerShell sem querer. Você pode considerar isso como uma funcionalidade de segurança que controla as condições sob as quais o PowerShell carrega arquivos de configuração e executa scripts. Esse recurso ajuda a impedir a execução de scripts mal-intencionados.

Para identificar a política de execução efetiva para a sessão atual do PowerShell, use o seguinte cmdlet:

```PowerShell
Get-ExecutionPolicy
```

Você pode definir as seguintes configurações de política:

- **AllSigned**. Limita a execução de script em todos os scripts assinados. Esta configuração exige que todos os scripts sejam assinados por um editor confiável, incluindo scripts escritos no computador local. Ele solicita antes de executar scripts de editores que você ainda não classificou como confiáveis ou não confiáveis. No entanto, verificar a assinatura de um script não elimina a possibilidade de esse script ser mal-intencionado. Isso simplesmente fornece uma verificação extra que minimiza essa possibilidade.

- **Default**. Define a política de execução padrão, que é **Restricted** para clientes do Windows e **RemoteSigned** para servidores do Windows.

- **RemoteSigned**. Essa é a política de execução padrão para computadores com servidor do Windows. Os scripts podem ser executados, mas a política exige uma assinatura digital de um editor confiável em scripts e arquivos de configuração que foram baixados da Internet. Essa configuração não exige assinaturas digitais em scripts escritos no computador local.

- **Restricted**. Essa é a política de execução padrão para computadores com cliente do Windows. Ela permite a execução de comandos individuais, mas não permite scripts.

- **Unrestricted**. Essa é a política de execução padrão para computadores não Windows, que você não pode alterar. Ela permite que sejam executados scripts não assinados. Essa política avisa o usuário antes de executar scripts e arquivos de configuração que não são da zona de intranet local.

- **Undefined**. Indica que não há uma política de execução definida no escopo atual. Se a política de execução em todos os escopos for **Undefined**, a política de execução efetiva será **Restricted** para clientes do Windows e **RemoteSigned** para servidores do Windows.

Para alterar a política de execução no PowerShell, use o seguinte comando:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
```


