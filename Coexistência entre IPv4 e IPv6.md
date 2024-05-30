#redes 
# Coexistência entre IPv4 e IPv6

Não há uma data exata para migrar para o IPv6. Tanto o IPv4 como o IPv6 coexistirão no futuro próximo e a transição levará vários anos. A IETF criou vários protocolos e ferramentas para ajudar os administradores de rede a migrarem as redes para IPv6. As técnicas de migração podem ser divididas em três categorias:

## Pilha dupla

A pilha dupla permite que IPv4 e IPv6 coexistam no mesmo segmento de rede. Os dispositivos de pilha dupla executam os protocolos IPv4 e IPv6 simultaneamente. Conhecido como IPv6 nativo, isso significa que a rede do cliente tem uma conexão IPv6 com seu ISP e é capaz de acessar o conteúdo encontrado na internet através de IPv6.

![[Pasted image 20240529104826.png]]

## Tunelamento

Tunelamento é um método de transporte de pacote IPv6 através de uma rede IPv4. O pacote IPv6 é encapsulado dentro de um pacote IPv4, de forma semelhante a outros tipos de dados.

![[Pasted image 20240529104903.png]]

## Conversão

O NAT64 (Network Address Translation 64) permite que os dispositivos habilitados para IPv6 se comuniquem com os dispositivos habilitados para IPv4 usando uma técnica de conversão semelhante ao NAT IPv4. Um pacote IPv6 é traduzido para um pacote IPv4 e um pacote IPv4 é traduzido para um pacote IPv6.

![[Pasted image 20240529104940.png]]

---

**Observação:** O tunelamento e a tradução são para transição para IPv6 nativo e só devem ser usados quando necessário. O objetivo deve ser as comunicações IPv6 nativas da origem até o destino.



























