#redes
# Operação NAT

O roteador sem fio recebe um endereço público do ISP, que permite que ele envie e receba pacotes pela internet. Ele, por sua vez, fornece endereços privados para clientes da rede local.

O processo usado para converter endereços privados em endereços roteáveis pela Internet é chamado de NAT. Com o NAT, um endereço IPv4 de origem privado (local) é convertido em um endereço público (global). O processo é o inverso para pacotes que chegam. Usando NAT, o roteador sem fio é capaz de converter vários endereços IPv4 internos no mesmo endereço público.

Só precisam ser convertidos pacotes destinados para outras redes. Esses pacotes devem passar pelo gateway. Nele, o roteador sem fio substitui o endereço IPv4 privado do host de origem pelo seu próprio endereço IPv4 público.