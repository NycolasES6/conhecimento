#Linux 
# Linux - Processamento de lotes de arquivos

_ecurso de curinga_ é o processo de interpretar e expandir metacaracteres ou curingas para especificar diferentes arquivos ou diretórios. Recurso de curinga é um tipo de processamento em lote porque você interage com muitos arquivos para evitar tarefas repetitivas.

Para manipular vários arquivos com uma execução de comando, você pode usar metacaracteres. Um _metacaractere_ é um caractere especial que o shell usa como um espaço reservado para algo mais complexo.

O metacaractere mais comum é o til (`~`), que expande para o caminho para seu diretório pessoal. Ao trabalhar em um terminal, o prompt de comando exibe um til (`~`), que indica que seu diretório de trabalho atual é seu diretório pessoal. Você pode usar o til (`~`) nos comandos como o caminho absoluto para seu diretório pessoal. Use a barra (`/`) após o til (`~`) para se referir a um arquivo ou diretório dentro do diretório pessoal.

![[Pasted image 20240614153326.png]]

O shell interpreta os metacaracteres asterisco (`*`) e ponto de interrogação (`?`) como curingas. Antes da execução do comando, o shell substitui um metacaractere por qualquer coisa que possa corresponder a ele. Um asterisco (`*`) corresponde a zero ou mais de qualquer caractere, e o caractere ponto de interrogação (`?`) corresponde exatamente a um de qualquer caractere.

Por exemplo, o padrão `Do*s` corresponde aos diretórios `Documents` e `Downloads`, e o padrão `D*` corresponde aos diretórios `Documents`, `Downloads` e `Desktop`.

![[Pasted image 20240614153419.png]]

Neste exemplo, o padrão `Document?` corresponde ao diretório `Documents`, mas não ao arquivo `Document`.

![[Pasted image 20240614153438.png]]

Você pode combinar metacaracteres. Por exemplo, o padrão `ar*t?z` corresponde aos arquivos `archive.tgz`, `archive.txz` e `artwork.tgz`, mas não ao arquivo `artwork.tar.xz`. No entanto, o padrão `ar*t*z` corresponde aos arquivos `archive.tgz`, `archive.txz`, `artwork.tgz` e `artwork.tar.xz`.

---

Você pode usar o recurso de curinga para executar um único comando em vários arquivos. Por exemplo, você só pode mover documentos em PDF do diretório `Downloads` para o diretório `Documents`.

![[Pasted image 20240614153621.png]]