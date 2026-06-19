import os
import glob
import pandas as pd

def consolidar_bases():
    print("=== Iniciando a Consolidação do State of Data Brazil ===")
    
    # Caminhos relativos à raiz do projeto (onde o professor vai rodar o comando)
    input_dir = "data/brutos"
    output_dir = "data"
    
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    arquivos_csv = glob.glob(os.path.join(input_dir, "state_of_data_*.csv"))
    
    if not arquivos_csv:
        print(f"❌ Nenhum CSV encontrado em '{input_dir}'.")
        return

    lista_dfs = []
    for arquivo in sorted(arquivos_csv):
        print(f"📦 Lendo: {os.path.basename(arquivo)}")
        # Extrai ano do nome do arquivo
        ano = int(''.join(filter(str.isdigit, os.path.basename(arquivo))))
        df = pd.read_csv(arquivo, low_memory=False)
        df['ano_pesquisa'] = ano
        lista_dfs.append(df)
        
    df_final = pd.concat(lista_dfs, ignore_index=True)
    caminho_parquet = os.path.join(output_dir, "state_of_data_2021_2025.parquet")
    
    # Salva o .parquet
    df_final.to_parquet(caminho_parquet, index=False, engine='pyarrow')
    print(f"✅ Arquivo consolidado salvo em: {caminho_parquet}")

if __name__ == "__main__":
    consolidar_bases()
