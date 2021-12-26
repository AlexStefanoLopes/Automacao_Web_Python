from selenium import webdriver

#Devido a já estar importando o webdriver, nem precisaria declarar o caminho nem a função executable_path
navegador = webdriver.Chrome(executable_path=r'C:\Users\Alex\PycharmProjects\AnaliseBonusViagem\venv\Scripts\chromedriver.exe')

navegador.get('https://ri.magazineluiza.com.br/')

#O Jupyter falar que find_element_by_xpath é obsoleto e diz para usar apenas find_element, mas não deu certo, mesmo copiando apenas como elemento o botão
navegador.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/a[2]/span').click()
