import subprocess
import os
from pathlib import Path
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QObject

class JarvisTTS(QObject): # Adicionado QObject para suporte a sinais se precisar
    def __init__(self):
        super().__init__()
        self.base_path = Path(__file__).parent.parent
        self.piper_exe = self.base_path / "voice" / "bin" / "piper" / "piper.exe"
        self.model = next((self.base_path / "voice" / "models").glob("*.onnx"), None)
        self.output_wav = self.base_path / "voice" / "output.wav"
        
        # Player nativo otimizado
        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(1.0)

    def generate_and_speak(self, text, callback):
        """
        Gera o áudio primeiro. 
        Quando terminar, toca o som e executa o 'callback' para mostrar o texto.
        """
        if not self.piper_exe.exists() or not self.model:
            callback() # Se falhar, pelo menos mostra o texto
            return

        clean_text = text.replace('"', '').replace('\n', ' ').strip()

        # Comando otimizado para PC fraco
        command = [
            str(self.piper_exe),
            "--model", str(self.model),
            "--output_file", str(self.output_wav),
            "--threads", "1" 
        ]

        try:
            # 1. Gera o arquivo em silêncio
            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            
            # Envia o texto e aguarda o Piper terminar (essencial para o efeito)
            process.communicate(input=clean_text.encode('utf-8'))

            # 2. Quando o áudio estiver pronto, disparar o som e o texto juntos
            if self.output_wav.exists():
                url = QUrl.fromLocalFile(str(self.output_wav.absolute()))
                self.player.setSource(url)
                
                # Executa o callback (que vai mostrar o texto na MainWindow)
                callback() 
                
                # Toca o áudio
                self.player.play()
                print("[JARVIS-VOICE] Áudio e texto sincronizados.")
            else:
                callback()
            
        except Exception as e:
            print(f"[TTS SYNC ERROR] {e}")
            callback()

    def stop(self):
        self.player.stop()
