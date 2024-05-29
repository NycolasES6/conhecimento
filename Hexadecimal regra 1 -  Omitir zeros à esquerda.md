#redes #bases_numericas 
# Hexadecimal regra 1 -  Omitir zeros à esquerda

A primeira regra para ajudar a reduzir a notação de endereços IPv6 é omitir os 0s (zeros) à esquerda de qualquer seção de 16 bits ou hexteto. Aqui estão quatro exemplos de maneiras de omitir zeros à esquerda:

- 01AB pode ser representado como 1AB
- 09f0 pode ser representado como 9f0
- 0a00 pode ser representado como a00
- 00ab pode ser representado como ab

Essa regra se aplica somente aos 0s à esquerda, e NÃO aos 0s à direita. Caso contrário, o endereço ficaria ambíguo. Por exemplo, o hexteto “abc” poderia ser “0abc” ou “abc0”, mas essas duas representações não se referem ao mesmo valor.

| Tipo              | Formato                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Preferencial      | 2001   :   **0**db8   :   **000**0   :   1111   :   **000**0   :   **000**0   :   **000**0   :   **0**200          |
| Sem 0s à esquerda | 2001   :     db8   :         0   :   1111   :         0   :         0   :         0   :     200                    |
| Preferencial      | 2001   :   **0**db8   :   **000**0   :   **00**a3   :   ab00   :   **0**ab0   :   **00**ab   :   1234              |
| Sem 0s à esquerda | 2001   :     db8   :         0   :       a3   :   ab00   :     ab0   :       ab   :   1234                         |
| Preferencial      | 2001   :   **0**db8   :   **000**a   :   **000**1   :   c012   :     90ff   :    fe90   :   **000**1               |
| Sem 0s à esquerda | 2001   :     db8   :         a   :         1   :   c012   :     90ff   :    fe90   :        1                      |
| Preferencial      | 2001   :   **0**db8   :   aaaa   :   **000**1   :   **000**0   :    **000**0   :   **000**0   :   **000**0         |
| Sem 0s à esquerda | 2001   :     db8   :    aaaa  :         1   :         0    :         0   :         0   :         0                 |
| Preferencial      | fe80    :   **000**0   :   **000**0   :  **000**0   :    **0**123   :   4567   :   89ab   :   cdef                 |
| Sem 0s à esquerda | fe80    :       0     :         0   :        0   :       123   :   4567   :   89ab   :   cdef                      |
| Preferencial      | fe80    :   **000**0   :   **000**0   :   **000**0  :    **000**0   :   **000**0   :   **000**0   :   **000**1     |
| Sem 0s à esquerda | fe80    :         0   :         0   :        0   :          0   :         0   :         0   :         1            |
| Preferencial      | **000**0    :   **000**0   :   **000**0   :   **000**0  :    **000**0   :   **000**0   :   **000**0   :   **000**1 |
| Sem 0s à esquerda | 0      :         0   :         0   :        0   :          0   :         0   :         0   :         1             |
| Preferencial      | **000**0    :   **000**0   :   **000**0   :   **000**0  :    **000**0   :   **000**0   :   **000**0   :   **000**0 |
| Sem 0s à esquerda | 0      :         0   :         0   :        0   :          0   :         0   :         0   :         0             |

