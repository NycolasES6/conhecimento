# Exadecinal

Os números octais são escritos com os algarismos de 0 á 9 e A á F, somando assim 16 algarismos.

## Conversão Exadecimal > Decimal

O processo é o mesmo que o da conversão de binário para decimal.Mas em vez de a base ser 2 será 16.

| Ind |Casa3|Casa2|Casa1|
| --- | --- | --- | --- |
| Res | 256 | 240 |  10 |
| Oct |  1  |  F  | A   |
| Pot |16^2 |16^1 |16^0 |

`256 + 240 + 10 = 506`

## Conversão Decimal > Exadecimal

Para convertermos um número decimal em hexadecimal, devemos dividir esse número por 16 armazenar o resto e refazer esse processo até não seja mais possível. Depois pegamos os restos armazenados e os organizamos de forma inversa a que eles foram obtidos.

|Decimal|Resulta| Resto |  Exad |
| :---: | :---: | :---: | :---: |
|  685  |  42   |  13   |   0   |
|  42   |   2   |  10   |   2   |
|   2   |   0   |   2   |  10   |
|   0   |   0   |   0   |  13   |
