#cyber #redes
# Zona Desmilitarizada (DMZ)

![[Pasted image 20240528112201.png]]

Uma zona desmilitarizada (DMZ) é uma pequena rede entre uma rede privada confiável e a Internet.

## Acesso a redes não confiáveis

Os servidores Web e de correio geralmente são colocados na DMZ para permitir que os usuários acessem uma rede não confiável, como a Internet, sem comprometer a rede interna.

## Zonas de Risco

A maioria das redes tem de duas a quatro zonas de risco: a LAN privada confiável, a DMZ, a Internet e uma extranet.

- Na zona de LAN, o nível de risco é baixo e o nível de confiança é alto. 
- Na zona da extranet, o nível de risco é médio-baixo e o nível de confiança médio-alto.
- Na DMZ, o nível de risco é médio-alto e o nível de confiança é médio-baixo.
- Na zona da Internet, o nível de risco é alto e o nível de confiança é baixo.

## Modelo de zero-trust

Os firewalls gerenciam o tráfego de ponta a ponta (tráfego que vai entre os servidores no data center da empresa) e o tráfego de ponta a ponta (dados que entram e saem da rede da empresa).

Para proteger sua rede, uma empresa pode implementar um **modelo de confiança zero**. Confiar em usuários e endpoints automaticamente na empresa pode colocar qualquer rede em risco, já que usuários confiáveis podem se mover por toda a rede para acessar dados. A rede Zero Trust monitora constantemente todos os usuários na rede, independentemente de status ou função.
















