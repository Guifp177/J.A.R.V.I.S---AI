import threading
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QFrame, QPushButton, QVBoxLayout
)
from PySide6.QtCore import Qt, QPoint, QTimer, Signal, Slot
from PySide6.QtGui import QFont, QMovie
from datetime import datetime
import pytz

# Importações dos seus componentes
from ui.components.widgets.arc_meter import ArcMeter
from ui.components.widgets.radar import Radar
from ui.components.panels.panels import SidePanel
from ui.components.panels.info_panel import InfoPanel
from ui.components.widgets.chat_panel import ChatPanel

from modules.sound import SoundFX
from modules.mic_input import MicInput
from core.ollama_client import OllamaClient
from voice.jarvis_voice import JarvisTTS

# ───────── MAIN WINDOW ─────────
class MainWindow(QMainWindow):
    # SINAIS para ponte segura entre Threads e Interface
    voice_command_signal = Signal(str)
    jarvis_reply_signal = Signal(str) # Sinal para postar a resposta do Jarvis com segurança

    def __init__(self, use_voice=False):
        super().__init__()

        # Configuração de Modo
        self.use_voice = use_voice
        self.tts = JarvisTTS() if self.use_voice else None

        # Inicialização do Core
        self.ollama = OllamaClient()
        self.mic = MicInput() 
        self.sfx = SoundFX()

        # Configuração da Janela
        self.setWindowTitle("J.A.R.V.I.S")
        self.setFixedSize(1100, 700)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self._drag_pos = QPoint()

        # Interface Base
        central = QWidget(self)
        self.setCentralWidget(central)
        self.background = QFrame(central)
        self.background.setGeometry(self.rect())
        self.background.setStyleSheet("background-color: #050b10;")

        # Conectar Sinais
        self.voice_command_signal.connect(self.handle_user_message)
        self.jarvis_reply_signal.connect(self._post_jarvis_message)

        # 🎤 Botão Mic
        self.btn_mic = QPushButton("🎤", self.background) 
        self.btn_mic.setFixedSize(34, 24) 
        self.btn_mic.move(self.width() - 136, 12) 
        self.btn_mic.clicked.connect(self.listen_mic)

        # Cabeçalho
        self.title = QLabel("J.A.R.V.I.S", self.background)
        self.title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        self.title.move(20, 12)

        self.subtitle = QLabel("...SYSTEM ONLINE", self.background)
        self.subtitle.setFont(QFont("Segoe UI", 9))
        self.subtitle.move(25, 55)

        # Botões de Controle
        self.btn_close = QPushButton("✕", self.background)
        self.btn_close.setFixedSize(34, 24)
        self.btn_close.move(self.width() - 44, 12)
        self.btn_close.clicked.connect(self.close)

        self.btn_mute = QPushButton("🔇", self.background)
        self.btn_mute.setFixedSize(34, 24)
        self.btn_mute.move(self.width() - 90, 12)

        # HUD Widgets
        self.left_panel = SidePanel(parent=self.background, show_inner_lines=False)
        self.left_panel.move(20, 100)

        self.right_panel = SidePanel(parent=self.background)
        self.right_panel.move(self.width() - 300, 100)

        self.radar = Radar(parent=self.background)
        self.radar.move(50, 130)

        self.info_panel = InfoPanel(parent=self.background)
        self.info_panel.move(50, 390)

        self.core = ArcMeter(size=260, parent=self.background)
        self.core.move(self.width() // 2 - 130, self.height() // 2 - 195)

        # GIF Animado
        self.right_image_placeholder = QLabel(self.background)
        self.right_image_placeholder.setGeometry(self.width() - 290, 495, 260, 160)
        self.movie = QMovie("assets/jarvis.gif")
        self.movie.setScaledSize(self.right_image_placeholder.size())
        self.right_image_placeholder.setMovie(self.movie)
        self.movie.start()

        # Chat Panel
        arc_bottom = self.core.y() + self.core.height()
        self.chat_panel = ChatPanel(parent=self.background, width=420, max_height=250)
        self.chat_panel.move(self.width() // 2 - 210, arc_bottom + 10)
        
        # Conecta o texto digitado (Enter) à IA
        self.chat_panel.message_sent.connect(self.handle_user_message)

        # Início
        self.sfx.play_start()

    # ───────── LÓGICA DE MICROFONE ─────────
    def listen_mic(self):
        self.chat_panel.append_message("Jarvis", "Ouvindo, Senhor...")
        threading.Thread(target=self._mic_worker, daemon=True).start()

    def _mic_worker(self):
        print("[MIC] Capturando...")
        text = self.mic.listen() 
        
        if text and text.strip():
            print(f"[MIC] Reconhecido: {text}")
            self.voice_command_signal.emit(text)
        else:
            QTimer.singleShot(0, lambda: self.chat_panel.append_message("Jarvis", "Não detectei comandos."))

    # ───────── PROCESSAMENTO DE MENSAGENS ─────────
    @Slot(str)
    def handle_user_message(self, text):
        if not text.strip():
            return

        self.sfx.play_search()
        self.chat_panel.append_message("You", text)
        self.chat_panel.chat_input.clear()
        self.chat_panel.append_message("Jarvis", "Processando dados...")
        
        QTimer.singleShot(100, lambda: self._ask_ai(text))

    def _ask_ai(self, text):
        """Envia para o Ollama e coordena a exibição/fala"""
        try:
            reply = self.ollama.chat(text)
        except Exception as e:
            reply = f"Erro de rede: {e}"

        # Se houver voz, geramos primeiro e mostramos depois
        if self.use_voice and self.tts:
            print("[SISTEMA] Sincronizando áudio...")
            # O callback vai emitir o sinal para postar o texto na UI
            def on_ready():
                self.jarvis_reply_signal.emit(reply)

            threading.Thread(
                target=self.tts.generate_and_speak, 
                args=(reply, on_ready), 
                daemon=True
            ).start()
        else:
            # Modo silencioso posta direto
            self.jarvis_reply_signal.emit(reply)

    @Slot(str)
    def _post_jarvis_message(self, text):
        """Posta a mensagem do Jarvis no Chat Panel de forma segura"""
        self.chat_panel.append_message("Jarvis", text)

    # ───────── EVENTOS DE INTERFACE ─────────
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = event.globalPosition().toPoint() - self._drag_pos
            self.move(self.pos() + delta)
            self._drag_pos = event.globalPosition().toPoint()
