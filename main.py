import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1545945cf6c1f2b39fca419901018207"
# Your Auth Token from twilio.com/console
auth_token  = "9eaba67c7dfef1fd114a285eed46d7b5"
client = Client(account_sid, auth_token)

lista_meses = ['Janeiro', 'Fevereiro']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)

    if (tabela_vendas['Vendas'] > 55000).any():   # .any é para ver se tem ALGUM valor naquela condição
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]  #.values[0] é só para dizer que não queremos a tabela que o .loc dá automaticamente, mas sim apenas o valor
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]   # .loc é para pegar naquela respectiva linha da tabela
        print(f' No mes de {mes} o Vendendor: {vendedor}, bateu a meta acima de 55000, vendendo {vendas}')
        message = client.messages.create(
            to="+5543999333578",  # Numero para quem quer enviar a mensagem
            from_="+(505) 539-1169", #Pegar o número gerado pelo Twilio no site
            body=f' No mes de {mes} o Vendendor: {vendedor}, bateu a meta acima de 55000, vendendo {vendas}')

        print(message.sid)