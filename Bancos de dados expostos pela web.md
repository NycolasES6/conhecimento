#cyber #db

# Bancos de dados expostos pela web

Aplicativos Web geralmente se conectam a um banco de dados relacional para acessar dados. Como os bancos de dados relacionais geralmente contêm dados confidenciais, os bancos de dados são um alvo frequente para ataques.

#### Injeção de código

Os atacantes podem executar comandos no sistema operacional de um servidor Web através de uma aplicação Web vulnerável. Isso pode ocorrer se o aplicativo Web fornecer campos de entrada para o invasor para inserir dados mal-intencionados. Os comandos do intruso são executados através da aplicação Web e têm as mesmas permissões que a aplicação Web. Este tipo de ataque é usado porque muitas vezes não há validação insuficiente de entrada. Um exemplo é quando um ator ameaça injeta código PHP em um campo de entrada inseguro na página do servidor.

#### Injeção de SQL

SQL é a linguagem usada para consultar um banco de dados relacional. Os atores de ameaças usam injeções SQL para violar o banco de dados relacional, criar consultas SQL mal-intencionadas e obter dados confidenciais do banco de dados relacional.

Um dos ataques de banco de dados mais comuns é o ataque de injeção SQL. O ataque de injeção SQL consiste em inserir uma consulta SQL através dos dados de entrada do cliente para o aplicativo. Uma exploração de injeção SQL bem-sucedida pode ler dados confidenciais do banco de dados, modificar dados do banco de dados, executar operações de administração no banco de dados e, às vezes, emitir comandos para o sistema operacional.

A menos que um aplicativo use validação rigorosa de dados de entrada, ele será vulnerável ao ataque de injeção SQL. Se um aplicativo aceitar e processar dados fornecidos pelo usuário sem qualquer validação de dados de entrada, um ator de ameaça poderá enviar uma string de entrada criada com intuito malicioso para acionar o ataque de injeção SQL.

Os analistas de segurança devem ser capazes de reconhecer consultas SQL suspeitas para detectar se o banco de dados relacional foi submetido a ataques de injeção SQL. Eles precisam ser capazes de determinar qual ID de usuário foi usado pelo ator da ameaça para fazer login e, em seguida, identificar qualquer informação ou acesso adicional que o ator da ameaça poderia ter aproveitado após um login bem-sucedido.
































