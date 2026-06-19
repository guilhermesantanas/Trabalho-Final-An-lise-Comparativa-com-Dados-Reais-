import os
import pandas as pd

def limpar_e_integrar():
    print("=== Iniciando Limpeza e Integração das Bases ===")
    
    caminho_vagas = "data/vagas_raw.csv"
    caminho_state = "data/state_of_data_2021_2025.parquet"
    
    if not os.path.exists(caminho_vagas) or not os.path.exists(caminho_state):
        print("❌ Arquivos não encontrados. Rode os scripts de coleta primeiro.")
        return

    # 1. Carrega os dados
    df_vagas = pd.read_csv(caminho_vagas)
    df_state = pd.read_parquet(caminho_state)
    
    print("🧹 Padronizando textos e tratando nulos...")
    
    # 2. Limpeza textual básica nas vagas para o modelo de RI
    df_vagas['descricao_limpa'] = df_vagas['descricao'].str.lower()
    df_vagas['descricao_limpa'] = df_vagas['descricao_limpa'].str.replace('[^\w\s]', '', regex=True)
    
    # 3. Integração (exemplo: filtrando apenas perfis de dados compatíveis com as vagas)
    # Aqui criamos um subset preparado para a análise final no notebook
    df_integrado_vagas = df_vagas.copy()
    
    caminho_saida = "data/base_integrada_limpa.csv"
    df_integrado_vagas.to_csv(caminho_saida, index=False)
    
    print(f"✅ Bases limpas e preparadas. Salvo em: {caminho_saida}")

if __name__ == "__main__":
    limpar_e_integrar()
