#redes 
# TCP

## Cabeçalho TCP

![[Cabecalho-TCP.webp]]

Lembrese que ACK, FIN, SYN são flags no cabeçalho do TCP

## Conexão

Para estabelecer uma conexao, o protocolo TCP usa o Handshake de três vias. Sendo eles pedido de conexão - aceitação de conexão - confirmação de conxão

![[Pasted image 20240614093738.png]]

| Agent  | flag    | descrição               |
| ------ | ------- | ----------------------- |
| Client | SYN     | Faz o pedido de conexão |
| Server | ACK SYN | Confirma o pedido       |
| Client | ACK     | Estabelece a conexão    |
## Flags TCP

![[Pasted image 20240618110137.png]]

## Transferência de dados

Toda mensagem nessa etapa tem de ser um efeito de envio e resposta. Envio da informação e confirmação da informação enviada.

O protocolo TCP faz a confirmação da entrega de pacotes, caso o recebimento não esteja de acordo ele reenvia o pacote.

Para que isso ocorra há sempre uma mensagem com os dados(server) e uma confirmação da quantidade de dados recebidos(client)

![[Pasted image 20240614095916.png]]

Neste caso:
1. O servidor envia parte do pacote com um número de sequência (nesse caso 1)
2. O cliente confirma a entrega dessas partes do pacotes, informando a parte recebida (nesse caso 37)
3. O servidor manda outra parte com o número de sequência fornecido pelo cliente, para que o cliente saiba ordenar, assim o cliente sabe que esses dados são posteriores ao que ele acabou de receber. (nesse caso 37)
4. O cliente confirma a entrega desse dados com o número correspondente a quantidade de bytes fornecidos.

E ele vai fazendo essas comunicações até receber toda mensagem, lembrando que se houver falha na transmissão dos dados, o TCP reenvia essa parte de dados.

## Encerramento

O encerramento da comunicação pode ser feita tanto pelo servidor quanto pelo cliente.

![[Pasted image 20240614101122.png]]


| Agente   | flag    | Descrição                                                                                |
| -------- | ------- | ---------------------------------------------------------------------------------------- |
| Servidor | FIN     | O servidor manda uma mensagem de FIN para indicar o encerramento da cessão.              |
| Cliente  | ACK FIN | O cliente confirma que recebeu esta mensagem de encerramento, dizendo que pode encerrar. |
| Servidor | ACK     | O servidor confirma que vai encerrar a sessão de comunicação.                            |

## Perda de pacotes

Como o TCP é feito de envio e resposta, enquanto o cliente não enviar uma mensagem de ACK informando que recebeu o pacote o servidor vai continuar enviando o pacote.

![[Pasted image 20240614102049.png]]

Primeiro ele envia a mensagem, caso o "contador do TCP" estoure sem receber a mensagem de ACK, ele reenvia a mensagem.

O TCP envia vários pacotes de uma vez, e aguarda para saber se todos foram entregues, caso não haja a confirmação ele reenvia as que não foram confirmadas.

## Pacotes fora de ordem

Como o TCP não espera a confirmação de um pacote para enviar outro, pode haver de um pacote que devia chegar antes de outros chegue depois. Por isso que junto com os dados eles enviam um número de sequência, para que eles saibam ordenar e saber também se chegou um pacote errado.

![[Pasted image 20240614103013.png]]

Neste caso, o cliente recebeu um pacote de sequência 1 e mandou uma resposta dizendo que espera o pacote de sequência 37. Como o pacote de sequência 73 chegou antes do 37 o cliente reenvia a mensagem dizendo que espera o pacote de sequência 37. Caso o pacote chegue, independente se foi o que estava atrasado ou o que o servidor reenviou depois, ele manda uma resposta confirmando a entrega do pacote.