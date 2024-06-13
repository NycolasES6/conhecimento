#Windows 
# Definir o Serviço de Cópias de Sombra de Volume

O backup de dados críticos de negócios pode ser uma tarefa desafiadora, principalmente devido a seu tamanho e ao alto volume de alterações. Alguns dos arquivos de dados, inclusive, podem estar abertos ou em um estado inconsistente. Para enfrentar esse desafio, você pode usar o VSS.

## O que é o VSS?

As operações de backup e restauração requerem coordenação estreita entre os aplicativos de backup, os aplicativos de linha de negócios que manipulam os dados submetidos a backup e o hardware e software de gerenciamento do armazenamento. O Backup do Windows Server usa o VSS para executar backups. O VSS facilita a comunicação entre esses componentes para otimizar a colaboração. O VSS coordena as ações necessárias para criar uma cópia de sombra consistente (também conhecida como um instantâneo ou uma cópia pontual) dos dados que passarão por backup.

As soluções do VSS têm os seguintes componentes básicos:

- Serviço VSS. Parte do sistema operacional Windows que garante que os outros componentes consigam se comunicar entre si corretamente e funcionar juntos.
- Solicitante VSS. Esse software solicita a criação real de cópias de sombra ou outras operações de alto nível, como importação ou exclusão. Normalmente, esse é um aplicativo de backup, como Backup do Windows Server.
- Gravador VSS. Esse componente garante que você tenha um conjunto de dados consistente para fazer backup. Normalmente, ele faz parte de um aplicativo de linha de negócios, como o Microsoft SQL Server ou o Microsoft Exchange Server. O sistema operacional Windows inclui gravadores VSS para vários componentes do Windows, como o Registro.
- Provedor VSS. Esse componente cria e mantém as cópias de sombra. Isso pode ocorrer no software ou no hardware. O sistema operacional Windows inclui um provedor VSS que usa cópia em gravação.

![[Pasted image 20240613170755.png]]

![[Pasted image 20240613170814.png]]
O VSS dá suporte a tamanhos de volume de até 64 TB.