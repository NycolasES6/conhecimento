# Octal - Binário

## Octal > Binário

> A relação entre a base octal e binária é de que para chegarmos a 8 na base 2, elevamos 2 a 3. Então usaremos 3 casas para representar cada dígito de binário para octal e de octal para binário.

|       | casa3 | casa2 | casa1 |   | casa3 | casa2 | casa1 |
| :---  | :---: | :---: | :---: |---| :---: | :---: | :---: |
|Result |   4   |   2   |   1   |   |   4   |   2   |   1   |
|  Oct  |       |   2   |       |   |       |   7   |       |
| Potên |  2^2  |  2^1  |  2^0  |   |  2^2  |  2^1  |  2^0  |
| Bina  |   0   |   1   |   0   |   |   1   |   1   |   1   |

Para cada dígito em Octal precisamos de 3 em binário. Então teremos as potências de 0, 1 e 2, somando o resultado das potênciasonde especificamos com 1 devemos obter o número especificado.

``Exemplo :`` No 7 colocamos 1 em todas as casas pois somamos 4 + 2 + 1, que resulta em 7. Lembrando que só existe uma combinação possível para cada dígito, e que podemos descartar o zero a esquerda.

## Binário > Octal

> Nesse caso vamos pegar um número em binário e separar ele em grupos de 3, organizar as potências e somar para obter cada dígito.

Precisamos de grupos de 3 dígitos, caso fique faltando dígitos para formar um grupo, acrescente zeros a esquerda do ultimo grupo. Lembrando que é da direita para a esquerda : `10 111` --> `010 111`

|       | casa3 | casa2 | casa1 |   | casa3 | casa2 | casa1 |
| :---  | :---: | :---: | :---: |---| :---: | :---: | :---: |
| Bina  |   0   |   1   |   0   |   |   1   |   1   |   1   |
| Potên |  2^2  |  2^1  |  2^0  |   |  2^2  |  2^1  |  2^0  |
|Result |   4   |   2   |   1   |   |   4   |   2   |   1   |
|  Oct  |       |   2   |       |   |       |   7   |       |

Agora pegamos o número em binário, organizamos as potências, somamos o resultado de cada grupo.

Nesse caso obtivemos (2 7)8 = (27 na base octal)
