#SO #Windows 
# Fluxos de Dados Alternativos

NTFS armazena arquivos como uma série de atributos, como o nome do arquivo ou um carimbo de data/hora. Os dados que o arquivo contém são armazenados no atributo $DATA, e é conhecido como um fluxo de dados. Usando NTFS, você pode conectar fluxos de dados alternativos (ADSs) ao arquivo. Às vezes, isso é usado por aplicativos que estão armazenando informações adicionais sobre o arquivo. O ADS é um fator importante ao discutir malware. Isso ocorre porque é fácil ocultar dados em um ADS. Um invasor pode armazenar código mal-intencionado dentro de um ADS que pode ser chamado de um arquivo diferente.

No sistema de arquivos NTFS, um arquivo com um ADS é identificado após o nome do arquivo e dois pontos, por exemplo, **Testfile.txt:ADS.** Este nome de arquivo indica que um ADS chamado ADS está associado ao arquivo chamado **Testfile.txt.** Um exemplo de ADS é mostrado na saída do comando.

```sh
C:∖ADS> echo "Alternate Data Here" > Testfile.txt:ADS

C:∖ADS> dir

  Volume in drive C is Windows

  Volume Serial Number is A606-CB1B

  Directory of C:∖ADS

2020-04-28 04:01 PM   <DIR>            .

2020-04-28 04:01 PM   <DIR>            ..

2020-04-28 04:01 PM            0 Testfile.txt

                 1 File(s)                 0 bytes

                 2 Dir(s) 43,509,571,584 bytes free

C:∖ADS> more < Testfile.txt:ADS

"Alternate Data Here"

C:∖ADS> dir /r

   Volume in drive C is Windows

   Volume Serial Number is A606-CB1B

   Directory of C:∖ADS

2020-04-28 04:01 PM   <DIR>

2020-04-28 04:01 PM   <DIR>

2020-04-28 04:01 PM            0 Testfile.txt

                            24 Testfile.txt:ADS:$DATA

            1 File(s)            0 bytes

            2 Dir(s) 43,509,624,832 bytes free

C:∖ADS>
```

Na saída:

- O primeiro comando coloca o texto “Dados Alternativos Aqui” em um ADS do arquivo Testfile.txt chamado “ADS”.
- Depois disso, **dir**, mostra que o arquivo foi criado, mas o ADS não está visível.
- O próximo comando mostra que há dados no fluxo de dados Testfile.txt: ADS.
- O último comando mostra o ADS do arquivo Testfile.txt porque a opção **r** foi usada com o comando **dir**.





























