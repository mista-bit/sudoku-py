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
    
    app.start.destroy()
    gm.game_screen(tabuleiro, solucao)


class StartScreen():
    def __init__(self):
        self.start = ctk.CTk()
        self.start.title("Sudoku")
        self.start.geometry("300x375")
        self.start.resizable(False, False)
        self.start.grid_rowconfigure((0,1,2,3), weight=1)  # faz cada linha expandir
        self.start.grid_columnconfigure(0, weight=1)

        self.construir_elementos()

    def construir_elementos(self):
        self.forjar_titulo()
        self.forjar_seletor_dificuldade()
        self.forjar_btn_start()

    def forjar_titulo(self):
        lbl_title = ctk.CTkLabel(
            master=self.start, 
            text="Sudoku", 
            font=("Arial", 48, "bold")
        )
        lbl_title.grid(
            row=0, 
            column=0,
            sticky="n",
            pady=(20, 0)
        )

    def forjar_seletor_dificuldade(self):
        frame_diff = ctk.CTkFrame(self.start, fg_color="transparent")
        frame_diff.grid(row=1, column=0, sticky="n", pady=(20, 0))
        frame_diff.grid_columnconfigure(0, weight=1)

        lbl_diff = ctk.CTkLabel(
            master=frame_diff, 
            text="Selecione a dificuldade:", 
            font=("Arial", 16)
        )
        lbl_diff.grid(row=0, column=0, pady=(0, 10), sticky="n")

        optionmenu = ctk.CTkOptionMenu(
            master=frame_diff, 
            values=["Fácil", "Normal", "Difícil", "Impossível"], 
            command=seletor_dificuldade
        )
        optionmenu.grid(row=1, column=0, sticky="n")
        optionmenu.set("Normal")

    def forjar_btn_start(self):
        btn_start_game = ctk.CTkButton(
            master=self.start, 
            text="Iniciar Jogo", 
            command=iniciar_jogo
        )
        btn_start_game.grid(
            row=3, 
            column=0,
            pady=(30, 10),
            sticky="n"
        )


if __name__ == "__main__":
    app = StartScreen()
    app.start.mainloop()
