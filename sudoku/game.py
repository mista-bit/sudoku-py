import customtkinter as ctk

N = 9
printedkey = None

class game_screen():
    def __init__(self, tabuleiro, solucao):
        self.tabuleiro = tabuleiro
        self.solucao = solucao
        self.printedkey = None

        self.game = ctk.CTk()
        self.game.title("Sudoku - Jogo")
        self.game.geometry("760x475")
        self.game.resizable(False, False)
        self.game.grid_rowconfigure(0, weight=1)
        self.game.grid_columnconfigure(0, weight=1)

        self.construir_elementos()

    def construir_elementos(self):
        self.mainframe = ctk.CTkFrame(master=self.game, fg_color="transparent")
        self.mainframe.grid(
            row=0, 
            column=0, 
            sticky="nsew", 
            padx=10, 
            pady=10
        )
        self.mainframe.grid_columnconfigure(0, weight=0)
        self.mainframe.grid_columnconfigure(1, weight=1)
        
        self.forjar_titulo()
        self.forjar_tabuleiro(tabuleiro = self.tabuleiro, solucao = self.solucao)

        self.keynbtnsframe = ctk.CTkFrame(
            master=self.mainframe, 
            fg_color="transparent"
        )
        self.keynbtnsframe.grid(
            row=1, 
            column=1, 
            sticky=""
        )
        self.keynbtnsframe.grid_columnconfigure(0, weight=1)

        self.forjar_teclado()
        self.forjar_btns()

    def forjar_titulo(self):
        lbl_title = ctk.CTkLabel(
            master=self.mainframe, 
            text="Sudoku", 
            font=("Arial", 36, "bold")
        )
        lbl_title.grid(
            row=0, 
            column=0, 
            pady=(0, 20),
            columnspan=2
        )

    def forjar_tabuleiro(self, tabuleiro, solucao):
        tab_frame = ctk.CTkFrame(master=self.mainframe, fg_color="transparent")
        tab_frame.grid(
            row=1, 
            column=0, 
            sticky="nsew"
        )
        for i in range(N):
            for j in range(N):
                cell_value = tabuleiro[i][j]

                padx_left = 1
                padx_right = 1
                pady_top = 1
                pady_bottom = 1
            
                # Adiciona espaço extra à direita nas colunas 2 e 5 (após cada bloco 3x3)
                if j == 2 or j == 5:
                    padx_right = 3
            
                # Adiciona espaço extra à esquerda na coluna 3 e 6 (início de novo bloco)
                if j == 3 or j == 6:
                    padx_left = 3
            
                # Adiciona espaço extra abaixo nas linhas 2 e 5
                if i == 2 or i == 5:
                    pady_bottom = 3
            
                # Adiciona espaço extra acima nas linhas 3 e 6
                if i == 3 or i == 6:
                    pady_top = 3

                entry = ctk.CTkEntry(
                    master=tab_frame, 
                    width=40, 
                    height=40, 
                    font=("Arial", 20), 
                    justify="center"
                )
                if cell_value != 0:
                    entry.insert(0, str(cell_value))
                    entry.configure(state="disabled")
                entry.grid(
                    row=i, 
                    column=j, 
                    padx=(padx_left, padx_right), 
                    pady=(pady_top, pady_bottom)
                )

    def forjar_teclado(self):
        wrinote_seg = ctk.CTkSegmentedButton(
            master=self.keynbtnsframe,
            values=["Escrever", "Anotar"],
            width=200,
            height=40,
            font=("Arial", 14)
        )
        wrinote_seg.set("Escrever")
        wrinote_seg.grid(
            row=0, 
            column=0,
            pady=(20),
            padx=(40, 20),
            sticky="we"
            
        )

        teclado_frame = ctk.CTkFrame(master=self.keynbtnsframe, fg_color="transparent")
        teclado_frame.grid(
            row=1, 
            column=0, 
            padx=(20, 0),
            sticky=""
        )

        for i in range(1, 10):
            if i < 4:
                row = 0
                column = i - 1
            elif i < 7:
                row = 1
                column = i - 4
            else:
                row = 2
                column = i - 7
            btn = ctk.CTkButton(
                master=teclado_frame, 
                text=str(i), 
                width=60, 
                height=60, 
                font=("Arial", 16),
                command=lambda x=i: self.set_key(x)
            )
            btn.grid(row=row, column=column, padx=5, pady=5)

    def forjar_btns(self):
        btnframe = ctk.CTkFrame(master=self.keynbtnsframe, fg_color="transparent")
        btnframe.grid(
            row=2, 
            column=0, 
            pady=(20, 0),
            padx=(40, 20),
            sticky=""
        )
        showsol = ctk.CTkButton(
            master=btnframe,
            text="Mostrar Solução",
            font=("Arial", 16)
        )
        showsol.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )
        newgme = ctk.CTkButton(
            master=btnframe,
            text="Novo Jogo",
            font=("Arial", 16)
        )
        newgme.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )
        closegame = ctk.CTkButton(
            master=btnframe,
            text="Fechar Jogo",
            font=("Arial", 16),
            command=self.game.destroy
        )
        closegame.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=5,
            pady=5
        )

    def set_key(self, value):
        self.printedkey = value
        print(f"Tecla pressionada: {self.printedkey}")
"""
if __name__ == "__main__":
    app = game_screen([[0]*9 for _ in range(9)], [[0]*9 for _ in range(9)])
    app = game_screen([[0]*9 for _ in range(9)], [[0]*9 for _ in range(9)])
    app.game.mainloop()"""