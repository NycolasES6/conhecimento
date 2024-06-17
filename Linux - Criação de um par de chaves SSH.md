#Linux 
# Linux - Criação de um par de chaves SSH

Na linha de comando, gere um par de chaves SSH usando o comando `ssh-keygen` com a opção `-t ed25519` para escolher o algoritmo de criptografia `ed25519` e siga os prompts, aceitando todos os padrões. Você pode gerar um par de chaves apenas uma vez, pois pode usar o mesmo par de chaves para fazer login em vários servidores.

Opcionalmente, você pode definir uma senha ao criar um par de chaves SSH para obter uma camada de segurança adicional. Uma senha é algo que você configura para um par de chaves. Você deve inserir a senha toda vez que usar o par de chaves. Por padrão, os pares de chaves SSH não usam uma senha.

![[Pasted image 20240617140827.png]]

Verifique se o par de chaves `id_ed25519` existe usando a chave `ls` para visualizar o conteúdo do diretório oculto `~/.ssh`. O arquivo `id_ed25519` é a chave privada, e o arquivo `id_ed25519.pub` é a chave pública.

![[Pasted image 20240617140935.png]]