
## Inicial

```
Router>enable
	   en
```
Entra no privilegiado

```
Router#configure terminal
	   conf t
```
Entra no modo de configuração

```
Router (config) #hostname Roteador_1
```
Define o hostname para Roteador_1

## Senhas

```
Roteador_1 (config) #enable password cisco
```
Seta uma senha para o enable, mas não criptografa ela

```
Roteador_1 (config) #enable secret cisco
```
Seta uma senha para o enable, e a criptografa


## Mostrar as configurações atuais

```
Roteador_1#show running-config 
```
Mostra as configurações atuais
## Salvar as configurações atuais

```
Roteador_1#copy running-config startup-config

Roteador_1#write
```
As duas opções tem o mesmo efeito






























