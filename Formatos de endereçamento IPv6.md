#redes 
# Formatos de endereçamento IPv6

O primeiro passo para aprender sobre IPv6 em redes é entender a forma como um endereço IPv6 é escrito e formatado. Os endereços IPv6 são muito maiores do que os endereços IPv4, razão pela qual é improvável que fiquemos sem eles.

Os endereços IPv6 têm 128 bits e são escritos como uma sequência de valores hexadecimais. Cada 4 bits são representados por um único dígito hexadecimal, totalizando 32 valores hexadecimais, como mostra a Figura 1. Os endereços IPv6 não diferenciam maiúsculas e minúsculas e podem ser escritos tanto em minúsculas como em maiúsculas.

## Segmentos de 16 bits ou Hextets

![[Pasted image 20240529105659.png]]

**Formato Preferencial**

Como mostrado na Figura 1, o formato preferencial para escrever um endereço IPv6 é x: x: x: x: x: x: x: x, com cada “x” consistindo em quatro algarismos hexadecimais. O termo octeto refere-se aos oito bits em um endereço IPv4. No IPv6, um hexteto é o termo não oficial usado para se referir a um segmento de 16 bits ou quatro algarismos hexadecimais. Cada “x” é um único hexteto de 16 bits ou quatro dígitos hexadecimais.

Formato preferencial significa que o endereço IPv6 é gravado usando todos os 32 dígitos hexadecimais. Isso não significa necessariamente que é o método ideal para representar o endereço IPv6. Existem duas regras que ajudam a reduzir o número de dígitos necessários para representar um endereço IPv6.

A Figura 3 tem exemplos de endereços IPv6 no formato preferencial.

```txt
2001 : 0db8 : 0000 : 1111 : 0000 : 0000 : 0000: 0200

2001 : 0db8 : 0000 : 00a3 : abcd : 0000 : 0000: 1234

2001 : 0db8 : 000a : 0001 : c012 : 9aff : fe9a: 19ac

2001 : 0db8 : aaaa : 0001 : 0000 : 0000 : 0000: 0000

fe80 : 0000 : 0000 : 0000 : 0123 : 4567 : 89ab: cdef

fe80 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000: 0001

fe80 : 0000 : 0000 : 0000 : c012 : 9aff : fe9a: 19ac

fe80 : 0000 : 0000 : 0000 : 0123 : 4567 : 89ab: cdef

0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000: 0001

0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000: 0001`
```

