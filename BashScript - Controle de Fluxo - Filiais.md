# BashScript - Controle de Fluxo - Filiais

## Case Statements

Instruções `Case` também são conhecidas como instruções `switch-case` em outras linguagens, como C/C++ e C#.

A principal diferença entre `if-else` e `switch-case` é que `if-else` as construções nos permitem verificar qualquer expressão booleana, enquanto `switch-case` sempre compara apenas a variável com o valor exato.

Portanto, as mesmas condições de `if-else`, como "maior que", não são permitidas para `switch-case`. A sintaxe para as instruções switch-case é semelhante a esta:

### Sintaxe - Switch-Case

```bash
case <expression> in
	pattern_1 ) statements ;;
	pattern_2 ) statements ;;
	pattern_3 ) statements ;;
esac
```

A definição de switch-case começa com `case`, seguida pela variável ou valor como uma expressão, que é então comparada no padrão.

Se a variável ou valor corresponder à expressão, as instruções serão executadas após os parênteses e terminarão com ponto-e-vírgula duplo ( `;;`).

Em nosso script `CIDR.sh`, usamos essa afirmação `case`. Aqui definimos quatro opções diferentes que atribuímos ao nosso roteiro, como ele deve proceder após a nossa decisão.

### CIDR.sh

```bash
<SNIP>
# Available options
echo -e "Additional options available:"
echo -e "\t1) Identify the corresponding network range of target domain."
echo -e "\t2) Ping discovered hosts."
echo -e "\t3) All checks."
echo -e "\t*) Exit.\n"

read -p "Select your option: " opt

case $opt in
	"1") network_range ;;
	"2") ping_host ;;
	"3") network_range && ping_host ;;
	"*") exit 0 ;;
esac
<SNIP>
```





















