📊 Análise Financeira - Microsoft Financial Sample
Este projeto é uma aplicação web interativa desenvolvida com Streamlit para análise de dados financeiros de amostra da Microsoft.

🧾 Funcionalidades
Visualização de métricas financeiras como vendas, lucro, descontos e custo de produção.

Filtros interativos por ano, segmento, país e outros.

Gráficos dinâmicos com Matplotlib e Seaborn.

Layout responsivo via streamlit.set_page_config(layout="wide").

📁 Estrutura do Projeto
bash
Copiar
Editar
prova/
├── app.py                  # Aplicação Streamlit principal
├── 1.png, 2.png            # Imagens de apoio (potencialmente para o app)
├── ec2-keys.pem            # Chave PEM (⚠️ não deve ser versionada publicamente)
├── README.md               # Documentação original (possivelmente desatualizada)
├── .git/                   # Repositório Git
🚀 Como Executar
⚠️ Certifique-se de que o arquivo MS_Financial Sample.csv está presente no mesmo diretório do app.py.

Crie um ambiente virtual e ative-o:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
Instale as dependências:

bash
Copiar
Editar
pip install streamlit pandas matplotlib seaborn
Execute o app:

bash
Copiar
Editar
streamlit run app.py
