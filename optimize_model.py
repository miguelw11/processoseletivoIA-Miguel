import tensorflow as tf
import os

def main():
    model_path = 'model.h5'
    tflite_model_path = 'model.tflite'

    if not os.path.exists(model_path):
        print(f" Erro: O modelo '{model_path}' não foi encontrado. Execute 'train_model.py' primeiro.")
        return

    print(f"Carregando o modelo salvo '{model_path}'...")
    model = tf.keras.models.load_model(model_path)

    print("Inicializando o conversor TensorFlow Lite...")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    print("Aplicando Dynamic Range Quantization...")
    # Esta flag é o que ativa a otimização de quantização
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    print("Convertendo o modelo...")
    tflite_model = converter.convert()

    print(f"Salvando o modelo otimizado em '{tflite_model_path}'...")
    with open(tflite_model_path, 'wb') as f:
        f.write(tflite_model)

    # Exibe o tamanho dos arquivos para comparação
    h5_size = os.path.getsize(model_path) / 1024
    tflite_size = os.path.getsize(tflite_model_path) / 1024
    
    print("\nConversão e otimização concluídas!")
    print("Comparação de Tamanho:")
    print(f"   - Tamanho Original (.h5): {h5_size:.2f} KB")
    print(f"   - Tamanho Otimizado (.tflite): {tflite_size:.2f} KB")

if __name__ == "__main__":
    main()
