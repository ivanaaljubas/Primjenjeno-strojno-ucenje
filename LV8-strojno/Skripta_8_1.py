from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import os
import matplotlib.pyplot as plt

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

# Strukturiranje konvolucijske neuronske mreže
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

# Definiranje karakteristika procesa učenja pomoću .compile
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Definiranje callbacks
log_dir = os.path.join("logs", "fit", "mnist_model")
tensorboard_callback = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

checkpoint_filepath = 'best_model.keras'
model_checkpoint_callback = callbacks.ModelCheckpoint(
    filepath=checkpoint_filepath,
    save_weights_only=False,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True)

callbacks_list = [tensorboard_callback, model_checkpoint_callback]

# Provođenje treniranja mreže pomoću .fit
history = model.fit(x_train_s, y_train_s,
                    epochs=10,
                    batch_size=64,
                    validation_split=0.1,
                    callbacks=callbacks_list)

# Učitavanje najboljeg modela
best_model = keras.models.load_model(checkpoint_filepath)

# Izračunavanje točnosti mreže na skupu podataka za učenje i skupu podataka za testiranje
train_loss, train_accuracy = best_model.evaluate(x_train_s, y_train_s)
test_loss, test_accuracy = best_model.evaluate(x_test_s, y_test_s)
print(f'Točnost na skupu za učenje: {train_accuracy:.4f}')
print(f'Točnost na skupu za testiranje: {test_accuracy:.4f}')

# Prikaz matrice zabune na skupu podataka za testiranje
y_test_pred = np.argmax(best_model.predict(x_test_s), axis=1)
y_train_pred = np.argmax(best_model.predict(x_train_s), axis=1)

train_cm = confusion_matrix(np.argmax(y_train_s, axis=1), y_train_pred)
test_cm = confusion_matrix(np.argmax(y_test_s, axis=1), y_test_pred)

plt.figure(figsize=(10, 8))
ConfusionMatrixDisplay(train_cm).plot()
plt.title('Matrica zabune - Skup za učenje')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

plt.figure(figsize=(10, 8))
ConfusionMatrixDisplay(test_cm).plot()
plt.title('Matrica zabune - Skup za testiranje')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
