import streamlit as st
import pickle

st.title('Heart Disease Prediction App')
#load the pretrained model
with open('heart_disease.pkl','rb') as modelFile:#rb means read binary
    model=pickle.load(modelFile)

st.image('heart_disease.jpg', caption='This app predicts the presence of heart disease based on patient details using a pre-trained machine learning model. Please note that this should not be considered as a diagnosis nor as healthcare advice. Consult a medical professional for any health concerns.')

st.sidebar.header('User instructions:')
st.sidebar.markdown("""
1. Enter the Patient Details in the form.
2. Click 'Predict' to see the survival prediction.
3. Adjust values to test different scenarios.
""")
st.sidebar.info('Example: A 55 year old male with chest pain, high blood pressure, and high cholesterol.')


#function to make predictions
def PredictionFunction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang):
    try:
        prediction=model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang]])
        return prediction

    except Exception as e:
        return f'Error: {str(e)}'
    
def main():
    st.subheader('Enter Patient Details:')
    col1,col2 = st.columns(2)
    #organize inputs in columns
    with col1:
        age=st.slider('Age', 0,100,50)
        sex=st.radio('Sex ', options=['male','female'])
        if sex == 'male':
            sex=1
        else:
            sex=0
        cp=st.radio('Chest pain type: ',options=['typical angina','atypical angina','non-anginal pain','asymptomatic'])
        if cp == 'typical angina':
            cp=1
        elif cp == 'atypical angina':
            cp=2
        elif cp == 'non-anginal pain':
            cp=3
        else:
            cp=4
        trestbps=st.slider('Resting blood pressure (in mm Hg): ',80,200,120)
        chol=st.slider('Serum cholesterol (in mg/dl): ',100,600,150)
        fbs=st.radio('Fasting blood sugar > 120 mg/dl ', options=['normal','ST-T wave abnormality (e.g., T wave inversions, ST elevation/depression > 0.05 mV','showing probable or definite left ventricular hypertrophy by Estes criteria'])
        if fbs=='normal':
            fbs=0
        else:
            fbs=1
    with col2:
        restecg=st.radio('Resting electrocardiographic results: ', options=['normal','ST-T wave abnormality e.g., T wave inversions, ST elevation/depression > 0.05 mV','showing probable or definite left ventricular hypertrophy by Estes criteria'])
        if restecg=='normal':
            restecg=0
        elif restecg=='ST-T wave abnormality e.g., T wave inversions, ST elevation/depression > 0.05 mV':
            restecg=1
        else:
            restecg=2
        thalach=st.slider('Maximum heart rate achieved during excercise: ',60,220,100)
        exang=st.radio('Exercise induced angina: ', options=['yes','no']) 
        if exang=='yes':
            exang=1
        else:
            exang=0

        if st.button('Predict'):
            result=PredictionFunction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang)
            st.markdown(f'Predicted stage of heart disease: {result[0]}')
main()