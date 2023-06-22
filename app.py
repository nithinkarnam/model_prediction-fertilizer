# import numpy as np 
# import pickle
# import pandas as pd
# import streamlit as st 
# import sklearn

# pickled_model = pickle.load(open('ferti.pkl', 'rb'))

# def main():
#     st.title("Prediction of Fertilizer") 
#     html_temp = """
#     <div style="background-color:teal; padding:10px;">
#     <h2 style="color:white; text-align:center;">Fertilizer Forecast App</h2>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)
#     activities1=['Loamy','Sandy','Clayey','Black','Red ']
#     option1 =st.sidebar.selectbox('which Soil Type would you like to use ?',activities1)

#     activities2=['Sugarcane','Cotton','Millets','Paddy','Pulses','Wheat','Tobacco','Barley','Oil seeds','Ground Nuts','Maize']
#     option2 =st.sidebar.selectbox('which Crop Type would you like to use ?',activities2)

#     temperature=st.number_input("Enter the temperature in celcius")
#     humidity=st.number_input("Enter the humidity")
#     nitrogen = st.number_input("Enter the nitrogen content in soil") 
#     potassium = st.number_input("Enter the potassium content in soil")
#     phosphorous = st.number_input("Enter the phosphorous content in soil")

#     soiltype = 3
#     croptype = 3

#     if option1 == 'Loamy':
#         soiltype = 2
#     elif option1 == 'Sandy':
#         soiltype = 4
#     elif option1 == 'Clayey':
#         soiltype = 1
#     elif option1 == 'Black':
#         soiltype = 0
#     else:
#         soiltype = 3

#     if option2 == 'Sugarcane':
#         croptype = 8
#     elif option2 == 'Cotton':
#         croptype = 1
#     elif option2 == 'Millets':
#         croptype = 4
#     elif option2 == 'Paddy':
#         croptype = 6
#     elif option2 == 'Pulses':
#         croptype = 7
#     elif option2 == 'Wheat':
#         croptype = 10
#     elif option2 == 'Tobacco':
#         croptype = 9
#     elif option2 == 'Barley':
#         croptype = 0
#     elif option2 == 'Oil seeds':
#         croptype = 5
#     elif option2 == 'Ground Nuts':
#         croptype = 2
#     else:
#         croptype = 3
    
#     inputs=[[temperature,humidity,soiltype,croptype,nitrogen,potassium,phosphorous]]

#     result=""

#     if st.button('Predict'):
#         result=pickled_model.predict(inputs)
#         if result==6:
#             result="Urea"
#         elif result==5:
#             result="DAP"
#         elif result==4:
#             result="28-28"
#         elif result==3:
#             result="20-20"
#         elif result==2:
#             result="17-17-17"
#         elif result==1:
#             result="14-35-14"
#         elif result==0:
#             result="10-26-26"
#         st.success('Fertilizer to be used is : {}'.format(result))

# if __name__ == '__main__':
#     main()
import pickle
import streamlit as st 

# load the pickled model
pickled_model = pickle.load(open('ferti.pkl', 'rb'))

# define soil and crop options
soil_options = {
    'Loamy': 2,
    'Sandy': 4,
    'Clayey': 1,
    'Black': 0,
    'Red': 3
}

crop_options = {
    'Sugarcane': 8,
    'Cotton': 1,
    'Millets': 4,
    'Paddy': 6,
    'Pulses': 7,
    'Wheat': 10,
    'Tobacco': 9,
    'Barley': 0,
    'Oil seeds': 5,
    'Ground Nuts': 2,
    'Other': 3
}

def main():
    st.set_page_config(page_title="Fertilizer Forecast App", page_icon=":farm:", layout="wide")
    st.title("Fertilizer Prediction")

    # create sidebar options
    st.sidebar.header('Parameters')
    temp = st.sidebar.slider("Temperature (in Celsius)", -30, 50, 25)
    hum = st.sidebar.slider("Humidity", 0, 100, 50)
    nitrogen = st.sidebar.slider("Nitrogen Content in Soil", 0, 200, 100, step=5)
    potassium = st.sidebar.slider("Potassium Content in Soil", 0, 200, 100, step=5)
    phosphorous = st.sidebar.slider("Phosphorous Content in Soil", 0, 200, 100, step=5)

    soil_type = st.sidebar.selectbox(
        "Select Soil Type",
        list(soil_options.keys())
    )

    crop_type = st.sidebar.selectbox(
        "Select Crop Type",
        list(crop_options.keys())
    )

    # get the soil and crop parameters
    soil_param = soil_options[soil_type]
    crop_param = crop_options[crop_type]

    inputs = [[temp, hum, soil_param, crop_param, nitrogen, potassium, phosphorous]]

    if st.sidebar.button("Predict"):
        prediction = pickled_model.predict(inputs)

        # map the predicted value to fertilizer type
        fertilizer_types = {
            0: "10-26-26",
            1: "14-35-14",
            2: "17-17-17",
            3: "20-20",
            4: "28-28",
            5: "DAP",
            6: "Urea"
        }

        result = fertilizer_types[prediction[0]]
        st.success(f"Fertilizer recommended: {result}")

if __name__ == '__main__':
    main()
