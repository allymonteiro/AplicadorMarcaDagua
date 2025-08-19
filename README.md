# 🖼️ Ferramenta de Marca d'Água para Imagens

Um aplicativo de linha de comando feito em Python que aplica marcas d'água de texto personalizáveis em várias imagens. Ideal para fotógrafos e criadores de conteúdo protegerem seus trabalhos.

## ✨ Funcionalidades

- **Totalmente Interativo:** O usuário define o texto, a posição, o ângulo de inclinação e o tamanho da fonte.
- **Posicionamento Flexível:** Oferece um menu para escolher a posição da marca d'água (cantos ou centro).
- **Rotação de Texto:** Permite inclinar o texto em qualquer ângulo para um efeito diagonal.
- **Processamento em Lote:** Aplica a mesma marca d'água em todas as imagens de uma pasta `input` e as salva em uma pasta `output`.

## ⚙️ Configuração (Para Rodar do Código-Fonte)

1. Clone este repositório.
2. **Importante:** Coloque um arquivo de fonte (ex: `arial.ttf`) na pasta principal do projeto.
3. Crie e ative um ambiente virtual.
4. Instale as dependências: `pip install -r requirements.txt`
5. Coloque as imagens que deseja processar na pasta `input`.
6. Execute o script: `python marca.py` e siga as instruções!

## 🚀 Como Usar (Versão Executável para Windows)

1. Vá para a **[Página de Releases](LINK_DA_SUA_RELEASE_AQUI)**.
2. Baixe o arquivo `marca.exe`.
3. Coloque o `.exe` em uma pasta. Crie uma subpasta `input` ao lado dele e adicione suas imagens.
4. Dê dois cliques no `.exe` para executar. As imagens com marca d'água aparecerão em uma nova pasta `output`.