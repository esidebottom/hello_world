import streamlit as st

st.title('Titanic Survival Prediction App')

st.image('titanic.jpg', caption='Predicting Titanic Survivors')

#Sidebar for Instructions

st.sidebar.header('User instructions:')
st.sidebar.markdown("""
1. Enter the Passenger Derails in the form.
2. Click 'Predict' to see the survival prediction.
3. Adjust values to test different scenarios.
""")
st.sidebar.info('Example: A 30 year old male, 3rd class passenger $20 fare, travelling alone from Southhampton.')

#main input form
def main():
    st.subheader('Enter Passenger Details:')
    col1,col2 = st.columns(2)
    #organize inputs in columns
    with col1:
        Pclass=st.selectbox('Passenger Class', options=[1,2,3])
        Sex=st.radio('Sex ', options=['male','female'])
        Age=st.slider('Age: ',0,80,25)
    with col2:
        SibSp=st.slider('Siblings/Spouses Aboard: ',0,8,0)
        Parch=st.slider('Parents/Children Aboard: ',0,6,0)
        Fare=st.slider('Fare ($): ',0.0,500.0,32.0,step=0.1)
        Embarked=st.radio('Embarked From: ', options=['C','Q','S']) #C = Cherbourg, Q = Queenstown, S = Southampton         
#convert categorical inputs to numerical

    Sex = 1 if Sex == 'female' else 0

    Embarked={'C':0,'Q':1,'S':2}[Embarked]

if st.button('Predict'):
    st.balloons()
main()

# #connect to model and predict from jupyter notebook
# import pickle
# model=pickle.load(open('titanic_model.sav','rb'))
# input_data=[[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]]                        
# prediction=model.predict(input_data)
# if prediction[0]==0:
#     st.error('The passenger would not have survived.')
# else:
#     st.success('The passenger would have survived.')    
