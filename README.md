🔐 Sistema de Reconhecimento Facial com Arduino e LCD
📌 Objetivo

Este projeto implementa um sistema de controle de acesso que utiliza:

Python + OpenCV + face_recognition para reconhecer rostos a partir de vídeo ou webcam.

Arduino UNO para acender LEDs indicando o resultado.

Display LCD 16x2 (I2C) para exibir mensagens de “Acesso Liberado” ou “Acesso Negado”.

Fluxo:

O Python detecta o primeiro rosto → autorizado.

Se o mesmo rosto aparecer → LED verde + mensagem “Acesso Liberado”.

Se outro rosto aparecer → LED vermelho + mensagem “Acesso Negado”.

⚙️ Dependências
Python (3.10)

- cmake
- Visual Studio Build Tools
- dlib (dependência do face_recognition).

Arduino

- IDE Arduino 
Biblioteca do LCD: LiquidCrystal_I2C (arduino)

🔌 Conexões do Arduino

LED verde 

LED vermelho 

LCD I2C
