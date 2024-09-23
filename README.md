# Automatização de Envio de E-mails com Python

Este script em Python utiliza as bibliotecas Pandas e smtplib para automatizar o envio de e-mails. O código lê informações de uma planilha (CSV) e envia e-mails personalizados para cada destinatário.

## Pré-requisitos

- Python 3.0
- Biblioteca Pandas
  ```bash
  pip install pandas
- Conta de e-mail (neste exemplo, Gmail é utilizado)

## Configuração 
 ### Crie um arquivo CSV:
  Crie um arquivo CSV contendo as colunas 'Nome' e 'E-mail Alternativo'.
 ### Configurações do Código:
  - Atualize o caminho_do_csv no código para o caminho do seu arquivo CSV.
  - Substitua 'remetente' e 'Senha do email' nas configurações do e-mail.

## Observações 
- Certifique-se de ativar a opção "Acesso a apps menos seguros" na conta de e-mail se estiver usando o Gmail.
- Utilize senhas de aplicativo para autenticação se estiver usando autenticação em dois fatores.

## Execução 
 Execute o script Python:
 ```bash
 python script_email.py
