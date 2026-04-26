# Processo Seletivo – Intensivo Maker | AI
👤 **Aluno:** Miguel Wagner Galvão Ferreira de Morais

# Classificação de Dígitos MNIST para Edge AI 🚀

Este projeto consiste no desenvolvimento, treinamento e otimização de uma Rede Neural Convolucional (CNN) para a classificação de dígitos manuscritos (dataset MNIST), com foco em dispositivos de baixo recurso computacional (Edge Computing).

---

## 📋 Resumo da Arquitetura

O modelo foi projetado com uma arquitetura **CNN (Convolutional Neural Network)** enxuta para equilibrar alta precisão e baixo consumo de memória:

* **Camada de Entrada:** Imagens de 28x28 pixels em tons de cinza (1 canal).
* **Primeiro Bloco Convolucional:** Camada `Conv2D` (16 filtros, 3x3) + `MaxPooling2D` (2x2).
* **Segundo Bloco Convolucional:** Camada `Conv2D` (32 filtros, 3x3) + `MaxPooling2D` (2x2).
* **Camada de Achatamento (Flatten):** Converte o mapa de características 2D em um vetor 1D.
* **Camada Densa:** 32 neurônios com ativação **ReLU**.
* **Camada de Saída:** 10 neurônios (classes de 0 a 9) com ativação **Softmax**.

---

## 📚 Bibliotecas Utilizadas

* **TensorFlow 2.12+**: Framework principal para construção e treinamento.
* **Keras**: API de alto nível utilizada para definir as camadas da rede.
* **NumPy**: Processamento numérico e manipulação de arrays.
* **TensorFlow Lite**: Conversão e otimização para implantação em dispositivos Edge.

---

## ⚡ Técnica de Otimização

Para reduzir o peso do modelo para sistemas IoT, foi aplicada a técnica de **Dynamic Range Quantization** via TFLite Converter.

* **O Processo:** Os pesos do modelo foram convertidos de ponto flutuante (32 bits) para inteiros (8 bits).
* **Vantagem:** Redução drástica no armazenamento e aceleração da inferência, ideal para microcontroladores ou sistemas embarcados que operam apenas com CPU.

---

## 📊 Resultados Obtidos

Os resultados superaram as expectativas de engenharia, mantendo alta precisão em um arquivo extremamente leve.

| Métrica | Resultado |
| :--- | :--- |
| **Acurácia Final (Teste)** | **98,55%** |
| **Épocas de Treinamento** | 3 |
| **Tamanho Original (.h5)** | **400,12 KB** |
| **Tamanho Otimizado (.tflite)** | **36,79 KB** |
| **Fator de Redução** | **~10,8x mais leve** |

---

## 🧠 Principais Aprendizados

1.  **Design Eficiente:** A redução de filtros (de 64 para 32/16) e neurônios na camada densa permitiu que o modelo ficasse abaixo do limite de 600KB exigido, sem comprometer a acurácia.
2.  **Otimização de Bordas:** Aprendi que, para tarefas como o MNIST, a quantização de pesos é extremamente eficaz, pois o modelo não perde a capacidade de identificar formas fundamentais mesmo com menos precisão numérica.
3.  **Ambientes CI/CD:** O desenvolvimento focado em scripts que executam sem intervenção manual é crucial para pipelines de integração contínua.

---

## 🚀 Possíveis Melhorias

* **Acurácia:** Implementação de *Data Augmentation* (rotação e deslocamento) para aumentar a robustez contra dígitos escritos de forma inclinada.
* **Tamanho:** Testar a técnica de **Pruning** (poda de neurônios) para remover conexões com peso zero antes da conversão para TFLite.
* **Velocidade:** Utilizar *Full Integer Quantization* com um dataset representativo para permitir que o modelo rode em hardwares que não possuem unidade de ponto flutuante (FPU).

---
*Relatório final desenvolvido para o desafio técnico de Visão Computacional e Edge AI para o processo seletivo do PNAAT.*
