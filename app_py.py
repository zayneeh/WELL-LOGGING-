import streamlit as st
import numpy as np
import joblib

def main():
    # Load your model
    model = joblib.load('porosity_model.pkl')

    # Title of your app
    st.title('Porosity Prediction App')

    # User inputs for the features
    st.header('Please input the values for the following parameters:')
    density = st.number_input('Density')
    vshale = st.number_input('Vshale')
    delta = st.number_input('Delta')
    gamma = st.number_input('Gamma')
    epsilon = st.number_input('Epsilon')

    # Button to make prediction
    if st.button('Predict Porosity'):
        # Create an array from the input values
        input_data = np.array([[density, vshale, delta, gamma, epsilon]])

        # Predict the porosity
        prediction = model.predict(input_data)

        # Display the prediction
        st.write(f'The predicted porosity is: {prediction[0]}')

# Running the app
if __name__ == '__main__':
    main()
