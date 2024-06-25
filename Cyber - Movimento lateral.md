# Cyber - Movimento lateral

Se tudo correr bem entraremos em seguida na `Lateral Movement`fase.

Se um sistema na rede corporativa estiver infectado com ransomware, ele poderá se espalhar por toda a rede. Ele bloqueia todos os sistemas usando vários métodos de criptografia, tornando-os inutilizáveis ​​para toda a empresa até que uma chave de descriptografia seja inserida.

Nos casos mais comuns, a empresa é extorquida financeiramente para obter lucro.

Muitas vezes é esquecido que, em muitos países, as `CEOs are held liable`empresas não protegem adequadamente os dados dos seus clientes.

![[0-PT-Process-LA.webp]]

Nesta etapa, queremos testar até onde podemos avançar manualmente em toda a rede e quais vulnerabilidades podemos encontrar do ponto de vista interno que podem ser exploradas. Ao fazer isso, passaremos novamente por várias fases:

1. Pivoting
2. Evasive Testing
3. Information Gathering
4. Vulnerability Assessment
5. (Privilege) Exploitation
6. Post-Exploitation

Como pode ser visto no gráfico acima, podemos passar para este estágio a partir do estágio `Exploitation`e `Post-Exploitation`. Às vezes, podemos não encontrar uma maneira direta de aumentar nossos privilégios no próprio sistema de destino, mas temos maneiras de nos movimentar pela rede. É aqui que `Lateral Movement`entra em jogo.

## Pivoting

Na maioria dos casos, o sistema que utilizamos não terá as ferramentas para enumerar a rede interna de forma eficiente. Algumas técnicas nos permitem usar o host explorado como proxy e realizar todas as varreduras de nossa máquina de ataque ou VM. Ao fazer isso, o sistema explorado representa e encaminha todas as nossas solicitações de rede enviadas da nossa máquina de ataque para a rede interna e seus componentes de rede.

Desta forma, fazemos com que redes não roteáveis ​​(e, portanto, publicamente inacessíveis) ainda possam ser alcançadas. Isso nos permite examiná-los em busca de vulnerabilidades e penetrar mais profundamente na rede. Este processo também é conhecido como `Pivoting`ou `Tunneling`.

## Testes evasivos

Além disso, nesta fase, devemos considerar se os testes evasivos fazem parte do âmbito da avaliação.

Existem procedimentos diferentes para cada tática, que nos auxiliam a disfarçar essas solicitações para não disparar um alarme interno entre os administradores e a equipe azul.

Existem muitas maneiras de proteger contra movimentos laterais, incluindo rede (micro) `segmentation`, `threat monitoring`, `IPS`/ `IDS`, `EDR`, etc. Para contorná-los de forma eficiente, precisamos entender como eles funcionam e a que respondem.

Então poderemos adaptar e aplicar métodos e estratégias que ajudem a evitar a detecção.

## Coleta de informações

Antes de atingirmos a rede interna, devemos primeiro saber `overview`quais sistemas e quantos podem ser alcançados a partir do nosso sistema.

Voltamos à etapa de Coleta de Informações, mas desta vez fazemos isso de dentro da rede com uma visão diferente dela.

## Avaliação de vulnerabilidade

A avaliação da vulnerabilidade de dentro da rede difere dos procedimentos anteriores. Isso ocorre porque ocorrem muito mais erros dentro de uma rede do que em hosts e servidores expostos à Internet.

Aqui, aquele `groups`ao qual foi atribuído e os `rights`diferentes componentes do sistema desempenham um papel essencial.

Por exemplo, se comprometermos uma conta de usuário atribuída a um grupo de desenvolvedores, poderemos obter acesso à maioria dos recursos usados ​​pelos desenvolvedores da empresa. Isto provavelmente nos fornecerá informações internas cruciais sobre os sistemas e poderá nos ajudar a identificar falhas ou promover nosso acesso.

## (Privilégio) Exploração

Freqüentemente encontramos maneiras de quebrar senhas e hashes e obter privilégios mais elevados. Outro método padrão é usar nossas credenciais existentes em outros sistemas. Haverá também situações em que nem precisaremos quebrar os hashes, mas poderemos usá-los diretamente. Por exemplo, podemos usar a ferramenta [Responder](https://github.com/lgandx/Responder) para interceptar hashes NTLMv2.

Se pudermos interceptar um hash de um administrador, poderemos usar a `pass-the-hash`técnica para fazer login como administrador (na maioria dos casos) em vários hosts e servidores.

## Pós exploração

Depois de atingirmos um ou mais hosts ou servidores, passamos novamente pelas etapas do estágio de pós-exploração para cada sistema.

Aqui coletamos novamente informações do sistema, dados de usuários criados e informações comerciais que podem ser apresentadas como evidência.

No entanto, devemos novamente considerar como estas diferentes informações devem ser tratadas e as regras definidas em torno dos dados sensíveis no contrato.











