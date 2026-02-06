# J.A.R.V.I.S. — v1.0 Beta
README PT-BR / EN
PT-BR:
=========================================
Assistente inteligente local inspirado no J.A.R.V.I.S. do Tony Stark do MCU, desenvolvido em Python, com interface gráfica, voz opcional, microfone, memória persistente e integração com Ollama (Cloud Free/Paga ou Local). 

Aviso Legal / Disclaimer ⚠️
PT-BR: Este projeto é um tributo de fã, desenvolvido apenas para fins educacionais e de estudo de IA. O nome J.A.R.V.I.S., bem como os conceitos visuais e nomes associados ao Universo Cinematográfico Marvel (MCU), são marcas registradas e propriedade intelectual da Marvel Entertainment, LLC e The Walt Disney Company. Este software não possui fins lucrativos e não tem afiliação oficial com as empresas mencionadas.
EN: This project is a fan tribute, developed solely for educational and AI research purposes. The name J.A.R.V.I.S., as well as visual concepts and names associated with the Marvel Cinematic Universe (MCU), are registered trademarks and intellectual property of Marvel Entertainment, LLC and The Walt Disney Company. This software is non-profit and has no official affiliation with the aforementioned companies.


Projeto em BETA, funcional e estável para uso diário.

🧩 Funcionalidades

Interface gráfica em PyQt

Reconhecimento de voz 

Voz masculina 

Memória persistente (memory_store.json)

Pesquisa web

Modo silencioso (sem voz)

Launcher interativo (.bat)

Organização modular (core / ui / modules / voice)

💻 Requisitos

Windows 10 ou 11

Python 3.10+

Ollama instalado


🔧 Instalação 
1. Instalar o Ollama

Baixe e instale:

https://ollama.com


Após instalar:

Abra o Ollama

Ele deve ficar rodando na bandeja do Windows

❗ NÃO feche o Ollama, senão o JARVIS não funciona

Se o Ollama não estiver aberto, o JARVIS não consegue se conectar à IA.

2. Clonar este repositório

3.  Instalar dependências:
pip install -r requirements.txt

ecutar (FORMA CORRETA)
✅ Método recomendado

Execute o arquivo:

JARVIS_LAUNCHER.bat


Ele abrirá um menu interativo.

🎛️ Modos disponíveis

[1] Protocolo Integral (Com Voz)

Microfone Ativo (Opcional, vem o botão desativado por padrão)

Respostas Faladas

Chat

Funções de Pesquisa Web e Abrir Apps

[2] Modo Furtivo (Silencioso)

Sem voz a ia

Apenas texto + interface + mic opcional + Funções 


[3] Encerrar sistema

📂 Estrutura do Projeto (Resumo)
assets/        → Sons e imagens
core/          → IA, memória e prompt principal
modules/       → Microfone, som, web
ui/            → Interface gráfica
voice/         → Voz TTS e modelos
main.py        → Arquivo principal
JARVIS_LAUNCHER.bat → Launcher recomendado

EN:

Local intelligent assistant inspired by J.A.R.V.I.S., developed in Python, with graphical interface, optional voice, microphone, persistent memory, and integration with Ollama (Cloud Free/Paid or Local).

Project in BETA, functional and stable for daily use.

🧩 Features

Graphical interface in PyQt

Voice recognition

Male voice

Persistent memory (memory_store.json)

Web search

Silent mode (no voice)

Interactive launcher (.bat)

Modular organization (core / ui / modules / voice)

💻 Requirements

Windows 10 or 11

Python 3.10+

Ollama installed

🔧 Installation

1. Install Ollama

Download and install:

https://ollama.com

After installing:

Open Ollama

It should run in the Windows system tray

❗ DO NOT close Ollama, otherwise JARVIS will not work

If Ollama is not open, JARVIS cannot connect to the AI.

2. Clone this repository

3. Install dependencies: `pip install -r requirements.txt`

Execute (CORRECT WAY)

✅ Recommended method

Run the file:

`JARVIS_LAUNCHER.bat`

It will open an interactive menu.

🎛️ Available Modes

[1] Full Protocol (With Voice)

Microphone Active (Optional, button is disabled by default)

Spoken Responses

Chat

Web Search and App Opening Functions

[2] Stealth Mode (Silent)

No AI voice

Text only + interface + optional mic + functions

[3] System Shutdown

📂 Project Structure (Summary)
assets/ → Sounds and images
core/ → AI, memory and main prompt
modules/ → Microphone, sound, web
ui/ → Graphical interface
voice/ → TTS voice and models
main.py → Main file
JARVIS_LAUNCHER.bat → Recommended launcher
