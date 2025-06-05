<h1 align="center">📊 Análise Financeira — Microsoft Financial Sample</h1> <p align="center"> Uma aplicação web interativa feita com <strong>Streamlit</strong> para análise de dados financeiros da Microsoft. <br> Visualize métricas, filtre dados, e explore insights de forma rápida e dinâmica. </p>
🧰 Funcionalidades
✅ Visualização de métricas financeiras como:

Vendas
Lucro
Descontos
Custo de produção

✅ Filtros interativos por:

Ano
Segmento
País

✅ Visualizações com:

📈 Matplotlib

📊 Seaborn

✅ Layout moderno e responsivo via:

st.set_page_config(layout="wide")
📁 Estrutura do Projeto
prova/
├── app.py              # Aplicação principal em Streamlit
├── 1.png, 2.png        # Imagens de apoio (ex: gráficos, interface)
├── ec2-keys.pem        # 🔒 Chave PEM (⚠️ não versionar publicamente!)
├── README.md           # Este arquivo
├── .git/               # Diretório Git
🚀 Como Executar
⚠️ Certifique-se de que o arquivo MS_Financial Sample.csv está presente no mesmo diretório do app.py.

1️⃣ Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
2️⃣ Instale as dependências
pip install streamlit pandas matplotlib seaborn
3️⃣ Execute a aplicação
streamlit run app.py
