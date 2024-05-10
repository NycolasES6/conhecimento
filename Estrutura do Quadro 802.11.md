#redes 

# Estrutura do Quadro 802.11

Lembre-se de que todos os quadros da camada 2 consistem em uma seção de cabeçalho, carga útil e sequência de verificação de quadro (FCS - Frame Check Sequence). O formato de quadro 802.11 é semelhante ao formato de quadro Ethernet, exceto pelo fato de conter mais campos, conforme mostrado na figura.

![[Pasted image 20240510111051.png]]

Todos os quadros sem fio 802.11 contêm os seguintes campos:

- **Controle de quadro -** Identifica o tipo de quadro sem fio e contém subcampos para versão do protocolo, tipo de quadro, tipo de endereço, gerenciamento de energia e configurações de segurança.
- **Duração -** Isso normalmente é usado para indicar a duração restante necessária para receber a próxima transmissão de quadro.
- **Address1 -** Geralmente contém o endereço MAC do dispositivo sem fio ou AP receptor.
- **Address2 -** Geralmente contém o endereço MAC do dispositivo sem fio ou AP de transmissão.
- **Address3 -** Isso às vezes contém o endereço MAC do destino, como a interface do roteador (gateway padrão) ao qual o AP está conectado.
- **Sequence Control -** Contém informações para controlar o sequenciamento e os quadros fragmentados.
- **Address4 -** Isso geralmente está ausente porque é usado apenas no modo ad hoc.
- **Payload -** Contém os dados para transmissão.
- **FCS -** Isso é usado para controle de erro da camada 2.