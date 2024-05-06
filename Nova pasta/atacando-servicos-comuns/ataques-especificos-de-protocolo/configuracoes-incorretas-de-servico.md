# Configurações incorretas de serviço

As configurações incorretas geralmente acontecem quando um administrador de sistema, suporte técnico ou desenvolvedor não configura corretamente a estrutura de segurança de um aplicativo, site, desktop ou servidor, levando a caminhos abertos perigosos para usuários não autorizados. Vamos explorar algumas das configurações incorretas mais típicas de serviços comuns.

## Autenticação

Nos anos anteriores (embora ainda vejamos isso algumas vezes durante as avaliações), era comum que os serviços incluíssem credenciais padrão (nome de usuário e senha). Isto representa um problema de segurança porque muitos administradores deixam as credenciais padrão inalteradas. Hoje em dia, a maioria dos softwares pede aos usuários que configurem credenciais durante a instalação, o que é melhor do que as credenciais padrão. No entanto, lembre-se de que ainda encontraremos fornecedores que usam credenciais padrão, especialmente em aplicativos mais antigos.

Mesmo quando o serviço não possui um conjunto de credenciais padrão, um administrador pode usar senhas fracas ou nenhuma senha ao configurar os serviços, com a ideia de que alterará a senha assim que o serviço estiver configurado e em execução.

Como administradores, precisamos definir políticas de senha que se apliquem ao software testado ou instalado em nosso ambiente. Os administradores devem ser obrigados a cumprir uma complexidade mínima de senha para evitar combinações de usuários e senhas, como:

```txt
admin:admin
admin:password
admin:<blank>
root:12345678
administrator:Password
```

Assim que pegarmos o banner do serviço, a próxima etapa deverá ser identificar possíveis credenciais padrão. Se não houver credenciais padrão, podemos tentar as combinações fracas de nome de usuário e senha listadas acima.

### Autenticação anônima

Outra configuração incorreta que pode existir em serviços comuns é a autenticação anônima. O serviço pode ser configurado para permitir autenticação anônima, permitindo que qualquer pessoa com conectividade de rede acesse o serviço sem ser solicitada autenticação.

### Direitos de acesso mal configurados

Vamos imaginar que recuperamos as credenciais de um usuário cuja função é fazer upload de arquivos para o servidor FTP, mas que recebeu o direito de ler todos os documentos FTP. A possibilidade é infinita, dependendo do que está no servidor FTP. Podemos encontrar arquivos com informações de configuração de outros serviços, credenciais de texto simples, nomes de usuário, informações proprietárias e informações de identificação pessoal (PII).

Direitos de acesso mal configurados ocorrem quando as contas de usuário têm permissões incorretas. O maior problema poderia ser dar às pessoas mais abaixo na cadeia de comando acesso a informações privadas que apenas gerentes ou administradores deveriam ter.

Os administradores precisam planejar sua estratégia de direitos de acesso e existem algumas alternativas, como controle de acesso baseado em função (RBAC) e listas de controle de acesso (ACL) . Se quisermos prós e contras mais detalhados de cada método, podemos ler Escolhendo a melhor estratégia de controle de acesso , de Warren Parad, da Authress.

## Padrões desnecessários

A configuração inicial de dispositivos e software pode incluir, entre outros, configurações, recursos, arquivos e credenciais. Esses valores padrão geralmente visam a usabilidade e não a segurança. Deixá-lo padrão não é uma boa prática de segurança para um ambiente de produção. Padrões desnecessários são aquelas configurações que precisamos alterar para proteger um sistema, reduzindo sua superfície de ataque.

Poderíamos muito bem entregar as informações pessoais de nossa empresa em uma bandeja de prata se seguirmos o caminho mais fácil e aceitarmos as configurações padrão ao configurar o software ou um dispositivo pela primeira vez. Na realidade, os invasores podem obter credenciais de acesso para equipamentos específicos ou abusar de uma configuração fraca realizando uma breve pesquisa na Internet.

A configuração incorreta de segurança faz parte da lista dos 10 principais da OWASP . Vamos dar uma olhada naqueles relacionados aos valores padrão:

- Recursos desnecessários são ativados ou instalados (por exemplo, portas, serviços, páginas, contas ou privilégios desnecessários).
- As contas padrão e suas senhas ainda estão habilitadas e inalteradas.
- O tratamento de erros revela rastreamentos de pilha ou outras mensagens de erro excessivamente informativas aos usuários.
- Para sistemas atualizados, os recursos de segurança mais recentes estão desativados ou não configurados de forma segura.

## Prevenindo configuração incorreta

Depois de compreendermos o nosso ambiente, a estratégia mais simples para controlar o risco é bloquear a infraestrutura mais crítica e permitir apenas o comportamento desejado. Qualquer comunicação que não seja exigida pelo programa deverá ser desativada. Isso pode incluir coisas como:

- As interfaces administrativas devem ser desativadas.
- A depuração está desativada.
- Desative o uso de nomes de usuário e senhas padrão.
- Configure o servidor para evitar acesso não autorizado, listagem de diretórios e outros problemas.
- Execute verificações e auditorias regularmente para ajudar a descobrir futuras configurações incorretas ou correções ausentes.

O OWASP Top 10 fornece uma seção sobre como proteger os processos de instalação:

- Um processo de proteção repetível torna rápida e fácil a implantação de outro ambiente que esteja devidamente bloqueado. Os ambientes de desenvolvimento, controle de qualidade e produção devem ser configurados de forma idêntica, com credenciais diferentes usadas em cada ambiente. Além disso, este processo deve ser automatizado para minimizar o esforço necessário para configurar um novo ambiente seguro.

- Uma plataforma mínima sem recursos, componentes, documentação e amostras desnecessárias. Remova ou não instale recursos e estruturas não utilizados.

- Uma tarefa para revisar e atualizar as configurações apropriadas para todas as notas de segurança, atualizações e patches como parte do processo de gerenciamento de patches (consulte A06:2021-Componentes vulneráveis ​​e desatualizados). Revise as permissões de armazenamento em nuvem (por exemplo, permissões de bucket S3).

- Uma arquitetura de aplicação segmentada fornece separação eficaz e segura entre componentes ou locatários, com segmentação, conteinerização ou grupos de segurança em nuvem (ACLs).

- Envio de diretivas de segurança aos clientes, por exemplo, cabeçalhos de segurança.

- Um processo automatizado para verificar a eficácia das configurações e definições em todos os ambientes.
































