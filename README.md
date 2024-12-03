
# Projeto de Geração de Endereços Bitcoin e Verificação de Correspondência

Este projeto gera endereços Bitcoin a partir de frases mnemônicas BIP39 (12, 15, 21 e 24 palavras) e verifica se algum endereço gerado já existe em um arquivo fornecido. Caso haja uma correspondência, ele salva a mnemônica, chave privada e endereço em um arquivo. A interface gráfica exibe os endereços gerados em tempo real.

Endereços Ricos Bitcoin P2PHK : https://github.com/Pymmdrza/Rich-Address-Wallet

## Requisitos

- **Python 3.x**
- Bibliotecas Python:
  - `mnemonic`: Para gerar frases mnemônicas BIP39.
  - `ecdsa`: Para gerar chaves privadas e públicas usando o algoritmo ECDSA.
  - `base58`: Para codificação do endereço Bitcoin no formato P2PKH.
  - `tkinter`: Para criar a interface gráfica.
  
Instale as bibliotecas necessárias utilizando o `pip`:

```
pip install mnemonic ecdsa base58
```

*Nota: `tkinter` é uma biblioteca padrão do Python, então não é necessário instalá-la separadamente.*

## Funcionalidade

- O script gera **frases mnemônicas** com 12, 15, 21 ou 24 palavras, conforme especificado.
- Para cada frase mnemônica, o script gera:
  1. A chave privada correspondente.
  2. A chave pública associada.
  3. O endereço Bitcoin no formato P2PKH.
- O script **verifica se o endereço gerado já existe no arquivo `P2PKH.txt`**. Caso encontre uma correspondência, ele salva a mnemônica, chave privada e o endereço no arquivo `matches.txt`.
- **Interface gráfica** usando Tkinter:
  - Exibe os endereços gerados em quatro colunas, uma para cada tamanho de mnemônica.
  - A contagem de endereços encontrados é exibida em tempo real na interface.
  - O plano de fundo da interface é configurado para usar uma imagem (PNG ou GIF) presente no mesmo diretório do script.

## Como Usar

1. Coloque o arquivo `P2PKH.txt` (contendo uma lista de endereços Bitcoin a serem verificados) no mesmo diretório do script.
2. Execute o script. O programa irá gerar endereços Bitcoin e verificar se algum endereço gerado já existe no arquivo `P2PKH.txt`.
3. A interface gráfica será aberta, mostrando os endereços gerados em tempo real.
4. Quando um endereço gerado coincidir com um dos endereços existentes no arquivo `P2PKH.txt`, ele será registrado em um arquivo de saída `matches.txt`.
5. A interface continua gerando e verificando endereços até que o usuário feche a janela.

## Estrutura de Arquivos

```
/diretório_do_script
├── P2PKH.txt          # Arquivo de endereços Bitcoin para verificação
├── matches.txt        # Arquivo onde mnemônicas e endereços correspondentes são salvos
├── script.py          # Código Python para geração de endereços e verificação
└── imagem_de_fundo.png # Imagem de fundo opcional para a interface gráfica (formato PNG ou GIF)
```

## Observações

- O arquivo `P2PKH.txt` deve conter um endereço Bitcoin P2PKH por linha.
- O script pode ser ajustado para gerar um número maior ou menor de endereços por execução.
- Caso o arquivo de imagem de fundo (`imagem_de_fundo.png`) não seja encontrado no diretório, o script usará um fundo preto padrão.

## Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo `LICENSE` para mais detalhes.
