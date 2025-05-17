import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime

ARQUIVO = "banco_de_dados.csv"

def bater_ponto():
    agora = datetime.now()
    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M:%S")
    tipo = "Entrada" if contar_registros_dia(data) % 2 == 0 else "Saída"

    registro = {"Data": data, "Hora": hora, "Tipo": tipo}
    
    try:
        df = pd.read_csv(ARQUIVO)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Data", "Hora", "Tipo"])
    
    df = pd.concat([df, pd.DataFrame([registro])], ignore_index=True)
    df.to_csv(ARQUIVO, index=False)
    
    messagebox.showinfo("Ponto Registrado", f"{tipo} registrada: {data} às {hora}")

def contar_registros_dia(data):
    try:
        df = pd.read_csv(ARQUIVO)
        return len(df[df["Data"] == data])
    except:
        return 0

def visualizar_historico():
    try:
        df = pd.read_csv(ARQUIVO)
        historico = df.tail(10).to_string(index=False)
        messagebox.showinfo("Últimos Pontos", historico)
    except FileNotFoundError:
        messagebox.showwarning("Aviso", "Nenhum ponto registrado ainda.")

# Interface
janela = tk.Tk()
janela.title("App de Bater Ponto")
janela.geometry("300x200")

titulo = tk.Label(janela, text="Registro de Ponto", font=("Helvetica", 16))
titulo.pack(pady=10)

botao_bater = tk.Button(janela, text="Bater Ponto", command=bater_ponto, height=2, width=20, bg='green', fg='white')
botao_bater.pack(pady=10)

botao_ver = tk.Button(janela, text="Ver Últimos Registros", command=visualizar_historico)
botao_ver.pack(pady=10)

janela.mainloop()

