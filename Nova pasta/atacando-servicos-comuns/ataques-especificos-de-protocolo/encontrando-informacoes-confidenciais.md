# Encontrando informações confidenciais

Ao atacar um serviço, geralmente desempenhamos um papel de detetive e precisamos coletar o máximo de informações possível e observar cuidadosamente os detalhes. Portanto, cada informação é essencial.

Vamos imaginar que estamos envolvidos com um cliente, temos como alvo e-mail, FTP, bancos de dados e armazenamento, e nosso objetivo é obter Execução Remota de Código (RCE) em qualquer um desses serviços. Iniciamos a enumeração e tentamos o acesso anônimo a todos os serviços, sendo que apenas o FTP possui acesso anônimo. Encontramos um arquivo vazio dentro do serviço FTP, mas com o nome johnsmith, tentamos johnsmith como usuário e senha do FTP, mas não funcionou. Tentamos o mesmo no serviço de e-mail e fizemos o login com sucesso. Com o acesso ao email, começamos a pesquisar emails contendo a palavra senha, encontramos muitos, mas um deles contém as credenciais de John para o banco de dados MSSQL. Acessamos o banco de dados e usamos a funcionalidade integrada para executar comandos e obter RCE com sucesso no servidor de banco de dados. Atingimos nosso objetivo com sucesso.

Um serviço mal configurado nos permitiu acessar uma informação que inicialmente pode parecer insignificante, johnsmith, mas essa informação abriu as portas para descobrirmos mais informações e finalmente conseguirmos a execução remota de código no servidor de banco de dados. Essa é a importância de prestar atenção a cada informação, a cada detalhe, à medida que enumeramos e atacamos serviços comuns.

As informações confidenciais podem incluir, mas não estão limitadas a:

- Nomes de usuário.
- Endereço de e-mail.
- Senhas.
- Registros DNS.
- Endereços IP.
- Código fonte.
- Arquivos de configuração.
- PII.

Este módulo cobrirá alguns serviços comuns onde podemos encontrar informações interessantes e descobrir diferentes métodos e ferramentas que podemos usar para automatizar nosso processo de descoberta. Esses serviços incluem:

- Compartilhamentos de arquivos.
- E-mail.
- Bancos de dados.

## Compreensão do que devemos procurar

Cada alvo é único e precisamos nos familiarizar com ele, seus processos, procedimentos, modelo de negócios e propósito. Depois de entendermos nosso alvo, podemos pensar sobre quais informações são essenciais para eles e que tipo de informações são úteis para nosso ataque.

Existem dois elementos principais para encontrar informações confidenciais:

1. Precisamos entender o serviço e como ele funciona.
2. Precisamos saber o que estamos procurando.
