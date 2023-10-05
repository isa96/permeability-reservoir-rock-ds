import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('../model/permeability_prediction.sav', 'rb'))

st.title('Permeability(D) Prediction based on Porosity and Connate Water Saturation')
st.sidebar.header('Physical Properties of Reservoir Rocks')
image = Image.open('../reports/rig.jpg')
st.image(image, '')

# FUNCTION
def user_report():
  Porosity = st.sidebar.slider('Porosity', 0.000, 0.476, 0.001)
  Swc = st.sidebar.slider('Connate Water Saturation', 0.001, 1.0, 0.001)

  user_report_data = {
      'Porosity':Porosity,
      'Swc':Swc,
  }

  report_data = pd.DataFrame(user_report_data, index=['Data'])
  return report_data

user_data = user_report()
st.header('Physical Properties of Reservoir Rocks')
st.write(user_data)

permeability_pred = model.predict(user_data)
st.subheader('Permeability(D) Prediction:')
st.subheader(str(np.round(permeability_pred[0], 3)) + ' ' + 'Darcy')