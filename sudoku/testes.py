import customtkinter as ctk
import gen_sudoku as gsdk
import game as gm

diff = 0

def seletor_dificuldade(choice):
    global diff  
    match choice:
        case "Fácil":
            diff = 40
        case "Normal":
            diff = 49
        case "Difícil":
            diff = 56
        case "Impossível":
            diff = 60
        case _:
            diff = 49
    print(diff)

def iniciar_jogo():
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    gsdk.gerar_completo(tabuleiro)
    solucao = [[0 for _ in range(9)] for _ in range(9)]
    gsdk.copiar_tabuleiro(tabuleiro, solucao)
    
    gsdk.criar_desafio(tabuleiro, diff)
    
    start.destroy()
    gm.game_screen(tabuleiro, solucao)

start = ctk.CTk()
start.title("Sudoku")
start.geometry("300x375")
start.resizable(False, False)
lbl_title = ctk.CTkLabel(
    master=start, 
    text="Sudoku", 
    font=("Arial", 48, "bold")
)
lbl_title.place(
    relx=0.5, 
    rely=0.2, 
    anchor=ctk.CENTER
)
lbl_diff = ctk.CTkLabel(
    master=start, 
    text="Selecione a dificuldade: ", 
    font=("Arial", 16)
)
lbl_diff.place(
    relx=0.5, 
    rely=0.4, 
    anchor=ctk.CENTER
)
optionmenu = ctk.CTkOptionMenu(
    master=start, 
    values=["Fácil", "Normal", "Difícil", "Impossível"], 
    command=seletor_dificuldade
)
optionmenu.place(
    relx=0.5, 
    rely=0.5, 
    anchor=ctk.CENTER)
optionmenu.set("Normal")
btn_start_game = ctk.CTkButton(
    master=start, 
    text="Iniciar Jogo", 
    command=iniciar_jogo
).place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

start.mainloop()