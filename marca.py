from PIL import Image, ImageDraw, ImageFont
import os
from colorama import Fore, Style, init

PASTA_INPUT = 'input'
PASTA_OUTPUT = 'output'
NOME_FONTE = 'arial.ttf'

def aplicar_marca_dagua():
    init(autoreset=True)
    print(Style.BRIGHT + Fore.CYAN + f"--- APLICADOR DE MARCA D'ÁGUA ---")

    texto_marca = input("Digite o texto da marca d'água: ").strip()
    if not texto_marca:
        print(Fore.RED + "O texto não pode estar vazio.")
        return
    
    posicoes = {
        '1': 'canto_superior_esquerdo', '2': 'canto_superior_direito',
        '3': 'canto_inferior_esquerdo', '4': 'canto_inferior_direito',
        '5': 'centro'
    }
    print("\nEscolha a posição em que a marca d'água irá ficar: ")
    for num, pos in posicoes.items():
        print(f"[{num}] {pos.replace('_', ' ').title()}")

    while True:
        escolha_pos = input("Digite o número da posição: ")
        if escolha_pos in posicoes:
            posicao_escolhida = posicoes[escolha_pos]
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")
        
    while True:
        try:
            angulo = int(input("Digite o ângulo de inclinação (Ex: 45 para diagonal, 0 para reto): "))
            break
        except ValueError:
            print(Fore.RED + "Por favor, digite um número inteiro para o ângulo.")

    while True:
        try:
            tamanho_fonte = int(input("Digite o tamanho da fonte: "))
            break
        except ValueError:
            print(Fore.RED + "Por favor, digite um número inteiro para o tamanho da fonte.")

    if not os.path.exists(PASTA_OUTPUT):
        os.makedirs(PASTA_OUTPUT)
    
    print(Fore.YELLOW + "\nProcessando...")
    arquivos_processados = 0
    for nome_arquivo in os.listdir(PASTA_INPUT):
        caminho_arquivo_origem = os.path.join(PASTA_INPUT, nome_arquivo)

        try:
            with Image.open(caminho_arquivo_origem).convert("RGBA") as imagem_base:
                largura_img, altura_img = imagem_base.size

                txt_canvas = Image.new('RGBA', (largura_img, altura_img), (255, 255, 255, 0))
                
                desenho = ImageDraw.Draw(txt_canvas)
                try:
                    fonte = ImageFont.truetype(NOME_FONTE, tamanho_fonte)
                except IOError:
                    fonte = ImageFont.load_default()

                caixa_texto = desenho.textbbox((0, 0), texto_marca, font=fonte)
                largura_txt = caixa_texto[2] - caixa_texto[0]
                altura_txt = caixa_texto[3] - caixa_texto[1]

                pos_texto_inicial = ((largura_img - largura_txt) // 2, (altura_img - altura_txt) // 2)
                desenho.text(pos_texto_inicial, texto_marca, font=fonte, fill=(255, 255, 255, 128))

                if angulo != 0:
                    txt_canvas = txt_canvas.rotate(angulo, expand=True)

                margem = 10
                if posicao_escolhida == 'canto_superior_esquerdo':
                    pos_final = (margem, margem)
                elif posicao_escolhida == 'canto_superior_direito':
                    pos_final = (largura_img - txt_canvas.width + margem, margem)
                elif posicao_escolhida == 'canto_inferior_esquerdo':
                    pos_final = (margem, altura_img - txt_canvas.height + margem)
                elif posicao_escolhida == 'canto_inferior_direito':
                    pos_final = (largura_img - txt_canvas.width - margem, altura_img - txt_canvas.height - margem)
                elif posicao_escolhida == 'centro':
                    pos_final = ((largura_img - txt_canvas.width) // 2, (altura_img - txt_canvas.height) // 2)
                
                imagem_base.paste(txt_canvas, pos_final, txt_canvas)
                
                imagem_final = imagem_base.convert("RGB")
                
                caminho_arquivo_destino = os.path.join(PASTA_OUTPUT, nome_arquivo)
                imagem_final.save(caminho_arquivo_destino)
                arquivos_processados += 1
                print(f" -> Marca d'água aplicada em: {nome_arquivo}")

        except IOError:
            print(Fore.YELLOW + f"Arquivo '{nome_arquivo}' não é uma imagem válida e será ignorado.")
            
    if arquivos_processados > 0:
        print(Style.BRIGHT + Fore.GREEN + f"\n✅ Sucesso! {arquivos_processados} imagens foram processadas e salvas em '{PASTA_OUTPUT}'.")
    else:
        print(Fore.RED + "Nenhuma imagem foi encontrada na pasta 'input'.")

if __name__ == "__main__":
    aplicar_marca_dagua()
    input("\nPressione Enter para sair.")