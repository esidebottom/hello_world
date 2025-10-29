import streamlit as st

st.title('BMI Calculator')

status=st.radio('select your height format: ', ('cm','m','feet'))
weightstatus=st.radio('select your weight format: ', ('kg','stone'))

if weightstatus=='stone':
    weightStone=(st.text_input('Enter your weight in stone: '))
    weight=weightStone*6.35029
else:
    weight=st.number_input('Enter your weight in kg: ')

if status=='cm':
    height=st.number_input('Enter your height in cm: ')
    try:
        bmi=weight/((height/100)**2)
    except:
        st.text('please enter valid height')
elif status=='m':
    height=st.number_input('Enter your height in meters: ')
    try:
        bmi=weight/(height**2)
    except:
        st.text('please enter valid height')
elif status=='feet':
    height=st.number_input('Enter your height in feet: ')
    try:
        bmi=weight/((height*0.3048)**2)
    except:
        st.text('please enter valid height')

if(st.button('Calculate BMI')):
    if height==0:
        st.text('height cannot be zero')
    else:
        st.text(f'Your BMI is: {bmi}')
        st.text('BMI is a standard measure and does not take into account muscle mass, bone density, overall body composition, and racial and sex differences.')
        if bmi<18.5:
            st.warning('Your bmi score indicates you are underweight')
        elif 18.5<=bmi<24.9:
            st.success('Your bmi score falls within the normal weight range')
        elif 25.0<=bmi<29.9:
            st.error('Your bmi score indicates you are overweight')
        elif 30.0<=bmi<=34.9:
            st.error('Your bmi score indicates you are obese')
        elif 35.0<=bmi<=50.0:
            st.error('Your bmi score indicates you are severely obese')
        else:
            st.error('You may have entered invalid values')
