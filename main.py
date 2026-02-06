import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

def load_theme(app):
    """Carrega o visual Neon do Jarvis"""
    try:
        with open("ui/theme.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except Exception as e:
        print(f"[AVISO] Não foi possível carregar o tema: {e}")

if __name__ == "__main__":
    # Inicializa a aplicação base do Qt
    app = QApplication(sys.argv)
    
    # Aplica o estilo visual (CSS/QSS)
    load_theme(app)

    # LÓGICA DO MODO VOZ:
    # Verifica se o usuário digitou "--voice" ao abrir o programa
    use_voice = "--voice" in sys.argv
    
    if use_voice:
        print("\n" + "!"*40)
        print("[SISTEMA] JARVIS VOICE VERSION ATIVADA")
        print("!"*40 + "\n")
    else:
        print("\n" + "="*40)
        print("[SISTEMA] JARVIS MODO SILENCIOSO")
        print("="*40 + "\n")

    # Inicia a janela principal passando a configuração de voz
    window = MainWindow(use_voice=use_voice)
    window.show()

    # Mantém o programa rodando
    sys.exit(app.exec())
