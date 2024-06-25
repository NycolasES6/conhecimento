# Cyber - Prova de conceito

`Proof of Concept`( `PoC`) ou `Proof of Principle`é um termo de gerenciamento de projetos. No gerenciamento de projetos, serve como prova de que um projeto é viável em princípio.

Os critérios para isso podem residir em fatores técnicos ou comerciais.

Em outras palavras, serve como base de tomada de decisão para o futuro curso de ação. Ao mesmo tempo, permite identificar e minimizar riscos.

![[0-PT-Process-POC.webp]]

Esta etapa do projeto é frequentemente integrada ao processo de desenvolvimento de novos softwares aplicativos (prototipagem) ou soluções de segurança de TI.

Para nós da segurança da informação, é aqui que comprovamos vulnerabilidades em sistemas operacionais ou softwares aplicativos. Usamos esta PoC para provar que existe um problema de segurança para que os desenvolvedores ou administradores possam validá-lo, reproduzi-lo, ver o impacto e testar seus esforços de correção.

A versão mais prática de um PoC é um `script`ou `code`que explora automaticamente as vulnerabilidades encontradas. Isso demonstra a exploração perfeita das vulnerabilidades.

Esta variante é simples para um administrador ou desenvolvedor porque eles podem ver quais etapas nosso script executa para explorar a vulnerabilidade.

Depois que os administradores e desenvolvedores recebem esse script de nós, é fácil para eles "lutar" contra o nosso script. Eles se concentram em mudar os sistemas para que o script que criamos não funcione mais.

O importante é que o script seja apenas `one way`de exploração de uma determinada vulnerabilidade.

Por exemplo, se um usuário usar a senha `Password123`, a vulnerabilidade subjacente não será a senha, mas o `password policy`.

 Se for descoberto que um administrador de domínio está usando essa senha e ela for alterada, essa conta agora terá uma senha mais forte, mas o problema de senhas fracas provavelmente ainda será endêmico na organização.






















