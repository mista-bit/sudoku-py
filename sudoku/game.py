import gen_sudoku as gsdk
import customtkinter as ctk

N = 9

def game_screen(tabuleiro, solucao):
    game = ctk.CTk()
    game.title("Sudoku - Jogo")
    game.geometry("600x350")
    game.resizable(False, False)
    lbl_title = ctk.CTkLabel(master=game, text="Sudoku", font=("Arial",24, "bold")).place(relx=0.2, rely=0.1, anchor=ctk.CENTER)
    btn_showsol = ctk.CTkButton(master=game, text="Mostrar Solução").place(relx=0.2, rely=0.9, anchor=ctk.CENTER)
    btn_restart = ctk.CTkButton(master=game, text="Reiniciar Jogo").place(relx=0.5, rely=0.9, anchor=ctk.CENTER)
    btn_quit = ctk.CTkButton(master=game, text="Sair do Jogo", command=game.destroy).place(relx=0.8, rely=0.9, anchor=ctk.CENTER)
    # Additional game screen setup goes here

    game.mainloop()

