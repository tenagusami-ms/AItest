"""
Moroney (2021) AI and Machine Learning for Coders
(動かして学ぶAI・機械学習の基礎)
section 2.3
"""
from __future__ import annotations

import numpy as np
import tensorflow as tf


class MyCallback(tf.keras.callbacks.Callback):
    """
    callback class
    """
    def on_epoch_end(self, epoch, logs=None) -> None:
        """
        setting of the end of epoch
        Args:
            epoch(int): epoch number
            logs(dict): logs
        """
        if logs.get('accuracy') > 0.95:
            print('\nReached 95% accuracy so cancelling training!')
            self.model.stop_training = True


def section2_3() -> None:
    """
    section 2.3
    """
    mnist = tf.keras.datasets.fashion_mnist
    (train_images_raw, train_labels), (test_images_raw, test_labels) = mnist.load_data()
    train_images: np.ndarray = train_images_raw / 255.0
    test_images: np.ndarray = test_images_raw / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=50, callbacks=[MyCallback()])
    model.evaluate(test_images, test_labels)

    classifications = model.predict(test_images)
    print(classifications[0])
    print(test_labels[0])
