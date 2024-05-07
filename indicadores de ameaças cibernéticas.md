
# Indicadores de ameaças cibernéticas

Muitos ataques de rede podem ser evitados compartilhando informações sobre indicadores de comprometimento (COI). Cada ataque tem atributos identificáveis únicos. Indicadores de compromisso são a evidência de que um ataque ocorreu. Os IOCs podem ser recursos que identificam arquivos de malware, endereços IP de servidores que são usados em ataques, nomes de arquivos e alterações características feitas no software final do sistema, entre outros. Os IOCs ajudam o pessoal de segurança cibernética a identificar o que aconteceu em um ataque e desenvolver defesas contra o ataque. Um resumo do COI para um pedaço de malware é mostrado na figura.

```txt
Malware File - "studiox-link-standalone-v20.03.8-stable.exe"
        sha256 6a6c28f5666b12beecd56a3d1d517e409b5d6866c03f9be44ddd9efffa90f1e0
        sha1 eb019ad1c73ee69195c3fc84ebf44e95c147bef8
        md5 3a104b73bb96dfed288097e9dc0a11a8
DNS requests
        domain log.studiox.link
        domain my.studiox.link
        domain  _sips._tcp.studiox.link
        domain sip.studiox.link
Connections
        ip 198.51.100.248
        ip 203.0.113.82
```

Por exemplo, um usuário recebe um e-mail afirmando que ganhou um grande prêmio. Clicar no link no e-mail resulta em um ataque. O COI poderia incluir o fato de o usuário não estar concorrendo a nenhum sorteio, o endereço IP do remetente, a linha de assunto do e-mail, o URL a ser clicado, ou um anexo para baixar, entre outros.

**Indicadores de ataque** (IOA) se concentram mais na motivação por trás de um ataque e nos potenciais meios pelos quais os atores da ameaça têm, ou irão, comprometer vulnerabilidades para obter acesso a ativos. Os IOAs estão preocupadas com as estratégias usadas pelos atacantes. Por esse motivo, em vez de informar a resposta a uma única ameaça, os IOAs podem ajudar a gerar uma abordagem de segurança proativa. Isso ocorre porque as estratégias podem ser reutilizadas em vários contextos e ataques múltiplos. Defender contra uma estratégia pode, portanto, impedir ataques futuros que utilizem a mesma estratégia, ou similar.














