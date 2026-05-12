import re
import csv

def html_para_csv(caminho_html, caminho_csv):
	with open(caminho_html, 'r', encoding='utf-8') as f:
		html_content = f.read()

	# Busca todos os links no formato padrão de favoritos do navegador
	padrao = re.compile(r'<A\s+HREF="([^"]+)"[^>]*>(.*?)</A>', re.IGNORECASE)
	matches = padrao.findall(html_content)

	# Prepara os dados para o CSV
	dados_csv = [['Nome', 'Link']]
	for match in matches:
			url = match[0]
			nome = match[1].strip()
			dados_csv.append([nome, url])

	# Cria o arquivo CSV separado por ponto e vírgula
	with open(caminho_csv, 'w', newline='', encoding='utf-8') as f:
			writer = csv.writer(f, delimiter=';')
			writer.writerows(dados_csv)

	print(f"Sucesso! {len(matches)} mangás foram extraídos para o arquivo '{caminho_csv}'.")

# Executa a extração
html_para_csv('doc/mangas/favoritos_mangas.html', 'doc/mangas/mangas_extraidos.csv')