"""
Run this ONCE locally to convert your Keras model to a smaller TFLite model.
Usage: python convert_model.py
"""

import tensorflow as tf
import os

KERAS_MODEL_PATH = "models/crop_disease_model.keras"
TFLITE_MODEL_PATH = "models/crop_disease_model.tflite"

print("Loading Keras model...")
model = tf.keras.models.load_model(KERAS_MODEL_PATH)

print("Converting to TFLite with quantization...")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # dynamic range quantization

tflite_model = converter.convert()

with open(TFLITE_MODEL_PATH, "wb") as f:
    f.write(tflite_model)

original_size = os.path.getsize(KERAS_MODEL_PATH) / (1024 * 1024)
new_size = os.path.getsize(TFLITE_MODEL_PATH) / (1024 * 1024)

print(f"\nOriginal .keras size : {original_size:.2f} MB")
print(f"New .tflite size      : {new_size:.2f} MB")
print(f"Reduction             : {(1 - new_size/original_size) * 100:.1f}%")
print(f"\nSaved to: {TFLITE_MODEL_PATH}")
