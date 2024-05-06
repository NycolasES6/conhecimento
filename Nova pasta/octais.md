# Números octais

Os números octais são escritos com os algarismos de 0 á 7, somando assim 8 algarismos.

## Conversão Octal > Decimal

O processo é o mesmo que o da conversão de binário para decimal.Mas em vez de a base ser 2 será 8.

| Ind |Casa3|Casa2|Casa1|
| --- | --- | --- | --- |
| Res |  64 |  24 |  7  |
| Oct |  1  |  3  |  7  |
| Pot | 8^2 | 8^1 | 8^0 |

`64 + 24 + 7 = 95`

| Ind |Casa3|Casa2|Casa1|Casa1|
| --- | --- | --- | --- | --- |
| Res | 512 | 128 | 40  |  7  |
| Oct |  1  |  2  |  5  |  7  |
| Pot | 8^3 | 8^2 | 8^1 | 8^0 |

`512 + 128 + 40 + 7 = 687`

## Conversão Decimal > Octal

Para convertermos um número decimal em octal, devemos dividir esse número por 8 armazenar o resto e refazer esse processo até não seja mais possível. Depois pegamos os restos armazenados e os organizamos de forma inversa a que eles foram obtidos.

|Decimal|Resulta| Resto | Octal |
| :---: | :---: | :---: | :---: |
|  177  |  22   |   1   |   0   |
|  22   |   2   |   6   |   2   |
|   2   |   0   |   2   |   6   |
|   2   |   1   |   0   |   1   |
