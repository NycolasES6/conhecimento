# Números binários

## Conversão de Binário > Decimal

Para convertermos um número binário em decimal, devemos pegar esse número, separar por casas, elevar a base 2 pela potência de cada casa, multiplicar pelo algarismo contido na casa e somar os resultados.

| Ind |Casa3|Casa2|Casa1|
| --- | --- | --- | --- |
| Res |  4  |  2  |  1  |
| Bin |  1  |  0  |  1  |
| Pot | 2^2 | 2^1 | 2^0 |

A casa 1 tem potência de 2^0 = 1, se multiplicarmos pelo 1, que é o algarismo contido naquela casa resultara em 1.

A casa 2 tem o 0 como algarismo, então podemos ignorá lo, pois o resultado da multiplicação será 0.

A casa 3 tem potência de 2^2 = 4, se multiplicarmos pelo 1, que é o algarismo daquela casa dara 4.

Então somamos o resultado de cada casa.

`1 + 4 = 5`

Então o número em binário 101 representa o número 5 na base decimal.

> Como pode perceber, não precisamos fazer a perte ad multiplicação,pois qualquer número vezes 1 sera ele mesmo, e qualquer número vezes 0será 0.

|  Ind  | Casa5 | Casa4 | Casa3 | Casa2 | Casa1 |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  Res  |  16   |   8   |   4   |   2   |   1   |
|  Bin  |   1   |   0   |   0   |   1   |   1   |
|  Pot  |  2^4  |  2^3  |  2^2  |  2^1  |  2^0  |

Como falado, podemos ignorar os 0, e apenas somar o resultado das potênciações.

`16 + 2 + 1 = 19`

Então o número em binário 10011 representa o número 19 na base decimal.

## Conversão de Decimal > Binário

Para convertermos um número decimal em binário, devemos dividir esse número por 2 armazenar o resto e refazer esse processo até não seja mais possível. Depois pegamos os restos armazenados e os organizamos de forma inversa a que eles foram obtidos.

|Decimal|Resulta| Resto | Binar |
| :---: | :---: | :---: | :---: |
|  19   |   9   |   1   |   1   |
|   9   |   4   |   1   |   0   |
|   4   |   2   |   0   |   0   |
|   2   |   1   |   0   |   1   |
|   1   |   0   |   1   |   1   |

### Passo a passo

1 - 19/2 = 9 e sobra 1 então armazenamos o 1.
`[1]`

2 - 9/2 = 4 e sobra 1 então armazenamos o 1.
`[11]`

3 - 4/2 = 2 e sobra 0 então armazenamos o 0.
`[110]`

4 - 2/2 = 1 e sobra 0 então armazenamos o 0.
`[1100]`

5 - 1/2 = 0 e sobra 1 então armazenamos o 1.
`[11001]`

E agora colocamos eles de forma inversa a que eles foram obtidos.
`[10011]`

### Macete

Podemos fazer de um jeito mais rápido.
Vamos montar as notações posicionais, e vamos pegar o resultadodas potências. Vamos somar o resultado das potências até chegar no número que estamos convertendo.Não se preocupe só existe uma combinação possível.

Nas casas que usamos o resultado da potência para chagoar ao número em questão colocamos 1, e nas que não usamos colocamos o 0.

`19 = [ 16 ] [ 8 ] [ 4 ] [ 2 ] [ 1 ]`

|       | casa 5| casa4 | casa3 | casa2 | casa1 |
| :---: | :---: | :---: | :---: | :---: | :---: |
|Result |  16   |   8   |   4   |   2   |   1   |
|  Bin  |   1   |   0   |   0   |   1   |   1   |
|  Pot  |  2^4  |  2^3  |  2^2  |  2^1  |  2^0  |

A única solução possível é se somarmos `16 + 2 + 1`
