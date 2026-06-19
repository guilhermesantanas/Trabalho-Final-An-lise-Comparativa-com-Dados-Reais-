# Trabalho Final — Recuperação da Informação (2026.1)

Disciplina: Recuperação da Informação
Curso: Bacharelado em Ciência de Dados e Machine Learning — CEUB
Professor: MSc. Weslley Rodrigues
Entrega e apresentação: 22/06/2026

Este repositório contém a consolidação, coleta e análise de dados exigidas para o Trabalho Final, integrando a pesquisa State of Data Brazil com dados reais de vagas de tecnologia.

---

## Como executar

Para reproduzir este projeto do zero, siga os passos abaixo estando na raiz do repositório:

# 1. Instalar dependências
pip install -r requirements.txt

# 2. Consolidar o State of Data (gera o .parquet em data/)
python src/coleta/consolida_state_of_data.py

# 3. Coletar a base externa (Vagas via API/Scraping)
python src/coleta/coleta_externa.py

# 4. Limpar e integrar
python src/limpeza/integra.py

# 5. Gerar o relatório
# Abra o arquivo relatorio.ipynb no Jupyter/VS Code e execute todas as células.

---

## Identificação do grupo

**Nome do grupo:** Data Mappers
**Tema / pergunta de pesquisa:** Quais são os principais desalinhamentos (gaps) entre as competências dominadas pelos profissionais de dados no Brasil e os requisitos técnicos exigidos pelas vagas ativas?
**Base externa escolhida (fonte + método de coleta):** API Pública do Adzuna (ou GitHub Jobs) coletada programaticamente via script Python (`requests`).

**Integrantes:**
| Nome | Matrícula | E-mail institucional | Usuário GitHub |
| :--- | :--- | :--- | :--- |
| [Nome 1] | [Matrícula] | `nome1@sempreceub.com` | `@usuario1` |
| [Nome 2] | [Matrícula] | `nome2@sempreceub.com` | `@usuario2` |
| [Nome 3] | [Matrícula] | `nome3@sempreceub.com` | `@usuario3` |
| [Nome 4] | [Matrícula] | `nome4@sempreceub.com` | `@usuario4` |

**Modelo(s) de RI utilizado(s):** Modelo Vetorial com ponderação TF-IDF (Term Frequency-Inverse Document Frequency).
**Resumo do projeto:** O trabalho integra a base State of Data Brazil (2021-2025) com vagas de tecnologia coletadas via API. Aplicamos o modelo vetorial TF-IDF para extrair a relevância de competências técnicas nas descrições de vagas e cruzamos com as habilidades autodeclaradas pelos profissionais, identificando lacunas no mercado.
