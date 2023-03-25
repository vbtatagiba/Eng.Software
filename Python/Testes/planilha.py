import pandas as pd

# Cria um dicionário com as informações de instalação
instalacoes = {
    'Nome do Cliente': ['Cliente A', 'Cliente B', 'Cliente C'],
    'Local da Instalação': ['Rua A, 123', 'Rua B, 456', 'Rua C, 789'],
    'Data e Horário': ['01/01/2022 09:00', '02/01/2022 14:00', '03/01/2022 10:30'],
    'Valor do Serviço': [1000, 1500, 800],
    'Técnico Responsável': ['Técnico 1', 'Técnico 2', 'Técnico 3']
}

# Cria um DataFrame a partir do dicionário
df = pd.DataFrame(instalacoes)

# Cria um arquivo do Excel e grava o DataFrame na planilha "Instalações"
with pd.ExcelWriter('instalacoes.xlsx') as writer:
    df.to_excel(writer, sheet_name='Instalações', index=False)

    # Formata a planilha
    workbook = writer.book
    worksheet = writer.sheets['Instalações']
    header_format = workbook.add_format({'bold': True, 'bg_color': '#C0C0C0', 'align': 'center'})
    worksheet.set_column('A:E', 20)
    worksheet.set_row(0, None, header_format)
