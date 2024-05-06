#protocolo #hacking #redes 

# Últimas vulnerabilidades de DNS

Podemos encontrar milhares de subdomínios e domínios na web. Freqüentemente, eles apontam para provedores de serviços terceirizados que não estão mais ativos, como AWS, GitHub e outros e, na melhor das hipóteses, exibem uma mensagem de erro como confirmação de um serviço terceirizado desativado. Grandes empresas e corporações também são afetadas continuamente. Muitas vezes, as empresas cancelam serviços de fornecedores terceirizados, mas esquecem de excluir os registros DNS associados. Isso ocorre porque não há custos adicionais para uma entrada de DNS. Muitas plataformas conhecidas de recompensas por bugs, como [HackerOne](https://www.hackerone.com/) , já listam explicitamente `Subdomain Takeover`como uma categoria de recompensas. Com uma simples pesquisa, podemos encontrar diversas ferramentas no GitHub, por exemplo, que automatizam a descoberta de subdomínios vulneráveis ​​ou ajudam a criar Provas de Conceito ( `PoC`) que podem então ser submetidas ao programa de recompensas de bugs de nossa escolha ou da empresa afetada. RedHuntLabs fez um [estudo](https://redhuntlabs.com/blog/project-resonance-wave-1.html) sobre isso em 2020 e descobriu que mais de 400.000 subdomínios de 220 milhões eram vulneráveis ​​à aquisição de subdomínios. 62% deles pertenciam ao setor de comércio eletrônico.

## Estudo RedHuntLabs

![[image-3.webp]]

## O conceito do ataque

Um dos maiores perigos de uma aquisição de subdomínio é que pode ser lançada uma campanha de phishing considerada parte do domínio oficial da empresa alvo. Por exemplo, os clientes olhariam o link e veriam que o domínio `customer-drive.inlanefreight.com`(que aponta para um bucket S3 inexistente da AWS) está por trás do domínio oficial `inlanefreight.com` e confiariam nele como cliente. Porém, os clientes não sabem que esta página foi espelhada ou criada por um invasor para provocar um login dos clientes da empresa, por exemplo.

Portanto, se um invasor encontrar um registro `CNAME` nos registros DNS da empresa que aponte para um subdomínio que não existe mais e retorne um `HTTP 404 error`, esse subdomínio provavelmente poderá ser assumido por nós por meio do uso de um provedor terceirizado. Um controle de subdomínio ocorre quando um subdomínio aponta para outro domínio usando o registro CNAME que não existe atualmente. Quando um invasor registra esse domínio inexistente, o subdomínio aponta para o registro do domínio por nós. Ao fazer uma única alteração de DNS, nos tornamos proprietários desse subdomínio específico e, depois disso, podemos gerenciar o subdomínio como quisermos.

## O conceito de ataques

![[attack_concept2 1.webp]]

O que acontece aqui é que o subdomínio existente já não aponta para um fornecedor terceiro e, portanto, já não é ocupado por este fornecedor. Praticamente qualquer pessoa pode registrar este subdomínio como seu. A visita a este subdomínio e a presença do registro CNAME no DNS da empresa faz com que, na maioria dos casos, tudo funcione conforme o esperado. No entanto, o design e a função deste subdomínio estão nas mãos do invasor.

## Início da aquisição de subdomínio

| **Etapa** | **Aquisição de subdomínio**                                                                                                                                                                                                          | **Conceito de Ataques - Categoria** |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| `1.`      | A fonte, neste caso, é o nome do subdomínio que não é mais utilizado pela empresa que descobrimos.                                                                                                                                   | `Source`                            |
| `2.`      | O registo deste subdomínio no site do fornecedor terceiro é feito através do registo e ligação a fontes próprias.                                                                                                                    | `Process`                           |
| `3.`      | Aqui, os privilégios são do proprietário do domínio primário e de suas entradas em seus servidores DNS. Na maioria dos casos, o fornecedor terceiro não é responsável pelo facto de este subdomínio ser acessível através de outros. | `Privileges`                        |
| `4.`      | O registro e a vinculação bem-sucedidos são feitos em nosso servidor, que é o destino neste caso.                                                                                                                                    | `Destination`                       |

É quando o ciclo recomeça, mas desta vez para acionar o encaminhamento para o servidor que controlamos.

## Acione o encaminhamento

|**Etapa**|**Aquisição de subdomínio**|**Conceito de Ataques - Categoria**|
|---|---|---|
|`5.`|O visitante do subdomínio insere a URL em seu navegador, e o registro DNS desatualizado (CNAME) que não foi removido é usado como fonte.|`Source`|
|`6.`|O servidor DNS consulta sua lista para ver se possui conhecimento sobre este subdomínio e, em caso afirmativo, o usuário é redirecionado para o subdomínio correspondente (que é controlado por nós).|`Process`|
|`7.`|Os privilégios para isso já são dos administradores que gerenciam o domínio, pois somente eles estão autorizados a alterar o domínio e seus servidores DNS. Como este subdomínio está na lista, o servidor DNS considera o subdomínio confiável e encaminha o visitante.|`Privileges`|
|`8.`|O destino aqui é a pessoa que solicita o endereço IP do subdomínio para onde deseja ser encaminhado pela rede.|`Destination`|

O controle de subdomínio pode ser usado não apenas para phishing, mas também para muitos outros ataques. Isso inclui, por exemplo, roubo de cookies, falsificação de solicitação entre sites (CSRF), abuso de CORS e violação da política de segurança de conteúdo (CSP). Podemos ver alguns exemplos de aquisições de subdomínios no [site HackerOne](https://hackerone.com/hacktivity?querystring=%22subdomain%20takeover%22) , que renderam pagamentos consideráveis ​​aos caçadores de recompensas de bugs.



























