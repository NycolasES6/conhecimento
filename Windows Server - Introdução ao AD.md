# Windows Server - Introdução ao AD

## Active Directory (AD)

- Banco de dados para armazenamento dos objetos no domínio.
- Os controladores de domínio(CD) hospedam esse banco de dados.
- Os computadores de domínio confiam nas informações presentes no AD.

## Exemplo de estrutura do AD

Aqui temos um domínio raiz, com uma estrutura de rede.

---

A empresa pode ter um domínio raiz, e todos os usuários pertencerem a este domínio raiz.

![[Pasted image 20240620143046.png]]

---

Mas também pode ter um domínio filho, com outra infraestrutura separada, mas pertence ao mesmo domínio raiz.

![[Pasted image 20240620143402.png]]

---

Você também pode ter uma segunda empresa com um nome diferente, que tem seu próprio domínio, mas pertencente as configurações do domínio raiz.

![[Pasted image 20240620143648.png]]

---

E essa empresa 2, pode ter também um domínio filho.

![[Pasted image 20240620143748.png]]

## Árvores

Dessa maneira, temos o que o AD chama de árvores.

![[Pasted image 20240620143909.png]]

Sempre que tivermos mais de uma árvore, temos uma floresta, com um domínio raiz.