# Redes - TTL

TTL ou tem pode vida do pacote IP serve justamente para que o pacote não fique vagando eternamente pela rede.

Cada vez que o pacote IP passa por um roteador (hop) o seu TTL é decrementado -1, até se tornar 0, quando o valor se torna 0 o roteador descarta o pacote.

O TTL é um campo do protocolo IP e cada sistema operacional implementa um valor padrão para esse campo. Por exemplo:

- Windows usa o TTL padrão de 128
- Linux usa o TTL padrão de 64
- Unix usa o TTL padrão de 255

De qualquer forma esse valores podem ser alterados pelo usuário.
