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

### 🐍 Python (versão 3.10 recomendada)
- [cmake](https://cmake.org/download/)  
- [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)  
- Bibliotecas:
  ```bash
  pip install opencv-python face-recognition pyserial
