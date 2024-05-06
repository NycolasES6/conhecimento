# Salvando os resultados

## Formatos diferentes

Enquanto executamos várias verificações, devemos sempre salvar os resultados. Podemos usá-los posteriormente para examinar as diferenças entre os diferentes métodos de digitalização que usamos. Nmappode salvar os resultados em 3 formatos diferentes.

- Saída normal ( -oN) com a extensão **.nmap** de arquivo
- Saída Grepable ( -oG) com a extensão **.gnmap** de arquivo
- Saída XML ( -oX) com a extensão **.xml** do arquivo

Também podemos especificar a opção **-oA** para salvar o resultado em todos os formatos.



    NycolasES6@htb[/htb]$ sudo nmap 10.129.2.28 -p- -oA target

| Opções de digitação | Descrição                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------- |
| -oA target          | Salva os resultados em todos os formatos, iniciando o nome de cada arquivo com 'target'. |

Se nenhum caminho completo for fornecido, os resultados serão armazenados no diretório em que estamos.

### Saída normal

    NycolasES6@htb[/htb]$ cat target.nmap

### Sapida grepável

    NycolasES6@htb[/htb]$ cat target.gnmap

### Saída XML

    NycolasES6@htb[/htb]$ cat target.xml

## Folas de estilo

Com a saída XML, podemos criar facilmente relatórios HTML de fácil leitura, mesmo para pessoas não técnicas. Posteriormente, isso será muito útil para documentação, pois apresenta nossos resultados de forma detalhada e clara. Para converter os resultados armazenados do formato XML para HTML, podemos usar a ferramenta xsltproc.



```bash
NycolasES6@htb[/htb]$ xsltproc target.xml -o target.html
```


