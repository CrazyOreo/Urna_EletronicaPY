import tkinter as tk
from tkinter import messagebox
import pickle

# defindo os tipos dos arquivos 
FILE_ELEITORES = "eleitores.csv"
FILE_CANDIDATOS = "candidatos.csv"

# Estruturas de dados para eleitores e candidatos
eleitores = {}
candidatos = {}

# Classes para os Eleitores e Candidatos
class Eleitor:
    def __init__(self, nome, RG, CPF, titulo, secao, zona):
        self.nome = nome
        self.RG = RG
        self.CPF = CPF
        self.titulo = titulo
        self.secao = secao
        self.zona = zona

    def get_titulo(self):
        return self.titulo

    def __str__(self):
        return f"{self.nome}, RG: {self.RG}, CPF: {self.CPF}, Título: {self.titulo}, Seção: {self.secao}, Zona: {self.zona}"

class Candidato:
    def __init__(self, nome, RG, CPF, numero):
        self.nome = nome
        self.RG = RG
        self.CPF = CPF
        self.numero = numero

    def get_numero(self):
        return self.numero

    def __str__(self):
        return f"{self.nome}, RG: {self.RG}, CPF: {self.CPF}, Número: {self.numero}"

# Aqui é a função para manipular os eleitores e candidatos
def carregar_eleitores():
    try:
        with open(FILE_ELEITORES, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return {}

def carregar_candidatos():
    try:
        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_eleitores():
    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

def salvar_candidatos():
    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

# A Classe principal da interface
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Eleições")
        self.root.geometry("600x400") 
        self.create_main_menu()
        
# Menu Principal
    def create_main_menu(self):
        
        menu_label = tk.Label(self.root, text="Urna Eleitoral", font=("Arial", 16))
        menu_label.pack(pady=10)

        # Botões para cada funcionalidade
        tk.Button(self.root, text="Inserir Eleitor", command=self.inserir_eleitor).pack(fill="x", padx=50, pady=5)
        tk.Button(self.root, text="Atualizar Eleitor", command=self.atualizar_eleitor).pack(fill="x", padx=50, pady=5)
        tk.Button(self.root, text="Inserir Candidato", command=self.inserir_candidato).pack(fill="x", padx=50, pady=5)
        tk.Button(self.root, text="Listar Candidatos", command=self.listar_candidatos).pack(fill="x", padx=50, pady=5)
        tk.Button(self.root, text="Iniciar Urna", command=self.iniciar_urna).pack(fill="x", padx=50, pady=5)
        tk.Button(self.root, text="Carregar Dados", command=self.carregar_dados).pack(fill="x", padx=50, pady=5)
        tk.Button(self.root, text="Sair", command=self.root.quit).pack(fill="x", padx=50, pady=5)

    def carregar_dados(self):
        global eleitores, candidatos
        eleitores = carregar_eleitores()
        candidatos = carregar_candidatos()
        messagebox.showinfo("Carregar Dados", "Dados de eleitores e candidatos carregados com sucesso!")

# função para colocar eleitor
    def inserir_eleitor(self):
        inserir_window = tk.Toplevel(self.root)
        inserir_window.title("Inserir Eleitor")
        inserir_window.geometry("400x400")

        def inserir():
            try:
                titulo = int(titulo_entry.get())
                if titulo in eleitores:
                    raise Exception("Eleitor já existente!")

                nome = nome_entry.get()
                RG = RG_entry.get()
                CPF = CPF_entry.get()
                secao = int(secao_entry.get())
                zona = int(zona_entry.get())

                eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
                eleitores[eleitor.get_titulo()] = eleitor

                salvar_eleitores()

                messagebox.showinfo("Sucesso", "Eleitor inserido com sucesso!")
                inserir_window.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao inserir eleitor: {str(e)}")

        # Campos para inserir os dados do eleitor
        tk.Label(inserir_window, text="Digite o título do eleitor:").pack(pady=5)
        titulo_entry = tk.Entry(inserir_window)
        titulo_entry.pack(pady=5)

        tk.Label(inserir_window, text="Digite o nome do eleitor:").pack(pady=5)
        nome_entry = tk.Entry(inserir_window)
        nome_entry.pack(pady=5)

        tk.Label(inserir_window, text="Digite o RG do eleitor:").pack(pady=5)
        RG_entry = tk.Entry(inserir_window)
        RG_entry.pack(pady=5)

        tk.Label(inserir_window, text="Digite o CPF do eleitor:").pack(pady=5)
        CPF_entry = tk.Entry(inserir_window)
        CPF_entry.pack(pady=5)

        tk.Label(inserir_window, text="Digite a seção do eleitor:").pack(pady=5)
        secao_entry = tk.Entry(inserir_window)
        secao_entry.pack(pady=5)

        tk.Label(inserir_window, text="Digite a zona do eleitor:").pack(pady=5)
        zona_entry = tk.Entry(inserir_window)
        zona_entry.pack(pady=5)

        tk.Button(inserir_window, text="Inserir", command=inserir).pack(pady=10)

# função para atualizar
    def atualizar_eleitor(self):
        atualizar_window = tk.Toplevel(self.root)
        atualizar_window.title("Atualizar Eleitor")
        atualizar_window.geometry("400x300")

        # função que atualiza o eleitor e caso nao tenha exibe mensagem q nao a eleitor
        def atualizar():
            try:
                titulo = int(titulo_entry.get())
                if titulo not in eleitores:
                    raise Exception("Eleitor não encontrado!")

                eleitor = eleitores[titulo]
                secao = int(secao_entry.get())
                zona = int(zona_entry.get())

                eleitor.secao = secao
                eleitor.zona = zona

                salvar_eleitores()

                messagebox.showinfo("Sucesso", "Dados do eleitor atualizados com sucesso!")
                atualizar_window.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar eleitor: {str(e)}")

        tk.Label(atualizar_window, text="Digite o título do eleitor:").pack(pady=5)
        titulo_entry = tk.Entry(atualizar_window)
        titulo_entry.pack(pady=5)

        tk.Label(atualizar_window, text="Digite a nova seção:").pack(pady=5)
        secao_entry = tk.Entry(atualizar_window)
        secao_entry.pack(pady=5)

        tk.Label(atualizar_window, text="Digite a nova zona:").pack(pady=5)
        zona_entry = tk.Entry(atualizar_window)
        zona_entry.pack(pady=5)

        tk.Button(atualizar_window, text="Atualizar", command=atualizar).pack(pady=10)

  # Janela de Inserir Candidato 
    def inserir_candidato(self):
        inserir_window = tk.Toplevel(self.root)
        inserir_window.title("Inserir Candidato")
        inserir_window.geometry("400x300")

        # Função para inserir o candidato e caso ja tenha exibe mensagem que ja esta cadastrado 
        def inserir():
            try:
                numero = int(numero_entry.get())
                if numero in candidatos:
                    raise Exception("Candidato já existente!")

                nome = nome_entry.get()
                RG = RG_entry.get()
                CPF = CPF_entry.get()

                candidato = Candidato(nome, RG, CPF, numero)
                candidatos[candidato.get_numero()] = candidato

                salvar_candidatos()

                messagebox.showinfo("Sucesso", "Candidato inserido com sucesso!")
                inserir_window.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao inserir candidato: {str(e)}")

        # Campos para inserir os dados dos candidato
        tk.Label(inserir_window, text="Digite o número do candidato:").pack(pady=5)
        numero_entry = tk.Entry(inserir_window)
        numero_entry.pack(pady=5)

        tk.Label(inserir_window, text="Digite o nome do candidato:").pack(pady=5)
        nome_entry = tk.Entry(inserir_window)
        nome_entry.pack(pady=5)

        tk.Label(inserir_window, text="Digite o RG do candidato:").pack(pady=5)
        RG_entry = tk.Entry(inserir_window)
        RG_entry.pack(pady=5)

        tk.Label(inserir_window, text="Digite o CPF do candidato:").pack(pady=5)
        CPF_entry = tk.Entry(inserir_window)
        CPF_entry.pack(pady=5)

        tk.Button(inserir_window, text="Inserir", command=inserir).pack(pady=10)

    def listar_candidatos(self):
    # Criar a janela de candidatos
        lista_window = tk.Toplevel(self.root)
        lista_window.title("Lista de Candidatos")
        lista_window.geometry("400x400")

    # Verificar se existem candidatos cadastrados
        if candidatos:
        # Criar uma label para cada candidato com nome e número
            for idx, candidato in enumerate(candidatos.values()):
             tk.Label(lista_window, text=f"{candidato.nome} - Número: {candidato.numero}").pack(pady=5)
        else:
            # Caso não haja candidatos, exibir uma mensagem
            tk.Label(lista_window, text="Nenhum candidato cadastrado.").pack(pady=5)
            
    def iniciar_urna(self):
        urna_window = tk.Toplevel(self.root)
        urna_window.title("Urna Eletrônica")
        urna_window.geometry("400x300") 

        tk.Label(urna_window, text="Digite o número do candidato:").pack(pady=5)
        numero_entry = tk.Entry(urna_window, font=("Arial", 20), justify="center")
        numero_entry.pack(pady=5)

        # Função para adicionar o número ao campo de entrada
        def adicionar_numero(num):
            numero_entry.insert(tk.END, num)

        # Função para votar em branco
        def votar_branco():
            confirma = messagebox.askyesno("Confirmação", "Você está votando em branco. Confirmar?")
            if confirma:
                messagebox.showinfo("Voto registrado", "Voto em branco computado com sucesso!")
                urna_window.destroy()

        # Função para corrigir o número
        def corrigir():
            numero_entry.delete(0, tk.END)

        # Função para confirmar o voto
        def confirmar_voto():
            numero = numero_entry.get()
            if numero.isdigit() and int(numero) in candidatos:
                candidato = candidatos[int(numero)]
                confirma = messagebox.askyesno("Confirmação", f"Confirmar voto para {candidato.nome}?")
                if confirma:
                    messagebox.showinfo("Voto registrado", "Voto computado com sucesso!")
                    urna_window.destroy()
            else:
                messagebox.showerror("Erro", "Candidato não encontrado!")

        # Botões numéricos (0-9)
        botoes_frame = tk.Frame(urna_window)
        botoes_frame.pack(pady=10)

        for i in range(1, 10):
            tk.Button(botoes_frame, text=str(i), width=5, height=2,
                      command=lambda num=i: adicionar_numero(num)).grid(row=(i-1)//3, column=(i-1)%3)
        tk.Button(botoes_frame, text="0", width=5, height=2,
                  command=lambda: adicionar_numero(0)).grid(row=3, column=1)

        # Botões para Branco, Corrigir e Confirmar
        tk.Button(urna_window, text="Branco", command=votar_branco, bg="white").pack(side="left", padx=10, pady=5)
        tk.Button(urna_window, text="Corrigir", command=corrigir, bg="yellow").pack(side="left", padx=10, pady=5)
        tk.Button(urna_window, text="Confirmar", command=confirmar_voto, bg="green").pack(side="left", padx=10, pady=5)

# Função para iniciar o aplicativo
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()