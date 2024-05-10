#redes 

# CSMA CA

As WLANs são configurações de mídia compartilhada half-duplex. Half-duplex significa que apenas um cliente pode transmitir ou receber a qualquer momento. Mídia compartilhada significa que todos os clientes sem fio podem transmitir e receber no mesmo canal de rádio. Isso cria um problema porque um cliente sem fio não pode ouvir enquanto está enviando, o que torna impossível detectar uma colisão.

Para resolver esse problema, as WLANs usam o acesso múltiplo com detecção de operadora com prevenção de colisão (CSMA / CA) como o método para determinar como e quando enviar dados na rede. Um cliente sem fio faz o seguinte:

1. Ouve o canal para ver se ele está ocioso, o que significa que nenhum outro tráfego está atualmente no canal. O canal também é chamado de portadora.
2. Envia uma mensagem pronta para enviar (RTS) para o ponto de acesso para solicitar acesso dedicado à rede.
3. Recebe uma mensagem clara para enviar (CTS) do ponto de acesso que concede acesso ao envio.
4. Se o cliente sem fio não receber uma mensagem CTS, ele aguardará um período aleatório antes de reiniciar o processo.
5. Depois de receber o CTS, ele transmite os dados.
6. Todas as transmissões são confirmadas. Se um cliente sem fio não receber uma confirmação, ele assume uma colisão e reinicia o processo.















