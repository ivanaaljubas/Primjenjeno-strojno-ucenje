import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Prikaži nekoliko slika iz train skupa
def display_sample_images(x, y):
    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(x[i], cmap=plt.cm.binary)
        plt.xlabel(y[i])
    plt.show()

display_sample_images(x_train, y_train)

# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)

# Kreiraj mrežu pomoću keras.Sequential() i prikaži njenu strukturu pomoću .summary()
model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(512, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.summary()

# Definiraj karakteristike procesa učenja pomoću .compile()
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Provodi treniranje mreže pomoću .fit()
history = model.fit(x_train_s, y_train_s, epochs=10, batch_size=128, validation_split=0.2)

# Izračunajte točnost mreže na skupu podataka za učenje i skupu podataka za testiranje
train_loss, train_acc = model.evaluate(x_train_s, y_train_s, verbose=2)
test_loss, test_acc = model.evaluate(x_test_s, y_test_s, verbose=2)
print(f'Točnost na skupu za učenje: {train_acc:.4f}')
print(f'Točnost na skupu za testiranje: {test_acc:.4f}')

# Prikazite matricu zabune na skupu podataka za testiranje
y_test_pred = model.predict(x_test_s)
y_test_pred_classes = np.argmax(y_test_pred, axis=1)
y_test_true = np.argmax(y_test_s, axis=1)

cm = confusion_matrix(y_test_true, y_test_pred_classes)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.arange(10))

disp.plot(cmap=plt.cm.Blues)
plt.show()

# Prikazite matricu zabune na skupu podataka za učenje
y_train_pred = model.predict(x_train_s)
y_train_pred_classes = np.argmax(y_train_pred, axis=1)
y_train_true = np.argmax(y_train_s, axis=1)

cm_train = confusion_matrix(y_train_true, y_train_pred_classes)
disp_train = ConfusionMatrixDisplay(confusion_matrix=cm_train, display_labels=np.arange(10))

disp_train.plot(cmap=plt.cm.Blues)
plt.show()

# Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreža pogrešno klasificirala
def display_errors(x, y_true, y_pred, n=10):
    errors = np.where(y_pred != y_true)[0]
    plt.figure(figsize=(10,10))
    for i, error in enumerate(errors[:n]):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(x[error].reshape(28,28), cmap=plt.cm.binary)
        plt.xlabel(f'True: {y_true[error]}, Pred: {y_pred[error]}')
    plt.show()

display_errors(x_test, y_test_true, y_test_pred_classes)
