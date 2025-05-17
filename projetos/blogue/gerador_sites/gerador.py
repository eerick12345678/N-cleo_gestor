import os
import random

# Lista de temas e títulos possíveis
temas = {
    "hacker": {
        "titulo": "Ferramentas Hacker Avançadas",
        "descricao": "Conheça as ferramentas mais poderosas do submundo digital!",
        "cor": "#0f0f0f",
        "fundo": "#121212",
        "categoria": "Hacking"
    },
    "filmes": {
        "titulo": "Top 10 Filmes Proibidos",
        "descricao": "Assista agora os filmes que foram censurados no mundo!",
        "cor": "#111",
        "fundo": "#000",
        "categoria": "Filmes"
    },
    "animes": {
        "titulo": "Animes Ocultos que Ninguém Conhece",
        "descricao": "Descubra os animes mais obscuros já criados!",
        "cor": "#1a1a1a",
        "fundo": "#080808",
        "categoria": "Animes"
    },
    "apps": {
        "titulo": "Apps Hacker para Android",
        "descricao": "Baixe os aplicativos mais insanos de hacking!",
        "cor": "#101010",
        "fundo": "#000000",
        "categoria": "Aplicativos"
    }
}

# Links ShrinkMe que você já tem
links = [
    "https://shrinkme.ink/IxJrV",
    "https://shrinkme.ink/OP9GZc"
]

# Gerador
def gerar_site():
    tema = random.choice(list(temas.keys()))
    info = temas[tema]
    titulo = info["titulo"]
    descricao = info["descricao"]
    cor = info["cor"]
    fundo = info["fundo"]
    categoria = info["categoria"]
    link = random.choice(links)

    html = f"""
    <html>
    <head>
        <title>{titulo}</title>
        <style>
            body {{
                background: {fundo};
                color: {cor};
                font-family: monospace;
                text-align: center;
                padding: 40px;
            }}
            a {{
                color: #00ff99;
                font-size: 22px;
                display: block;
                margin-top: 40px;
            }}
        </style>
    </head>
    <body>
        <h1>{titulo}</h1>
        <p>{descricao}</p>
        <a href="{link}" target="_blank">Acessar Conteúdo</a>
        <p style="margin-top:60px;font-size:12px;">Categoria: {categoria}</p>
    </body>
    </html>
    """

    nome_arquivo = f"{tema}_{random.randint(1000,9999)}.html"
    caminho = os.path.join("sites_gerados", nome_arquivo)
    with open(caminho, "w") as f:
        f.write(html)

    print(f"[+] Site gerado: {caminho}")

# Criar vários de uma vez
for _ in range(5):
    gerar_site()
