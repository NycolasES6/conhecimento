#redes #cyber 
# Vantagens e desvantagens de IDS e IPS

Vantagens e desvantagens do IDS

A tabela lista as vantagens e desvantagens do IDS e do IPS.

![[Pasted image 20240510175125.png]]

### Vantagens e desvantagens do IDS

**Vantagens IDS**

Um IDS é implantado no modo off-line e, portanto:

- Os IDs não afetam o desempenho da rede. Especificamente, ele não introduz latência, variação ou outros problemas de fluxo de tráfego.
- Os IDs não afetam a funcionalidade de rede se o sensor falhar. Isso afeta apenas a capacidade do IDS para analisar os dados.

**Desvantagens IDS**

As desvantagens de um IDS incluem:

- Um sensor IDS não pode parar o pacote de disparo e é menos útil na interrupção de vírus de e-mail e ataques automatizados, como worms.
- Ajustar os sensores IDS para atingir os níveis esperados de detecção de intrusão pode ser muito demorado. Os usuários que implantam ações de resposta do sensor IDS devem ter uma política de segurança bem projetada e uma boa compreensão operacional de suas implantações de IDS.
- Uma implementação de IDS é mais vulnerável a técnicas de evasão de segurança de rede porque não está em linha.

### Vantagens e desvantagens do IPS

**Vantagens IPS**

As vantagens de um IPS incluem:

- Um sensor IPS pode ser configurado para executar uma perda de pacotes para interromper o pacote de gatilho, os pacotes associados a uma conexão ou os pacotes de um endereço IP de origem.
- Como os sensores IPS estão em linha, eles podem usar a normalização de fluxo. Normalização de fluxo é uma técnica usada para reconstruir o fluxo de dados quando o ataque ocorre em vários segmentos de dados.

**Desvantagens IPS**

As desvantagens de um IPS incluem:

- Como ele é implantado em linha, erros, falhas e sobrecarregar o sensor IPS com muito tráfego podem ter um efeito negativo no desempenho da rede.
- Um sensor IPS pode afetar o desempenho da rede introduzindo latência e jitter.
- Um sensor IPS deve ser dimensionado e implementado adequadamente para que aplicativos sensíveis ao tempo, como VoIP, não sejam afetados negativamente.

### Considerações de implantação

Você pode implantar um IPS e um IDS. Usar uma dessas tecnologias não anula o uso da outra. Na verdade, as tecnologias IDS e IPS podem se complementar.

Por exemplo, um IDS pode ser implementado para validar a operação de IPS porque o IDS pode ser configurado para inspeção de pacotes mais profunda off-line. Isso permite que o IPS se concentre em menos, mas mais críticos padrões de tráfego em linha.

Decidir qual implementação usar se baseia nos objetivos de segurança da organização, conforme indicado em sua política de segurança de rede.












