#protocolo #redes #hacking 

# Vulnerabilidades RDP mais recentes

Em 2019, foi publicada uma vulnerabilidade crítica no serviço RDP (`TCP/3389`) que também levou à execução remota de código ( `RCE`) com o identificador [CVE-2019-0708](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2019-0708) . Esta vulnerabilidade é conhecida como `BlueKeep`. Não é necessário acesso prévio ao sistema para explorar o serviço para nossos propósitos. No entanto, a exploração desta vulnerabilidade levou e ainda leva a muitos ataques de malware ou ransomware. Grandes organizações, como hospitais, cujo software é concebido apenas para versões e bibliotecas específicas, são particularmente vulneráveis ​​a tais ataques, uma vez que a manutenção da infra-estrutura é dispendiosa. Aqui também não entraremos em detalhes minuciosos sobre essa vulnerabilidade, mas manteremos o foco no conceito.
## O conceito do ataque

A vulnerabilidade também se baseia, como acontece com o SMB, em solicitações manipuladas enviadas ao serviço visado. No entanto, o perigoso aqui é que a vulnerabilidade não requer autenticação do usuário para ser acionada. Em vez disso, a vulnerabilidade ocorre após a inicialização da conexão, quando as configurações básicas são trocadas entre o cliente e o servidor. Isso é conhecido como técnica [Use-After-Free](https://cwe.mitre.org/data/definitions/416.html) ( `UAF`) que usa memória liberada para executar código arbitrário.

### O conceito de ataques

![[attack_concept2 1.webp]]

Este ataque envolve muitas etapas diferentes no kernel do sistema operacional, que não são de grande importância aqui por enquanto para entender o conceito por trás dele. Após a função ter sido explorada e a memória liberada, os dados são gravados no kernel, o que nos permite sobrescrever a memória do kernel. Esta memória é usada para escrever nossas instruções na memória liberada e deixar a CPU executá-las. Se quisermos dar uma olhada na análise técnica da vulnerabilidade BlueKeep, este [artigo](https://unit42.paloaltonetworks.com/exploitation-of-windows-cve-2019-0708-bluekeep-three-ways-to-write-data-into-the-kernel-with-rdp-pdu/) fornece uma boa visão geral.

## Início do Ataque

| **Etapa** | **BlueKeep**                                                                                                                                                                                                                                                                                              | **Conceito de Ataques - Categoria** |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `1.`      | Aqui, a fonte é a solicitação de inicialização da troca de configurações entre servidor e cliente que o invasor manipulou.                                                                                                                                                                                | `Source`                            |
| `2.`      | A solicitação leva a uma função usada para criar um canal virtual contendo a vulnerabilidade.                                                                                                                                                                                                             | `Process`                           |
| `3.`      | Como este serviço é adequado para [administração](https://docs.microsoft.com/en-us/windows/win32/ad/the-localsystem-account) do sistema, ele é executado automaticamente com os privilégios [da conta LocalSystem](https://docs.microsoft.com/en-us/windows/win32/ad/the-localsystem-account) do sistema. | `Privileges`                        |
| `4.`      | A manipulação da função nos redireciona para um processo kernel.                                                                                                                                                                                                                                          | `Destination`                       |

É quando o ciclo recomeça, mas desta vez para obter acesso remoto ao sistema de destino.

### Acionar execução remota de código

| **Etapa** | **BlueKeep**                                                                                                                                                                                                                                                                | **Conceito de Ataques - Categoria** |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `5.`      | A fonte desta vez é a carga criada pelo invasor que é inserida no processo para liberar memória no kernel e colocar nossas instruções.                                                                                                                                      | `Source`                            |
| `6.`      | O processo no kernel é acionado para liberar a memória do kernel e permitir que a CPU aponte para o nosso código.                                                                                                                                                           | `Process`                           |
| `7.`      | Como o kernel também roda com os privilégios mais altos possíveis, as instruções que colocamos na memória liberada do kernel aqui também são executadas com privilégios [de conta LocalSystem .](https://docs.microsoft.com/en-us/windows/win32/ad/the-localsystem-account) | `Privileges`                        |
| `8.`      | Com a execução de nossas instruções do kernel, um shell reverso é enviado pela rede para nosso host.                                                                                                                                                                        | `Destination`                       |

Nem todas as variantes mais recentes do Windows são vulneráveis ​​ao Bluekeep, de acordo com a Microsoft. Estão disponíveis atualizações de segurança para versões atuais do Windows, e a Microsoft também forneceu atualizações para muitas versões mais antigas do Windows que não são mais suportadas. No entanto, `950,000` sistemas Windows foram identificados como vulneráveis ​​a ataques `Bluekeep` numa verificação inicial em maio de 2019 e, ainda hoje, cerca de um quarto desses anfitriões ainda estão vulneráveis.

> 
> Nota: Esta é uma falha que provavelmente encontraremos durante nossos testes de penetração, mas pode causar instabilidade do sistema, incluindo uma “tela azul da morte (BSoD)”, e devemos ter cuidado antes de usar a exploração associada. Em caso de dúvida, é melhor falar primeiro com nosso cliente para que ele entenda os riscos e então decida se gostaria que executássemos a exploração ou não.
> 




