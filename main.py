import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, nome):
    corpo_email =f"""
    <p style="color: black;">

    Caro(a) {nome},<br><br>

    Escreve o texto aqui
</p>
    """

    msg = MIMEMultipart()
    msg['Subject'] = "Titulo do Email"
    msg['From'] = 'remetente'
    msg['To'] = destinatario

    corpo = MIMEText(corpo_email, 'html')
    msg.attach(corpo)

    password = 'Senha do email (pode ser a opção "senhas de App" para maior segurança)'

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    
    # Envie o e-mail
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    print(f'E-mail enviado para {destinatario}')

caminho_do_csv = 'arquivo.csv'

# Carregue o arquivo CSV usando o pandas
df = pd.read_csv(caminho_do_csv, encoding='iso-8859-1', delimiter=',')

# Itere sobre as linhas da planilha
for indice, linha in df.iterrows():
    # Acesse os valores das células usando os nomes das colunas
    nome = linha['Nome']
    email = linha['E-mail Alternativo']

    # Verifique se o campo de e-mail não está vazio
    if pd.notna(email):
        # Chame a função para enviar e-mail
        enviar_email(email, nome)
    else:
        print(f'Pular linha {indice + 1}: E-mail vazio')