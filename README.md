# 📝 Relatório do Candidato

**👤 Identificação:** Miguel Wagner Galvão Ferreira de Morais

---

## Classificação de Dígitos MNIST para Edge AI 🚀

Este projeto consiste no desenvolvimento, treinamento e otimização de uma Rede Neural Convolucional (CNN) para a classificação de dígitos manuscritos (dataset MNIST), com foco em dispositivos de baixo recurso computacional (Edge Computing).

---

### 1️⃣ Resumo da Arquitetura do Modelo

O modelo foi projetado com uma arquitetura **CNN (Convolutional Neural Network)** enxuta para equilibrar alta precisão e baixo consumo de memória:

* **Camada de Entrada:** Imagens de 28x28 pixels em tons de cinza (1 canal).
* **Primeiro Bloco Convolucional:** Camada `Conv2D` (16 filtros, 3x3) + `MaxPooling2D` (2x2).
* **Segundo Bloco Convolucional:** Camada `Conv2D` (32 filtros, 3x3) + `MaxPooling2D` (2x2).
* **Camada de Achatamento (Flatten):** Converte o mapa de características 2D em um vetor 1D.
* **Camada Densa:** 32 neurônios com ativação **ReLU**.
* **Camada de Saída:** 10 neurônios (classes de 0 a 9) com ativação **Softmax**.

---

### 2️⃣ Bibliotecas Utilizadas

* **TensorFlow 2.12+**: Framework principal para construção e treinamento.
* **Keras**: API de alto nível utilizada para definir as camadas da rede.
* **NumPy**: Processamento numérico e manipulação de arrays.
* **TensorFlow Lite**: Conversão e otimização para implantação em dispositivos Edge.

---

### 3️⃣ Técnica de Otimização do Modelo

Para reduzir o peso do modelo para sistemas IoT, foi aplicada a técnica de **Dynamic Range Quantization** via TFLite Converter.

* **O Processo:** Os pesos do modelo foram convertidos de ponto flutuante (32 bits) para inteiros (8 bits).
* **Vantagem:** Redução drástica no armazenamento e aceleração da inferência, ideal para microcontroladores ou sistemas embarcados que operam apenas com CPU.

---

### 4️⃣ Resultados Obtidos

Os resultados superaram as expectativas de engenharia, mantendo alta precisão em um arquivo extremamente leve.

| Métrica | Resultado |
| :--- | :--- |
| **Acurácia Final (Teste)** | **98,55%** |
| **Épocas de Treinamento** | 3 |
| **Tamanho Original (.h5)** | **400,12 KB** |
| **Tamanho Otimizado (.tflite)** | **36,79 KB** |
| **Fator de Redução** | **~10,8x mais leve** |

---

### 5️⃣ Comentários Adicionais

**Principais Aprendizados:**
* A importância de equilibrar a profundidade da rede com o limite de hardware: reduzir filtros e neurônios permitiu bater a meta de 600KB mantendo uma performance excelente.
* O fluxo de conversão para TFLite é essencial para transformar modelos de pesquisa em produtos reais para Edge AI.

**Possíveis Melhorias:**
* **Acurácia:** Aplicação de *Data Augmentation* para aumentar a robustez contra variações na caligrafia.
* **Eficiência:** Uso de *Pruning* (poda de neurônios) para remover conexões redundantes e reduzir ainda mais o tamanho.
* **Hardware:** Implementação de *Full Integer Quantization* para rodar em dispositivos que não possuem unidade de processamento de ponto flutuante (FPU).
  
*Relatório final desenvolvido para o desafio técnico de Visão Computacional e Edge AI para o processo seletivo do PNAAT.*
