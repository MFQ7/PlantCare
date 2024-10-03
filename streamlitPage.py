import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("/Users/mohammedalqadda/PlantCare/trained_plantCare_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(256,256))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return predictions


st.header("Plant Recognition")
test_image = st.file_uploader("Choose an Image:")
if test_image:
    if st.button("Show Image"):
        st.image(test_image, use_column_width=True)

    if st.button("Predict"):
        class_name = ['Canna_Indice', 'Canna_Indice_Dead_Leafs', 'Egyptian_White_Guava', 'Noni_Fruit']
        st.write("Our Prediction")
        pred = model_prediction(test_image)
        result_index = np.argmax(pred)
        pred_round = np.round(pred[0], 20)

        result = np.column_stack((class_name, pred_round*100))
        st.write("Our  perdection{}".format(result))
        st.success("Max percentage is {} with {:.2f}% confidence".format(class_name[result_index], pred_round[result_index] * 100))
        if(pred_round[result_index] >= 0.75):
            st.success("Model is Predicting it's a {}".format(class_name[result_index]))
        else:
            st.success("Model is Predicting it's a Unknown Entity")