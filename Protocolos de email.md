#redes #cyber 
# Protocolos de email

Protocolos de e-mail como SMTP, POP3 e IMAP podem ser usados por atores de ameaças para espalhar malware, exfiltrar dados ou fornecer canais para servidores CNC de malware, como mostrado na figura.

SMTP envia dados de um host para um servidor de email e entre servidores de email. Como DNS e HTTP, é um protocolo comum para ver sair da rede. Como há muito tráfego SMTP, ele nem sempre é monitorado. No entanto, o SMTP foi usado no passado por malware para exfiltrar dados da rede. No 2014 hack da Sony Pictures, uma das explorações usou SMTP para exfiltrar detalhes do usuário de hosts comprometidos para servidores CNC. Essas informações podem ter sido usadas para ajudar a desenvolver explorações de recursos protegidos na rede Sony Pictures. O monitoramento de segurança pode revelar esse tipo de tráfego com base nos recursos da mensagem de email.

IMAP e POP3 são usados para baixar mensagens de email de um servidor de email para o computador host. Por esse motivo, eles são os protocolos de aplicativos que são responsáveis por trazer malware para o host. O monitoramento de segurança pode identificar quando um anexo de malware entrou na rede e qual host ele infectou pela primeira vez. A análise retrospectiva pode então rastrear o comportamento do malware a partir desse ponto em diante. Desta forma, o comportamento do malware pode ser melhor compreendido e a ameaça identificada. As ferramentas de monitoramento de segurança também podem permitir a recuperação de anexos de arquivos infectados para envio a caixas de proteção de malware para análise.

## Ameaças de protocolo de email

![[Pasted image 20240604120134.png]]















