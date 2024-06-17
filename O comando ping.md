#redes 
# O comando ping

Quando um ping é enviado para um endereço IP, um pacote conhecido como echo request é enviado através da rede para o endereço IP especificado. Se o host de destino receber o echo request, ele responderá com um pacote conhecido como echo reply. Se a origem receber o echo reply, a conectividade será verificada pela resposta do endereço IP específico. O ping não é bem-sucedido se uma mensagem como request timed out ou general failure for exibida.

Se um **ping** for enviado para um nome, como ww​w.cisco.com, um pacote será enviado primeiro para um servidor DNS para resolver o nome para um endereço IP. Depois que o endereço IP é obtido, o echo request é encaminhado para o endereço IP e o processo continua. Se um ping for bem-sucedido para o endereço IP, mas não for para o nome, talvez exista um problema com o DNS.