# Trabalhando com web services

Outro componente essencial é a comunicação com os servidores web. Existem muitas maneiras diferentes de configurar servidores web em sistemas operacionais Linux. Um dos servidores web mais utilizados e difundidos, além do IIS e do Nginx, é o Apache. Para um servidor web Apache, podemos usar módulos apropriados, que podem criptografar a comunicação entre o navegador e o servidor web (mod_ssl), usar como servidor proxy (mod_proxy) ou realizar manipulações complexas de dados de cabeçalho HTTP (mod_headers) e URLs (mod_rewrite ).

O Apache oferece a possibilidade de criar páginas web dinamicamente usando linguagens de script do lado do servidor. As linguagens de script comumente usadas são PHP, Perl ou Ruby. Outras linguagens são Python, JavaScript, Lua e .NET, que podem ser usadas para isso. Podemos instalar o servidor web Apache com o seguinte comando.

`apt install apache2 -y`

Depois de iniciá-lo, podemos navegar usando nosso navegador até a página padrão (http://localhost).

## CURL

CURL é uma ferramenta que nos permite transferir arquivos do shell por meios de protocolos como HTTP, HTTPS, FTP, SFTP, FTPS ou SCP. Esta ferranebta dá-nos a possibilidade de controlar e de testar sites remotamente. Além do conteúdo dos servidores remotos, também podemos visualizar solicitações individuais para observar a comunicação do cliente e do servidor. Normalmente, CURL já está instalado na maioria dos sistemas Linux. Este é outro motivo crítico para nos familiarizarmos com esta ferramenta, pois ela pode fazilitar muito alguns processos posteriormente.

`$ http://localhost`

Na tag de título, podemos ver que é o mesmo texto do nosso navegador. Por isso nos permite inspecionar o código-fonte do site e obter informações dele.

## wget

Uma alternativa ao curl é a ferramenta wget. Com esta ferramenta podemos baixar arquivos de servidores FTP ou HTTP diretamente do terminal, e ela serve como um bom gerenciador de downloads. Se usarmos o wget da mesma forma, a diferença para o curl é que o conteúdo do site é baixado e armazenado localmente, conforme mostrado no exemplo a seguir.

`$ http://localhost`

## python3

Outra opção muito utilizada quando se trata de transferência de dados é o uso do Python 3. Neste caso, o diretório raiz do servidor web é onde o comando é executado para iniciar o servidor. Neste exemplo, estamos em um diretório onde o WordPress está instalado e contém um “readme.html”. Agora, vamos iniciar o servidor web Python 3 e ver se podemos acessá-lo usando o navegador.

`python3 -m http.server`

