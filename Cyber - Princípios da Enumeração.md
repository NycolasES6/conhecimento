# Cyber - Princípios da Enumeração

Significa coleta de informações usando métodos ativos (varreduras) e passivos (uso de fornecedores terceirizados).

É importante observar que OSINT é um procedimento independente e deve ser executado separadamente da enumeração porque `OSINT is based exclusively on passive information gathering`não envolve enumeração ativa de um determinado alvo.

A enumeração é um ciclo no qual coletamos repetidamente informações com base nos dados que temos ou já descobrimos.

As informações podem ser coletadas de domínios, endereços IP, serviços acessíveis e muitas outras fontes.

---

Por exemplo, precisamos entender como a empresa está estruturada, quais serviços e fornecedores terceirizados ela utiliza, quais medidas de segurança podem estar em vigor e muito mais. É aqui que esta fase pode ser um pouco mal compreendida porque a maioria das pessoas se concentra no óbvio e tenta forçar a entrada nos sistemas da empresa em vez de entender como a infraestrutura está configurada e quais aspectos técnicos e serviços são necessários para poder oferecer um serviço específico.

Um exemplo dessa abordagem errada poderia ser que, depois de encontrar serviços de autenticação como SSH, RDP, WinRM e similares, tentamos usar a força bruta com senhas e nomes de usuário comuns/fracos. Infelizmente, a força bruta é um método barulhento e pode facilmente levar à lista negra, impossibilitando mais testes.

``Our goal is not to get at the systems but to find all the ways to get there.``

Na maioria dos casos, o foco principal de muitos testadores de penetração está no que podem ver e não no que não podem ver. No entanto, mesmo o que não podemos ver é relevante para nós e pode muito bem ser de grande importância. A diferença aqui é que começamos a ver os componentes e aspectos que não são visíveis à primeira vista com a nossa experiência.

- O que podemos ver?
- Que razões podemos ter para ver isso?
- Que imagem o que vemos cria para nós?
- O que ganhamos com isso?
- Como podemos usá-lo?
- O que não podemos ver?
- Que razões podem existir que não vemos?
- Que imagem resulta para nós daquilo que não vemos?

Um aspecto importante que não deve ser confundido aqui é que sempre há exceções às regras. Os princípios, porém, não mudam. Outra vantagem desses princípios é que podemos ver pelas tarefas práticas que não nos faltam habilidades de teste de penetração, mas sim conhecimento técnico, quando de repente não sabemos como proceder porque nossa tarefa principal não é explorar as máquinas, mas descobrir como elas podem ser explorado.

|     |                                                               |
| --- | ------------------------------------------------------------- |
| 1.  | Há mais do que aparenta. Considere todos os pontos de vista.  |
| 2.  | Distinguir entre o que vemos e o que não vemos.               |
| 3.  | Sempre há maneiras de obter mais informações. Entenda o alvo. |

























