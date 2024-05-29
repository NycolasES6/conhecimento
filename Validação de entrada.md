#cyber #programação  
# Validação de entrada

Controlar o processo de entrada de dados é fundamental para manter a integridade do banco de dados. Muitos ataques são executados em um banco de dados e inserem dados malformados. O ataque pode confundir, falhar ou fazer com que o aplicativo divulgue informações demais para o invasor. Role para baixo para ver um exemplo - neste caso, um ataque de entrada automatizado.

Por exemplo, os usuários preenchem um formulário usando um aplicativo da Web para assinar uma newsletter. Um aplicativo de banco de dados gera e envia automaticamente confirmações por e-mail para os clientes. Quando os usuários recebem as confirmações de e-mail com um link URL, para confirmar a assinatura, os invasores modificam o link URL. 

Essas modificações podem alterar o nome de usuário, o endereço de e-mail ou o status da assinatura dos clientes quando eles clicam para confirmar a assinatura. Dessa forma, quando o e-mail é retornado para o servidor host, ele recebe informações falsas, que podem não estar cientes se não verificar cada endereço de e-mail em relação às informações de assinatura.

Os hackers podem automatizar o ataque para inundar o aplicativo da Web com milhares de assinantes inválidos no banco de dados da newsletter.
