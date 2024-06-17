#Linux 
# Linux - Interrupção de um processo na linha de comando

Você pode usar a interface `top` para interromper um processo, mas primeiro deve determinar a ID do processo que pretende interromper.

Na interface `top`, pressione **L** no teclado. Os prompts interativos na interface `top` aparecem acima dos rótulos das colunas.

![[Pasted image 20240617144337.png]]

Digite o nome do processo que deseja interromper após o prompt `Locate string` e pressione **Enter**. A interface `top` é atualizada para exibir todas as correspondências para o termo de pesquisa. Revise a lista de correspondências para o processo que você deseja interromper e anote sua PID.

Para interromper o processo, pressione **k** no teclado. Digite a PID do processo no prompt `top` e pressione **Enter**.

![[Pasted image 20240617144424.png]]

Pressione **Enter** novamente quando o comando `top` solicitar o sinal a ser enviado.

Também é possível usar o comando `kill` para encerrar um processo. O comando `kill` não é um utilitário interativo; portanto, você deve fornecer a ID do processo a ser encerrado. No exemplo a seguir, você encerra o processo com a ID 7460.

![[Pasted image 20240617144810.png]]





