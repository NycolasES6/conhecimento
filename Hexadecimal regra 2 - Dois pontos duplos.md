#redes #bases_numericas 
# Hexadecimal regra 2 - Dois pontos duplos

A segunda regra para ajudar a reduzir a notação de endereços IPv6 é que dois pontos duplos (::) podem substituir qualquer string única e contígua de um ou mais hextetos de 16 bits consistindo em zeros. Por exemplo, 2001:db8:cafe: 1:0:0:0:1 (0s iniciais omitidos) poderia ser representado como 2001:db8:cafe:1::1. Os dois-pontos duplos (::) são usados no lugar dos três hextetos compostos por zeros (0:0:0).

Os dois-pontos duplos (::) só podem ser usados uma vez dentro de um endereço, caso contrário, haveria mais de um endereço resultante possível. Quando associada à técnica de omissão dos 0s à esquerda, a notação do endereço IPv6 pode ficar bastante reduzida. É o chamado formato compactado.

Aqui está um exemplo do uso incorreto dos dois pontos duplos: 2001:db8::abcd::1234.

Os dois pontos duplos são usados duas vezes no exemplo acima. Aqui estão as possíveis expansões possíveis deste endereço de formato compactado incorretamente:

- 2001:db8::abcd:0000:0000:1234
- 2001:db8::abcd:0000:0000:0000:1234
- 2001:db8:0000:abcd::1234
- 2001:db8:0000:0000:abcd::1234

Se um endereço tiver mais de uma string contígua de hextetos com zero, a melhor prática é usar dois pontos duplos (::) na string mais longa. Se as strings forem iguais, a primeira string deve usar dois pontos duplos (::).

|Tipo|Formato|
|---|---|
|Preferencial|2001   :   **0**db8   :   **000**0   :   1111   :   **000**0   :   **000**0   :   **000**0   :   **0**200|
|Compactado/espaços|2001   :     db8   :         0   :   1111   :                                            :     200|
|Compactado|2001:db8:0:1111::200|
|Preferencial|2001   :   **0**db8   :   **000**0   :   **000**0   :   ab00   :   **0000**   :   **0000**   :   **0000**|
|Compactado/espaços|2001   :     db8   :         0   :         0   :   ab00   : :|
|Compactado|2001:db8:0:0:ab00::|
|Preferencial|2001   :   **0**db8   :   aaaa   :   **000**1   :   **0000**   :   **0000**   :   **0000**   :   **0000**|
|Compactado/espaços|2001   :     db8   :    aaaa   :     1      : :|
|Compactado|2001:db8:aaaa:1::|
|Preferencial|fe80    :   **0000**   :   **0000**   :   **0000**   :   **0**123   :   4567   :   89ab   :   cdef|
|Compactado/espaços|fe80    :                                            :     123   :   4567   :   89ab   :   cdef|
|Compactado|fe80::123:4567:89ab:cdef|
|Preferencial|fe80    :   **0000**   :   **0000**   :   **0000**   :   **0000**   :   **0000**   :   **0000**   :   **000**1|
|Compactado/espaços|fe80    :                                                                                         :         1|
|Compactado|fe80::1|
|Preferencial|**0000**   :   **0000**   :   **0000**   :   **0000**   :   **0000**   :   **0000**   :   **0000**   :   **000**1|
|Compactado/espaços|::                                                                                                             1|
|Compactado|::1|
|Preferencial|**0000**   :   **0000**   :   **0000**   :   **0000**   :   **0000**   :   **0000**   :   **0000**   :   **0000**|
|Compactado/espaços|::|
|Compactado|::|

