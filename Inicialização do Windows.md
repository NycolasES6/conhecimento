#SO #Windows 

# Inicialização do Windows

Há dois itens de registro importantes que são usados para iniciar automaticamente aplicativos e serviços:

- **HKEY_LOCAL_MACHINE** - Vários aspectos da configuração do Windows são armazenados nesta chave, incluindo informações sobre serviços que iniciam com cada inicialização.
- **HKEY_CURRENT_USER** - Vários aspectos relacionados ao usuário logado são armazenados nesta chave, incluindo informações sobre serviços que iniciam somente quando o usuário faz logon no computador.

O registro será discutido mais adiante neste tópico.

Entradas diferentes nesses locais de registro definem quais serviços e aplicativos serão iniciados, conforme indicado pelo tipo de entrada. Esses tipos incluem Run, RunOnce, RunServices, RunServicesOnce e Userinit. Essas entradas podem ser inseridas manualmente no registro, mas é muito mais seguro usar a ferramenta **Msconfig.exe** . Esta ferramenta é usada para exibir e alterar todas as opções de inicialização do computador. Use a caixa de pesquisa para localizar e abrir a ferramenta Msconfig.