"""
Moroney (2021) AI and Machine Learning for Coders
(動かして学ぶAI・機械学習の基礎)
section 1.6
"""
from __future__ import annotations

from typing import Final

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense


def section1_6() -> None:
    """
    section 1.6
    """
    l0: Dense = Dense(units=1, input_shape=[1])
    model: Sequential = Sequential([l0])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.summary()

    xs: Final[np.array] = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
    ys: Final[np.array] = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

    model.fit(xs, ys, epochs=500)
    print(model.predict([10.0]))
    print(f"Here is what I learned: {l0.get_weights()}")
