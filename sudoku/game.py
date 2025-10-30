import customtkinter as ctk
import gen_sudoku as gsdk
import main

N = 9
printedkey = None
vidas = 3

class game_screen():
    def __init__(self, tabuleiro, solucao):
        self.tabuleiro = tabuleiro
        self.solucao = solucao
        self.printedkey = None
        self.entries = {}  
        self.selected_cell = None
        self.wrinote_mode = "Escrever"

        self.game = ctk.CTk()
        self.game.title("Sudoku - Jogo")
        self.game.geometry("760x500")
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

    def on_entry_click(self, i, j):
        """Callback quando uma entry é clicada"""
        self.selected_cell = (i, j)
        print(f"Célula selecionada: [{i}][{j}]")

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
                entry.bind(
                    "<FocusIn>", 
                    lambda event, 
                    row=i, 
                    col=j: 
                    self.on_entry_click(
                        row, 
                        col
                    )
                )
                self.entries[(i, j)] = entry
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
        self.wrinote_seg = ctk.CTkSegmentedButton(
            master=self.keynbtnsframe,
            values=["Escrever", "Anotar"],
            width=200,
            height=40,
            font=("Arial", 14),
            command=lambda value: seg_callback(value)
        )
        self.wrinote_seg.set("Escrever")
        self.wrinote_seg.grid(
            row=0, 
            column=0,
            pady=(20),
            padx=(40, 20),
            sticky="we" 
        )
        
        def seg_callback(value):
            self.wrinote_mode = value
            print(f"Modo alterado para: {self.wrinote_mode}")

        self.teclado_frame = ctk.CTkFrame(master=self.keynbtnsframe, fg_color="transparent")
        self.teclado_frame.grid(
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
                master=self.teclado_frame, 
                text=str(i), 
                width=60, 
                height=60, 
                font=("Arial", 16),
                command=lambda x=i: self.btn_press(x)
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
        self.liveslbl = ctk.CTkLabel(
            master=btnframe,
            text=f"Vidas: {vidas}",
            font=("Arial", 16)
        )
        self.liveslbl.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=5,
            pady=1
        )
        showsol = ctk.CTkButton(
            master=btnframe,
            text="Mostrar Solução",
            font=("Arial", 16),
            command=self.show_solution
        )
        showsol.grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )
        newgme = ctk.CTkButton(
            master=btnframe,
            text="Novo Jogo",
            font=("Arial", 16),
            command=self.new_game_callback
        )
        newgme.grid(
            row=1,
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
            row=2,
            column=0,
            columnspan=2,
            padx=5,
            pady=5
        )


    def new_game_callback(self):
        self.game.destroy()
        main.app = main.StartScreen()
        main.app.start.mainloop()

    def btn_press(self, value):
        global vidas
        self.printedkey = value
        print(f"Tecla pressionada: {self.printedkey}")
        
        if self.selected_cell:
            i, j = self.selected_cell
            entry = self.entries[(i, j)]
            
            if entry.cget("state") != "disabled":
                entry.delete(0, "end")
                entry.insert(0, str(value))
                if self.wrinote_mode == "Escrever":
                    if value == self.solucao[i][j]:
                        self.tabuleiro[i][j] = value
                        entry.configure(state="disabled")
                    else: 
                        vidas -= 1
                        self.liveslbl.configure(text=f"Vidas: {vidas}")
                        print(f"Valor incorreto! Vidas restantes: {vidas}")
                        entry.delete(0, "end")
                        if vidas == 0:
                            print("Game Over!")
                            self.teclado_frame.destroy()
                            self.wrinote_seg.destroy()
                            lbl_game_over = ctk.CTkLabel(
                                master=self.keynbtnsframe, 
                                text="Game over!\nSelecione uma das opções abaixo:", 
                                font=("Arial", 20)
                            )
                            self.liveslbl.configure(text=f"Vidas: {vidas}")
                            lbl_game_over.grid(row=1, column=0, pady=(20, 0))
                else:
                    print(f"Modo Anotar: Valor {value} anotado em [{i}][{j}]")
            else:
                print(f"A célula [{i}][{j}] está bloqueada e não pode ser modificada.")
        else:
            print("Nenhuma célula selecionada")
    
    def show_solution(self):
        for i in range(N):
            for j in range(N):
                entry = self.entries[(i, j)]
                entry.delete(0, "end")
                entry.insert(0, str(self.solucao[i][j]))
                entry.configure(state="disabled")
        
"""
if __name__ == "__main__":
    app = game_screen([[0]*9 for _ in range(9)], [[0]*9 for _ in range(9)])
    app = game_screen([[0]*9 for _ in range(9)], [[0]*9 for _ in range(9)])
    app.game.mainloop()"""