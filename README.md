# 🎮 Sudoku Game

Um jogo de Sudoku moderno e elegante desenvolvido em Python com interface gráfica usando CustomTkinter.

## 📥 Download

**[⬇️ Baixar última versão (Windows)](https://github.com/mista-bit/sudoku-py/releases/latest)**

Não precisa instalar Python - basta baixar, extrair e jogar!

## ✨ Características

- 🎨 **Interface Moderna**: Design clean e intuitivo com CustomTkinter
- 🎯 **Modo Escrever**: Insira números diretamente nas células
- 📝 **Modo Anotar**: Faça anotações para resolver o puzzle
- ❤️ **Sistema de Vidas**: 3 chances para acertar
- 💡 **Mostrar Solução**: Revele a solução completa a qualquer momento
- 🎲 **Geração Aleatória**: Novos tabuleiros gerados automaticamente
- 🔒 **Células Bloqueadas**: Números iniciais não podem ser alterados

## 🚀 Como Usar

### 💾 Download (Recomendado)

**Não precisa instalar Python!** Baixe o executável pronto:

1. Acesse a [página de Releases](https://github.com/mista-bit/sudoku-py/releases)
2. Baixe o arquivo `Sudoku-Windows.zip`
3. Extraia o arquivo ZIP
4. Execute `Sudoku.exe` (Windows)

### 🐍 Executar o Código Fonte

Se você quer rodar o código Python diretamente:

#### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

#### Passos

1. Clone o repositório:
```bash
git clone https://github.com/mista-bit/sudoku-py.git
cd sudoku-game
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o jogo:
```bash
python sudoku/main.py
```

## 📦 Dependências

```
customtkinter>=5.0.0
```

## 🎮 Como Jogar

1. **Selecione uma célula**: Clique em qualquer célula vazia
2. **Escolha o modo**:
   - **Escrever**: Para inserir a resposta definitiva
   - **Anotar**: Para fazer anotações temporárias
3. **Digite um número**: Use os botões numéricos (1-9)
4. **Sistema de vidas**: Você tem 3 tentativas. Errar 3 vezes encerra o jogo
5. **Vença**: Complete todo o tabuleiro corretamente!

### Botões Disponíveis

- **Mostrar Solução**: Revela a solução completa do puzzle
- **Novo Jogo**: Inicia um novo jogo com tabuleiro diferente
- **Fechar Jogo**: Encerra a aplicação

## 📁 Estrutura do Projeto

```
sudoku-game/
├── main.py              # Arquivo principal
├── game_screen.py       # Classe da interface do jogo
├── gen_sudoku.py        # Gerador de tabuleiros Sudoku
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem de programação
- **CustomTkinter**: Framework moderno para interfaces gráficas
- **Tkinter**: Biblioteca base para GUI

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ por Pedro Araújo

## 🙏 Agradecimentos

- CustomTkinter pela excelente biblioteca de interface gráfica
- Comunidade Python pelo suporte

---

⭐ Se você gostou deste projeto, considere dar uma estrela no repositório!
