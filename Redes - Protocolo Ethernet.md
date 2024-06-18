# Redes - Protocolo Ethernet

## Estrutura do protocolo Ethernet

![[Pasted image 20240618091453.png]]

**Tipo** - Código que identifica o tipo de protocolo (0800 = IP / 0806 = ARP)
**Payload** - Contém os dados a serem transportados (outro protocolo).

### Exemplo prático

![[Pasted image 20240618091824.png]]

## Frame ethernet

O tamanho mínimo do quadro Ethernet é 64 bytes e o máximo é 1518 bytes. Isso inclui todos os bytes do campo de endereço MAC de destino por meio do campo de sequência de verificação de quadro (FCS). O campo do preâmbulo não é incluído ao descrever o tamanho do quadro.

Qualquer quadro com menos de 64 bytes de comprimento é considerado um “fragmento de colisão” ou “quadro runt” e é automaticamente descartado pelas estações receptoras. Quadros com mais de 1.500 bytes de dados são considerados “jumbo” ou “quadros gigantes”.

Se o tamanho de um quadro transmitido for menor que o mínimo ou maior que o máximo, o dispositivo receptor descarta o quadro. Os quadros perdidos são provavelmente o resultado de colisões ou outros sinais indesejados. Eles são considerados inválidos. Os quadros jumbo são geralmente suportados pela maioria dos switches e NICs Fast Ethernet e Gigabit Ethernet.

A figura mostra cada campo no frame Ethernet. Consulte a tabela para obter mais informações sobre a função de cada campo.

![[Pasted image 20240618091434.png]]














