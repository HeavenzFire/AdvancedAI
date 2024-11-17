import tensorflow as tf

class AISymphony:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def process(self, input_data):
        return self.model.predict(input_data)
