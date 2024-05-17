#cyber #Linux #SO 

# Verificação de Rootkit

Um rootkit é um tipo de malware projetado para aumentar os privilégios de um usuário não autorizado ou conceder acesso a partes do software que normalmente não devem ser permitidas. Rootkits também são frequentemente usados para proteger uma porta traseira para um computador comprometido.

A instalação de um rootkit pode ser automatizada (feita como parte de uma infecção) ou um invasor pode instalá-lo manualmente após comprometer um computador. Um rootkit é destrutivo porque ele muda o código do kernel e seus módulos, alterando as operações mais fundamentais do próprio sistema operacional. Com um nível tão profundo de comprometimento, os rootkits podem ocultar a intrusão, remover quaisquer faixas de instalação e até mesmo adulterar ferramentas de diagnóstico e solução de problemas para que sua saída agora esconda a presença do rootkit. Embora algumas vulnerabilidades do Linux ao longo do histórico tenham permitido a instalação do rootkit através de contas de usuário regulares, a grande maioria dos compromissos do rootkit requer acesso root ou administrador.

Como a própria natureza do computador está comprometida, a detecção de rootkit pode ser muito difícil. Os métodos de detecção típicos geralmente incluem a inicialização do computador a partir de mídia confiável, como um CD ativo do sistema operacional de diagnóstico. A unidade comprometida é montada e, a partir do conjunto de ferramentas do sistema confiável, ferramentas de diagnóstico confiáveis podem ser iniciadas para inspecionar o sistema de arquivos comprometido. Os métodos de inspeção incluem métodos baseados em comportamento, varredura de assinatura, varredura de diferenças e análise de despejo de memória.

A remoção do Rootkit pode ser complicada e muitas vezes impossível, especialmente nos casos em que o rootkit reside no kernel; a reinstalação do sistema operacional geralmente é a única solução real para o problema. Os rootkits de firmware geralmente requerem substituição de hardware.

**chkrootkit** é um popular programa baseado em Linux projetado para verificar o computador para rootkits conhecidos. É um script shell que usa ferramentas comuns do Linux, como **strings** e **grep** para comparar as assinaturas de programas principais. Ele também procura discrepâncias à medida que atravessa o sistema de arquivos /proc comparando as assinaturas encontradas lá com a saída de **ps.**

Embora útil, tenha em mente que os programas para verificar se há rootkits não são 100% confiáveis.

A saída do comando mostra a saída do chkrootkit em um Ubuntu Linux.

Melhor visualizado no modo paisagem.

```sh
analyst@cuckoo:~$ sudo ./chkrootkit[sudo] password for analyst:ROOTDIR is ‘/’Checking 'amd’... not foundChecking 'basename’... not infectedChecking 'biff’... not foundChecking 'chfn’... not infectedChecking 'chsh'... not infectedChecking 'cron'... not infectedChecking 'crontab’... not infectedChecking 'date'... not infectedChecking 'du'... not infectedChecking 'dirname'... not infectedChecking 'echo'... not infectedChecking 'egrep’... not infectedChecking 'env'— not infectedChecking 'find'... not infectedChecking 'fingerd'... not foundChecking 'gpm'... not foundChecking 'grep'... not infectedChecking 'hdparm’... not infectedChecking 'su'... not infectedChecking 'ifconfig'... not infectedChecking 'inetd’... not testedChecking 'inetdconf’... not found
```

