#cyber #SO 
# Criptografia de host

O recurso Sistema de arquivos de criptografia do Windows (EFS) permite que os usuários criptografem arquivos, pastas ou um disco rígido inteiro. A criptografia de disco completa (FDE) criptografa todo o conteúdo de uma unidade (incluindo arquivos temporários e memória). O Microsoft Windows usa o **BitLocker** para FDE.

Antes de usar o BitLocker, o usuário precisa ativar o TPM (Trusted Platform Module, Módulo de plataforma confiável) na BIOS. TPM é um chip específico na placa-mãe que armazena informações específicas do sistema computacional como chaves de criptografia, certificados digitais e senhas. Quando ativado, o BitLocker pode usar o chip do TPM.

Da mesma forma, o **BitLocker To Go** é uma ferramenta que criptografa unidades removíveis. Ele não usa um chip TPM, mas ainda criptografa os dados, exigindo uma senha para descriptografá-los. Enquanto isso, uma unidade de autocriptografia criptografa automaticamente todos os dados na unidade para impedir que os invasores acessem os dados pelo sistema operacional.




















