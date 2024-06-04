#cyber #redes 
# RAID

![[Pasted image 20240604095421.png]]

## Como funciona?

O RAID obtém os dados normalmente armazenados em um único disco e os espalha entre várias unidades. Se qualquer disco único RAID0 for perdido, o usuário poderá recuperar os dados de outros discos que também hospedam os dados.

O RAID também pode aumentar a velocidade da recuperação de dados, já que várias unidades recuperarão os dados solicitados mais rapidamente do que um disco fazendo o mesmo.

## Armazenamento de dados

Uma solução RAID pode ser baseada em software ou hardware. Uma solução baseada em hardware requer um controlador de hardware especializado, no sistema que contenha as unidades RAID.

Os termos a seguir descrevem as várias maneiras pelas quais o RAID pode armazenar dados na matriz de discos.

- **Espelhamento** - Armazena dados duplicados em uma segunda unidade.
- **Distribuição** - Grava dados em várias unidades para que segmentos consecutivos sejam armazenados em unidades diferentes.
- **Paridade** - mais precisamente, tirar a paridade. Após a distribuição, as somas de verificação são geradas para verificar se não há erros nos dados distribuídos. Essas somas de verificação são armazenadas em uma terceira unidade.

Existem outras arquiteturas RAID, que combinam principalmente os elementos acima.











