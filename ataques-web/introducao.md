# Ataques na web

Cobriremos três outros ataques web que podem ser encontrados em qualquer aplicação web, o que pode levar ao comprometimento. Discutiremos como detectar, explorar e prevenir cada um desses três ataques.



## HTTP Verb Tampering

O primeiro ataque web discutido neste módulo é a adulteração de verbos HTTP . Um ataque de adulteração de verbos HTTP explora servidores web que aceitam muitos verbos e métodos HTTP. Isso pode ser explorado enviando solicitações maliciosas usando métodos inesperados, o que pode levar a contornar o mecanismo de autorização do aplicativo da web ou até mesmo ignorar seus controles de segurança contra outros ataques da web. Os ataques de adulteração de verbos HTTP são um dos muitos outros ataques HTTP que podem ser usados ​​para explorar configurações de servidores web enviando solicitações HTTP maliciosas.

## Insecure Direct Object References (IDOR)

O segundo ataque discutido neste módulo é o Insecure Direct Object References (IDOR) . IDOR está entre as vulnerabilidades da web mais comuns e pode levar ao acesso a dados que não deveriam ser acessíveis por invasores. O que torna este ataque muito comum é essencialmente a falta de um sistema sólido de controle de acesso no back-end. Como os aplicativos da web armazenam arquivos e informações dos usuários, eles podem usar números sequenciais ou IDs de usuário para identificar cada item. Suponha que o aplicativo Web não possua um mecanismo robusto de controle de acesso e exponha referências diretas a arquivos e recursos. Nesse caso, podemos acessar os arquivos e informações de outros usuários simplesmente adivinhando ou calculando seus IDs de arquivo.



## XML External Entity (XXE) Injection

O terceiro e último ataque da web que discutiremos é a injeção de entidade externa XML (XXE) . Muitas aplicações web processam dados XML como parte de sua funcionalidade. Suponha que um aplicativo da web utilize bibliotecas XML desatualizadas para analisar e processar dados de entrada XML do usuário front-end. Nesse caso, pode ser possível enviar dados XML maliciosos para divulgar arquivos locais armazenados no servidor back-end. Esses arquivos podem ser arquivos de configuração que podem conter informações confidenciais, como senhas ou até mesmo o código-fonte do aplicativo web, o que nos permitiria realizar um teste de penetração de caixa branca no aplicativo web para identificar mais vulnerabilidades. Os ataques XXE podem até ser aproveitados para roubar as credenciais do servidor de hospedagem, o que comprometeria todo o servidor e permitiria a execução remota de código.




















































