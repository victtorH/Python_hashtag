import pyautogui as pi
import time
import pandas as pd


# 1 passo entrar no google
pi.press("win")
pi.write("chome")
pi.press("enter")
pi.press("enter")
time.sleep(2)
pi.click(x=290, y=554)


# 2 passo entrar no sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login
time.sleep(2)
pi.hotkey('Ctrl','t')
pi.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pi.press("enter")
time.sleep(2)
pi.click(x=287, y=374)
pi.write("victtor12345678910@gmail.com")
pi.press("tab")
pi.write("1234")
pi.press("tab")
pi.press("enter")

# 3 passo colocar dado


tabela = pd.read_csv("Aula_1/produtos.csv")

for linha in tabela.index :
    time.sleep(0.5)
    pi.click(x=506, y=257)

    codigo = tabela.loc[linha, "codigo"]
    pi.write(str(codigo))
    pi.press("tab")

    marca = tabela.loc[linha, "marca"]
    pi.write(str(marca))
    pi.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pi.write(str(tipo))
    pi.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pi.write(str(categoria))
    pi.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pi.write(str(preco_unitario))
    pi.press("tab")

    custo = tabela.loc[linha, "custo"]
    pi.write(str(custo))
    pi.press("tab")

    obs = tabela.loc[linha, "obs"]
    pi.write(str(obs))
    pi.press("tab")
    pi.press("enter")
    pi.scroll(500)


# 4 passo mandar dado
# 5 passo repetir processos anteriores até o fim da lista