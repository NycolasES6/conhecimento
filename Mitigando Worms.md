#cyber 

# Mitigando Worms

Worms são mais baseados em rede do que vírus. A mitigação do worm requer diligência e coordenação por parte do profissionais de segurança de rede.

Como mostrado na figura, a resposta a um ataque de vermes pode ser dividida em quatro fases: contenção, inoculação, quarentena e tratamento.

![[Pasted image 20240508174853.png]]

- **custos** - A fase de contenção envolve limitar a propagação de uma infecção por vermes para áreas da rede que já estão afetadas. Isso requer compartimentação e segmentação da rede para abrandar ou parar o worm e evitar que hosts atualmente infectados segmentem e infectem outros sistemas. A contenção requer o uso de ACLs de saída e entrada em roteadores e firewalls em pontos de controle dentro da rede.
- **Inoculação** - A fase de inoculação corre paralela ou subsequente à fase de contenção. Durante a fase de inoculação, todos os sistemas não infectados são corrigidos com o patch de fornecedor apropriado. O processo de inoculação priva ainda mais o worm de quaisquer alvos disponíveis.
- **Quarentena** - A fase de quarentena envolve rastrear e identificar máquinas infectadas dentro das áreas contidas e desconectá-las, bloquear ou removê-las. Isto isola estes sistemas adequadamente para a fase de tratamento.
- **Tratamento** - A fase de tratamento envolve a desinfecção ativa dos sistemas infectados. Isso pode envolver encerrar o processo do worm, remover arquivos modificados ou configurações do sistema introduzidos pelo worm e corrigir a vulnerabilidade que o worm usou para explorar o sistema. Alternativamente, em casos mais graves, o sistema pode precisar ser reinstalado para garantir que o worm e seus subprodutos sejam removidos.

