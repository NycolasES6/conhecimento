#Linux #bash #programação 
# execução condicional bash

```bash
#!/bin/bash

# Check for given argument
if [ $# -eq 0 ]
then
	echo -e "You need to specify the target domain.\n"
	echo -e "Usage:"
	echo -e "\t$0 <domain>"
	exit 1
else
	domain=$1
fi
```

- `#!/bin/bash`- Shebang.
- `if-else-fi`- Execução condicional.
- `echo`- Imprime saída específica.
- `$#`// `$0`- `$1`Variáveis ​​especiais.
- `domain`- Variáveis.
- 
As condições das execuções condicionais podem ser definidas usando variáveis ​​( `$#`, `$0`, `$1`, `domain`), valores ( `0`) e strings, como veremos nos próximos exemplos. Esses valores são comparados com `comparison operators`( `-eq`) que veremos na próxima seção.