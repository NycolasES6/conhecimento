#cyber #programação 
# Verificações de Integridade

![[Pasted image 20240528090656.png]]

Dados comprometidos podem ameaçar a segurança de seus dispositivos e sistemas.

Uma **verificação de integridade** pode medir a consistência dos dados em um arquivo, imagem ou registro para garantir que eles não tenham sido corrompidos. A verificação de integridade executa uma **função hash** para obter um instantâneo de dados e, em seguida, usa esse instantâneo para garantir que os dados permaneçam inalterados. Um **checksum** é um exemplo de uma função hash.

## Como funciona um checksum

Uma checksum verifica a integridade de arquivos, ou de strings de caracteres, antes e depois de serem transferidos de um dispositivo para outro por uma rede local ou pela Internet. As checksum simplesmente convertem cada conjunto de informações para um valor e soma o total. Para testar a integridade de dados, um sistema de recebimento apenas repete o processo. Se as duas somas forem iguais, os dados são válidos. Caso contrário, uma alteração ocorreu em algum lugar ao longo do caminho.

## Funções de hash

Funções hash comuns incluem MD5, SHA-1, SHA-256 e SHA-512. Eles usam algoritmos matemáticos complexos para comparar dados com um valor de hash. Por exemplo, depois de baixar um arquivo, o usuário pode verificar a integridade do arquivo, comparando os valores de hash da fonte com o valor gerado por qualquer calculadora de hash.

## Controle de versão

As empresas usam controle de versão para evitar alterações acidentais por usuários autorizados. O controle de versão significa que dois usuários não podem atualizar o mesmo objeto, como um arquivo, registro de banco de dados ou transação, ao mesmo tempo. Por exemplo, o primeiro usuário a abrir um documento tem a permissão para alterar esse documento. A segunda pessoa tem uma versão somente leitura.

## Backups

Backups precisos ajudam a manter a integridade de dados, se os dados forem corrompidos. Uma empresa precisa verificar o seu processo para garantir a integridade do backup, antes que ocorra perda de dados.

## Aurotização

A autorização determina quem tem acesso aos recursos da empresa, de acordo com a necessidade de cada um. Por exemplo, controles de acesso de usuário e permissões de arquivo garantem que apenas determinados usuários possam modificar os dados. Um administrador pode definir as permissões de um arquivo como somente leitura. Como resultado, um usuário que acessa esse arquivo não pode fazer nenhuma alteração.

























