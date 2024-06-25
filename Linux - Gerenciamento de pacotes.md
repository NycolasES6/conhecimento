#Linux 
# Linux - Gerenciamento de pacotes

Os recursos que a maioria dos sistemas de gerenciamento de pacotes oferecem são:

- Download de pacote
- Resolução de dependência
- Um formato de pacote binário padrão
- Locais comuns de instalação e configuração
- Configuração e funcionalidade adicionais relacionadas ao sistema
- Controle de qualidade

Podemos usar muitos sistemas de gerenciamento de pacotes diferentes que cobrem diferentes tipos de arquivos como “.deb”, “.rpm” e outros. O requisito de gerenciamento de pacotes é que o software a ser instalado esteja disponível como um pacote correspondente. Normalmente, isso é criado, oferecido e mantido centralmente nas distribuições Linux. Desta forma, o software é integrado diretamente no sistema, e seus diversos diretórios são distribuídos por todo o sistema. O software de gerenciamento de pacotes recupera as alterações necessárias para a instalação do sistema do próprio pacote e, em seguida, implementa essas alterações para instalar o pacote com êxito. Se o software de gerenciamento de pacotes reconhecer que pacotes adicionais são necessários para o funcionamento adequado do pacote que ainda não foi instalado, uma dependência será incluída e avisará o administrador ou tentará recarregar o software ausente de um repositório, por exemplo, e instalar isso com antecedência.

Se um software instalado tiver sido excluído, o sistema de gerenciamento de pacotes retoma as informações do pacote, modifica-as com base em sua configuração e exclui os arquivos. Existem diferentes programas de gerenciamento de pacotes que podemos usar para isso. Aqui está uma lista de exemplos de tais programas:

|**Comando**|**Descrição**|
|---|---|
|`dpkg`|O `dpkg`é uma ferramenta para instalar, construir, remover e gerenciar pacotes Debian. O front-end principal e mais fácil de usar `dpkg`é o aptitude.|
|`apt`|Apt fornece uma interface de linha de comando de alto nível para o sistema de gerenciamento de pacotes.|
|`aptitude`|Aptitude é uma alternativa ao apt e é uma interface de alto nível para o gerenciador de pacotes.|
|`snap`|Instale, configure, atualize e remova pacotes snap. Os Snaps permitem a distribuição segura dos aplicativos e utilitários mais recentes para nuvem, servidores, desktops e Internet das Coisas.|
|`gem`|Gem é o front-end do RubyGems, o gerenciador de pacotes padrão do Ruby.|
|`pip`|Pip é um instalador de pacotes Python recomendado para instalar pacotes Python que não estão disponíveis no arquivo Debian. Ele pode funcionar com repositórios de controle de versão (atualmente apenas repositórios Git, Mercurial e Bazaar), registra extensivamente a saída e evita instalações parciais baixando todos os requisitos antes de iniciar a instalação.|
|`git`|Git é um sistema de controle de revisão distribuído, rápido e escalável, com um conjunto de comandos excepcionalmente rico que fornece operações de alto nível e acesso total aos componentes internos.|

É altamente recomendável configurar nossa máquina virtual (VM) localmente para experimentá-la. Vamos experimentar um pouco em nossa VM local e estendê-la com alguns pacotes adicionais. Primeiro, vamos instalar `git`usando

## Gerenciador de Pacotes Avançado (APT)

Distribuições Linux baseadas em Debian usam o gerenciador de pacotes `APT`. Um pacote é um arquivo contendo vários arquivos ".deb". O utilitário `dpkg` é usado para instalar programas do arquivo “.deb” associado. `APT` facilita a atualização e instalação de programas porque muitos programas têm dependências. Ao instalar um programa a partir de um arquivo ".deb" independente, podemos enfrentar problemas de dependência e precisar baixar e instalar um ou vários pacotes adicionais. `APT` torna isso mais fácil e eficiente ao agrupar todas as dependências necessárias para instalar um programa.

A maioria das distribuições Linux utiliza o repositório mais estável ou “principal”. Isso pode ser verificado visualizando o conteúdo do arquivo `/etc/apt/sources.list`. A lista de repositórios do Parrot OS está em `/etc/apt/sources.list.d/parrot.list`.

O APT usa um banco de dados chamado cache do APT. Isto é usado para fornecer informações sobre pacotes instalados em nosso sistema offline. Podemos pesquisar no cache do APT, por exemplo, para encontrar todos os pacotes `Impacket` relacionados.

```sh
$ apt-cache search impacket

impacket-scripts - Links to useful impacket scripts examples
polenum - Extracts the password policy from a Windows system
python-pcapy - Python interface to the libpcap packet capture library (Python 2)
python3-impacket - Python3 module to easily build and dissect network protocols
python3-pcapy - Python interface to the libpcap packet capture library (Python 3)
```

Podemos então visualizar informações adicionais sobre um pacote.

```sh
$ apt-cache show impacket-scripts
```

Também podemos listar todos os pacotes instalados.

```sh
$ apt list --installed
```

## DPKG

Também podemos baixar os programas e ferramentas dos repositórios separadamente. Neste exemplo, baixamos ‘strace’ para Ubuntu 18.04 LTS.

```sh
$ wget http://archive.ubuntu.com/ubuntu/pool/main/s/strace/strace_4.21-1ubuntu1_amd64.deb
```

Além disso, agora podemos usar ambos `apt` e `dpkg` para instalar o pacote. Como já trabalhamos com `apt`, passaremos `dpkg` ao próximo exemplo.

```sh
sudo dpkg -i strace_4.21-1ubuntu1_amd64.deb 
```















