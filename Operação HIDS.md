#cyber #redes 
# Operação HIDS

Pode-se dizer que os sistemas de segurança baseados em host funcionam como sistemas de detecção e prevenção porque evitam ataques conhecidos e detectam ataques potenciais desconhecidos. Um HIDS usa estratégias proativas e reativas. Um HIDS pode impedir invasões porque utiliza assinaturas para detectar malware conhecido e impedir que infecte um sistema. No entanto, esta estratégia só é boa contra ameaças desconhecidas. As assinaturas não são eficazes contra ameaças novas ou de dia zero. Além disso, algumas famílias de malware apresentam polimorfismo. Isso significa que variações de um tipo, ou família, de malware podem ser criadas por invasores que evitam detecções baseadas em assinaturas, alterando aspectos da assinatura de malware apenas o suficiente para que ele não seja detectado. Um conjunto adicional de estratégias é usado para detectar a possibilidade de intrusões bem-sucedidas por malware que evita a detecção de assinaturas:

## Baseado em anomalias

O comportamento do sistema host é comparado a um modelo de linha de base aprendido de comportamento normal. Desvios significativos da linha de base são interpretados como resultado de algum tipo de intrusão. Se uma intrusão for detectada, o HIDS poderá registrar detalhes da intrusão, enviar alertas para sistemas de gerenciamento de segurança e tomar medidas para evitar o ataque. A linha de medida base é derivada do comportamento do usuário e do sistema. Como muitas coisas além do malware podem fazer com que o comportamento do sistema mude, a detecção de anomalias pode criar muitos resultados errados, o que pode aumentar a carga de trabalho para o pessoal de segurança e também reduzir a atualização do sistema.

## Com base em política

O comportamento normal do sistema é descrito por regras, ou violação de regras, que são predefinidas. A violação dessas políticas resultará em ação do HIDS. O HIDS pode tentar encerrar processos de software que violaram as regras e pode registrar esses eventos e alertar o pessoal para particularidades. A maioria dos softwares HIDS vem com um conjunto de regras predefinidas. Com alguns sistemas, os administradores podem criar políticas personalizadas que podem ser distribuídas aos hosts a partir de um sistema central de gerenciamento de políticas.
























