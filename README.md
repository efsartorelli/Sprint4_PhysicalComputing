# 🔐 Sistema de Reconhecimento Facial com Arduino e LCD  

## 📌 Objetivo
Este projeto implementa um **sistema de controle de acesso** que combina **Visão Computacional** com **Arduino**.  

- 🎥 **Python + OpenCV + face_recognition** → reconhecimento de rostos a partir de vídeo ou webcam.  
- 💡 **Arduino UNO** → acende LEDs indicando o resultado.  
- 🖥️ **Display LCD 16x2 (I2C)** → exibe mensagens de “Acesso Liberado” ou “Acesso Negado”.  

### 🔄 Fluxo
1. O Python detecta o **primeiro rosto** → autorizado.  
2. Se o mesmo rosto aparecer → ✅ **LED verde + “Acesso Liberado”**.  
3. Se outro rosto aparecer → ❌ **LED vermelho + “Acesso Negado”**.  

---

## ⚙️ Dependências

### 🐍 Python (3.10)
- [cmake]
- [Visual Studio Build Tools] 
- Bibliotecas: IDE Arduino Biblioteca do LCD: LiquidCrystal_I2C (arduino)


### 🔌 Conexões do Arduino LED verde LED vermelho LCD I2C

- LED verde
- LED vermelho
- LCD I2C
