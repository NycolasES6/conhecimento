#redes 
# Firewalls

Um firewall é um sistema ou grupo de sistemas que aplica uma política de controle de acesso entre redes.

### Permitir

- **Permitir** o tráfego de qualquer endereço externo para o servidor Web.
- **Permitir** o tráfego no servidor FTP.
- **Permitir** o tráfego para o servidor SMTP.
- **Permitir** o tráfego no servidor IMAP interno.

### Negar

- **Negar** todo o tráfego de entrada com os endereços de rede que correspondem ao endereços IP registrados internamente.
- **Negar** todo o tráfego de entrada de endereços externos para o servidor.
- **Negar** todo o tráfego de entrada de ICMP echo requests.
- **Negar** todas as consultas de entrada ao MS Active Directory.
- **Negar** todas as transmissões do MS Domain Local

---

### Propriedades comuns do Firewall

Todos os firewalls compartilham algumas propriedades comuns:

- Os firewalls são resistentes a ataques de rede.
- Firewalls são o único ponto de trânsito entre redes corporativas internas e redes externas porque todo o tráfego flui através do firewall.
- Firewalls reforçam a política de controle de acesso.

### Benefícios do firewall

Existem vários benefícios do uso de um firewall em uma rede:

- Eles impedem a exposição de hosts, recursos e aplicações sensíveis a usuários não confiáveis.
- Eles sanitizam o fluxo do protocolo, o que impede a exploração de falhas no protocolo.
- Eles bloqueiam dados maliciosos de servidores e clientes.
- Eles reduzem a complexidade do gerenciamento de segurança descarregando a maior parte do controle de acesso à rede para alguns firewalls na rede.

### Limitações do Firewall

Os firewalls também têm algumas limitações:

- Um firewall mal configurado pode ter sérias conseqüências para a rede, como se tornar um único ponto de falha.
- Os dados de muitos aplicativos não podem ser transmitidos por firewalls com segurança.
- Os usuários podem procurar proativamente maneiras de contornar o firewall para receber material bloqueado, o que expõe a rede a possíveis ataques.
- O desempenho da rede pode diminuir.
- O tráfego não autorizado pode ser encapsulado ou escondido como tráfego legítimo através do firewall.




















