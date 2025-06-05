<h1 align="center">📊 Análise Financeira — Microsoft Financial Sample</h1> <p align="center"> Uma aplicação web interativa feita com <strong>Streamlit</strong> para análise de dados financeiros da Microsoft. <br> Visualize métricas, filtre dados, e explore insights de forma rápida e dinâmica. </p>

🛠️Ferramentas e Bibliotecas Utilizadas:

AWS EC2
Git
Python
Streamlit
Pandas
Matplotlib
Seaborn 

🔄️Passo a passo para rodar a aplicação

Criar a instância EC2 na AWS
Escolha a AMI (Ubuntu, Amazon Linux, Debian, etc).

Configure o grupo de segurança liberando as portas

22 (SSH) para acesso remoto
8501 para acesso ao Streamlit.
Faça o download da chave .pem para acesso via SSH.

Conectar à instância via SSH

ssh -i "minhachave.pem" usuario@<IP-da-instância>
Instalar Git

sudo apt update
sudo apt install git -y
Clonar o repositório do projeto

git clone https://github.com/usuario/repositorio.git


Instalar Python e bibliotecas necessárias


sudo apt install python3 python3-pip -y
pip3 install streamlit pandas altair
Rodar o app Streamlit

streamlit run app.py --server.port 8501 --server.address 0.0.0.0

Acesse a aplicação via browser:

http://<IP-da-instância>:8501
🗃️Arquivos principais
app.py (o app principal que tem os dashboards)

MS_Financial Sample.csv
