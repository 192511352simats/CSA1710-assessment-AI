import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

print("Test Accuracy:", model.evaluate(x_test, y_test)[1])

n = int(input("Enter test image number (0-9999): "))
print("Predicted Digit:", model.predict(x_test[n:n+1]).argmax())
print("Actual Digit:", y_test[n])
