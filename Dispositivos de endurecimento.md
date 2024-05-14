#Linux 
# Dispositivos de endurecimento

O fortalecimento (hardering) do dispositivo envolve a implementação de métodos comprovados de proteção do dispositivo e proteção de seu acesso administrativo. Alguns desses métodos envolvem a manutenção de senhas, a configuração de recursos avançados de login remoto e a implementação de login seguro com SSH. A definição de funções administrativas em termos de acesso é outro aspecto importante da proteção dos dispositivos de infraestrutura, pois nem todo o pessoal de tecnologia da informação deve ter o mesmo nível de acesso aos dispositivos de infraestrutura.

Dependendo da distribuição Linux, muitos serviços são habilitados por padrão. Alguns desses recursos estão habilitados por motivos históricos, mas não são mais necessários. Parar esses serviços e garantir que eles não iniciem automaticamente no momento da inicialização é outra técnica de fortalecimento (hardering) do dispositivo.

As atualizações do sistema operacional também são extremamente importantes para manter um dispositivo reforçado. Novas vulnerabilidades são descobertas todos os dias. Os desenvolvedores de SO criam e emitem correções e patches regularmente. Um computador atualizado é menos provável que seja comprometido.

A seguir estão as práticas recomendadas básicas para o fortalecimento (hardering) do dispositivo.

- Garanta a segurança física
- Minimizar pacotes instalados
- Desativar serviços não utilizados
- Usar SSH e desabilitar o login da conta raiz por SSH
- Manter o sistema atualizado
- Desativar a detecção automática de USB
- Aplicar senhas fortes
- Forçar mudanças de senha periódicas
- Manter os usuários de reutilizarem senhas antigas

Muitas outras etapas existem e muitas vezes dependem do serviço ou do aplicativo.