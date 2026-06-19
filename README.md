# Trabalho Final — Análise Comparativa com Dados Reais
## Disciplina: Ciência de Dados — 2026.1

### 👥 Identificação do Grupo e Integrantes
* **Integrante 1:** [Nome Completo] — `@sempreceub.com`
* **Integrante 2:** [Nome Completo] — `@sempreceub.com`
* **Integrante 3:** [Nome Completo] — `@sempreceub.com`
* **Integrante 4:** [Nome Completo] — `@sempreceub.com`

---

### 🎯 1. Objetivo do Trabalho e Pergunta de Pesquisa
O objetivo deste projeto é cruzar o panorama de competências dos profissionais de tecnologia no Brasil com as exigências atuais do mercado de trabalho.

* **Pergunta de Pesquisa:** *"Quais são os principais desalinhamentos (gaps) entre as competências dominadas pelos profissionais de dados no Brasil (série histórica State of Data) e os requisitos técnicos mais frequentes exigidos pelas vagas ativas capturadas via API/Web Scraping?"*

---

### 📁 2. Estrutura do Repositório
* `consolidar_state_of_data.py`: Script que automatiza a unificação das pesquisas State of Data (2021-2025) num arquivo `.parquet`.
* `coleta_base_externa.py`: Script de captura automatizada de vagas de tecnologia via API Pública / Web Scraping.
* `notebook_principal.ipynb`: Jupyter Notebook contendo a limpeza, integração, aplicação do Modelo Vetorial (TF-IDF) e as visualizações analíticas.
* `relatorio_analitico.pdf`: Relatório final estruturado para entrega.

---

### 🚀 3. Como Executar o Projeto (Reprodutibilidade)

#### Passo 1: Clonar o repositório e instalar dependências
```bash
git clone <link-do-seu-repositorio-privado>
cd <nome-do-repositorio>
pip install pandas pyarrow requests beautifulsoup4 scikit-learn matplotlib seaborn
