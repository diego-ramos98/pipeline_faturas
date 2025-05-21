# 💸 Pipeline de Controle de Gastos Automatizado

# Em desenvolvimento

Este projeto tem como objetivo automatizar o controle de gastos pessoais, substituindo o processo manual anteriormente utilizado. O pipeline é composto pelas etapas clássicas de ETL (Extração, Transformação e Carga), além de visualização e orquestração automatizada.

---

## 📦 Tecnologias Utilizadas

- 📧 [imap-tools](https://github.com/ikvk/imap_tools) – Extração de anexos de faturas e contas via e-mail.
- ⚙️ Apache Spark – Processamento e transformação dos dados.
- 📊 Microsoft Excel / Power BI – Visualização e análise dos dados.
- ⏱ Apache Airflow – Orquestração e automação do pipeline.

---

## 🔄 Etapas do Pipeline

### 1. Extração (Extract)
- Acessa automaticamente a conta de e-mail.
- Extrai os anexos de faturas e outras contas recebidas.
- Utiliza a biblioteca `imap_tools` para lidar com o protocolo IMAP.

### 2. Transformação (Transform)
- Os arquivos extraídos são processados com **Apache Spark**.
- Os dados são limpos, padronizados e enriquecidos.
- Essa etapa é utilizada para estudo prático dos conceitos do Spark.


### 3. Carga (Load)
- Os dados tratados são carregados para arquivos locais ou banco de dados.
- Essa etapa também é feita com Apache Spark, integrando as transformações.

### 4. Visualização 
- Utilização do **Excel** e **Power BI** para análise dos gastos.
- Criação de dashboards e gráficos para acompanhar os gastos mensais.

### 5. Automação (Será desenvolvida)
- O **Apache Airflow** será utilizado para agendar e automatizar todo o fluxo do pipeline.
- Garante que a extração, transformação, carga e visualizações sejam atualizadas automaticamente.

---

## 🧪 Próximos Passos

- ✅ Adicionar testes unitários nas etapas de extração e transformação.
- ✅ Automatizar execução diária/semanal com Apache Airflow.
- ✅ Colocar o projeto em produção em um servidor local.

---

## 🧠 Objetivo Educacional
Este projeto também tem fins educacionais, sendo utilizado para praticar:

- Processamento de dados com Apache Spark.

- Automatização de workflows com Apache Airflow.

- Criação de relatórios dinâmicos com ferramentas de BI.

- Boas práticas com testes e organização de pipelines de dados.

---

## 📁 Estrutura do Projeto

```plaintext
pipeline_faturas/
├── models/             # Entidades
├── notebooks/          # Notebooks Jupyter
├── scripts/            # Scripts de extração,transformação de dados e carregamento
│   └── extracts/
├── main.py             # Script principal para execução do pipeline
├── .gitignore          # Arquivos e pastas ignorados pelo Git
└── README.md           # Documentação do projeto



