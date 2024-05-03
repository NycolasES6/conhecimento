# Hexadecimal - Binário

## Hexadecimal > Binário

> A relação entre a base hexadecimal e binária é de que para chegarmos a 8 na base 2, elevamos 2 a 4. Então usaremos 4 casas para representar cada dígito de binário para hexadecimal e de hexadecimal para binário.

|       | casa4 | casa3 |     | casa2 | casa1 |   | casa4 | casa3 |     | casa2 | casa1 |
| :---  | :---: | :---: |:---:| :---: | :---: |---| :---: | :---: |:---:| :---: | :---: |
|Result |   8   |   4   |     |   2   |   1   |   |   8   |   4   |     |   2   |   1   |
|  Hex  |       |       |  1  |       |       |   |       |       |B(11)|       |       |
| Potên |  2^3  |  2^2  |     |  2^1  |  2^0  |   |  2^3  |  2^2  |     |  2^1  |  2^0  |
| Biná  |   0   |   0   |     |   0   |   1   |   |   1   |   0   |     |   1   |   1   |

Resultado: `0001 1011` --> `1 1011`

Para cada dígito em hexadecimal precisamos de 4 em binário. Então teremos as potências de 0, 1, 2 e 3, somando o resultado das potências onde especificamos com 1, devemos obter o número especificado.

``Exemplo :`` No B(11) colocamos 1 nas casas 1 | 2 | 4 pois somando 8 + 2 + 1, que resulta em 11. Lembrando que só existe uma combinação possível para cada dígito, e que podemos descartar o zero a esquerda.

## Binário > Hexadecimal

> Nesse caso vamos pegar um número em binário e separar ele em grupos de 3, organizar as potências e somar para obter cada dígito.

Precisamos de grupos de 3 dígitos, caso fique faltando dígitos para formar um grupo, acrescente zeros a esquerda do ultimo grupo. Lembrando que é da direita para a esquerda : `10 111` --> `010 111`

|       | casa4 | casa3 |     | casa2 | casa1 |   | casa4 | casa3 |     | casa2 | casa1 |
| :---  | :---: | :---: |:---:| :---: | :---: |---| :---: | :---: |:---:| :---: | :---: |
|Result |   8   |   4   |     |   2   |   1   |   |   8   |   4   |     |   2   |   1   |
| Biná  |   0   |   0   |     |   0   |   1   |   |   1   |   0   |     |   1   |   1   |
| Potên |  2^3  |  2^2  |     |  2^1  |  2^0  |   |  2^3  |  2^2  |     |  2^1  |  2^0  |
|  Hex  |       |       |  1  |       |       |   |       |       |B(11)|       |       |

Agora pegamos o número em binário, organizamos as potências, somamos o resultado de cada grupo.

Nesse caso obtivemos (1 B)16 = (1B na base hexadecimal)
