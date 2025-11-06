import pandas as pd

def mesclar_reorganizar_limpar(caminho_arq1, caminho_arq2, caminho_saida, coluna_id):
    # Lê os dois CSVs
    df1 = pd.read_csv(caminho_arq1)
    df2 = pd.read_csv(caminho_arq2)

    # Remove a primeira linha (cabeçalho) de cada CSV
    df1 = df1.iloc[1:]
    df2 = df2.iloc[1:]

    # Padroniza colunas para poder mesclar corretamente
    df2 = df2.reindex(columns=df1.columns.union(df2.columns, sort=False))
    df1 = df1.reindex(columns=df1.columns.union(df2.columns, sort=False))

    # Mescla os dois arquivos (um embaixo do outro)
    df = pd.concat([df1, df2], ignore_index=True)

    # Ordena pelo ID
    df = df.sort_values(by=coluna_id, ascending=True)

    # Remove a primeira linha e a primeira coluna
    df = df.iloc[1:, 1:]

    # Salva o resultado final
    df.to_csv(caminho_saida, index=False)
    print(f"Arquivo final gerado: {caminho_saida}")

# Exemplo de uso:
# mesclar_reorganizar_limpar("arq1.csv", "arq2.csv", "saida.csv", "CD_LCTO_CONTABIL")
# 
# Para Windows, use raw strings (r"") ou barras duplas (\\):
# mesclar_reorganizar_limpar(r"C:\Users\Documents\arq1.csv", r"C:\Users\Documents\arq2.csv", r"C:\Users\Documents\saida.csv", "CD_LCTO_CONTABIL")
# ou
# mesclar_reorganizar_limpar("C:\\Users\\Documents\\arq1.csv", "C:\\Users\\Documents\\arq2.csv", "C:\\Users\\Documents\\saida.csv", "CD_LCTO_CONTABIL")
