#Linux #shell 

# Trabalhando com arquivos de texto

Linux tem muitos editores de texto diferentes, com vários recursos e funções. Alguns editores de texto incluem interfaces gráficas, enquanto outros são apenas ferramentas de linha de comando. Cada editor de texto inclui um conjunto de recursos projetado para suportar um tipo específico de tarefa. Alguns editores de texto se concentram no programador e incluem recursos como realce de sintaxe, parênteses e verificação de parênteses e outros recursos focados na programação.

Embora os editores de texto gráficos sejam convenientes e fáceis de usar, os editores de texto baseados em linha de comando são muito importantes para os usuários do Linux. O principal benefício dos editores de texto baseados em linha de comando é que eles permitem a edição de arquivos de texto a partir de um computador remoto.

Considere o seguinte cenário: um usuário deve executar tarefas administrativas em um computador Linux, mas não está sentado na frente desse computador. Usando SSH, o usuário inicia um shell remoto para o computador remoto. Sob o shell remoto baseado em texto, a interface gráfica não está disponível, o que torna impossível confiar em ferramentas como editores de texto gráficos. Neste tipo de situação, programas baseados em texto são cruciais.

A figura mostra **nano**, um editor de texto de linha de comando popular. O administrador está editando regras de firewall. Editores de texto são frequentemente usados para configuração e manutenção do sistema no Linux.

![[Pasted image 20240514175315.png]]

Devido à falta de suporte gráfico, nano (ou GNU nano) só pode ser controlado com o teclado. Por exemplo, **CTRL+O** salva o arquivo atual; **CTRL+W** abre o menu de pesquisa. GNU nano usa uma barra de atalho de duas linhas na parte inferior da tela, onde os comandos para o contexto atual são listados. Pressione **CTRL+G** para a tela de ajuda e uma lista de comandos completa.