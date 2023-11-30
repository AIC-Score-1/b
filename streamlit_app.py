import streamlit as st
import numpy as np
import pickle
import sklearn


page = st.sidebar.selectbox("Select Activity", ["Prediction",])
st.sidebar.text(" \n")

pkl_file2 = open('rfc.pkl', 'rb')
rfc = pickle.load(pkl_file2)

d = {'female': {0.0, 1.0},
 'smoker': {0.0, 1.0},
 'alcohol': {0.0, 1.0},
 'nutrition': {0, 1, 2, 3, 4, 5, 6, 7},
 'prior': {0.0, 1.0},
 'leukocytosis': {0.0, 1.0},
 'steroids': {0.0, 1.0},
 'asa': {1, 2, 3, 4, 5},
 'renal': {"G1", "G2", "G3", "G4", "G5"},
 'hand': {0.0, 1.0},
 'emergent': {0.0, 1.0},
 'laparoscopic': {1.0, 2.0, 3.0},
 'type': {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0},
 'indication': {1.0, 2.0, 3.0, 4.0, 5.0, 6.0},
 'perforation ': {0.0, 1.0},
 'ct': {0.0, 1.0, 2.0, 3.0, 4.0},
 'cn': {0.0, 1.0, 2.0},
 'cm': {0.0, 1.0},
 'livermets': {0.0, 1.0},
 'ai': {0.0, 1.0}}


if page=="Prediction":

    st.header("Prediction. Not to be currently used for clinical purposes")
    st.text(" \n")

    form = st.form(key='my_form2')

    x1 = form.slider(label='Charlson Comorbidity Index (CCI)', min_value = 0, max_value = 20, step = 1, value = 4)
    form.text(" \n")

    x2 = form.slider(label='Age (years)', min_value = 18, max_value = 105, step = 1, value = 65)
    form.text(" \n")


    x3 = form.slider(label='Albumin', min_value = 0.0, max_value = 5.0, step = 0.1, value = 3.0)
    form.text(" \n")


    x4 = form.slider(label='Body Mass Index (BMI)', min_value = 15.0, max_value = 60.0, step = 0.1, value = 26.0)
    form.text(" \n")

    x5 = form.slider(label='Hemoglobin level (in g/dL)', min_value = 0.0, max_value = 20.0, step = 0.1, value = 13.0)
    form.text(" \n")



    x6 = form.selectbox(' Alcohol abuse (>2 alcoholic beverages per day)',["YES","NO"], key=1)
    form.text(" \n")

    x7 = form.selectbox('American Society of Anesthesiologists (ASA) Score',list(d["asa"]),key=1)
    form.text(" \n")


    x8 = form.selectbox("Gender",["MALE","FEMALE"],key=1)
    form.text(" \n")


    x9 = form.selectbox('Leukocytosis',["YES","NO"],key=1)
    form.text(" \n")

    x11 = form.selectbox('Prior Abdominal Surgery',["YES","NO"],key=1)
    form.text(" \n")

    x12 = form.selectbox("Renal function (CKD Stages G1 (normal) to G5)",["G1", "G2", "G3", "G4", "G5"],key=1)
    form.text(" \n")




    x13 = form.selectbox("Active smoking",["YES","NO"],key=1)
    form.text(" \n")



    x14 = form.selectbox("Preoperative steroid use",["YES","NO"],key=1)
    form.text(" \n")


    submit_button = form.form_submit_button(label='Predict')



    if submit_button:
        l = {"YES":1,"NO":0}
        f = {"MALE":0,"FEMALE":1}
        n = {0:0.0, 1:1.0,2:2.0,3:3.0,4:4.0,5:5.0,6:6.0,7:9.0}
        r = {"G1":1.0, "G2":2.0, "G3":3.0, "G4":4.0, "G5":5.0}
       
        x1 = (float(x1) - 0.0)/(18.0 - 0.0) 
        x2 = (float(x2) - 16.0)/(101.0 - 16.0)
        x3 = (float(x3) - 1.1)/(8.0 - 1.1)
        x4 = (float(x4) - 15.0)/(59.5 - 15.0)
        x5 = (float(x5) - 6.0)/(140.0 - 6.0)

        x6 = float(l[x6])
        x7 = float(x7) / 5.0
        x8 = float(f[x8])
        x9 = float(l[x9])
        x11 = float(l[x11])
        x12 = float(r[x12]) / 5.0
        x13 = float(l[x13])

        x14 = float(l[x14])

        
        c1 = rfc.predict_proba(np.array([x2,x8,x4,x13,x6,x11,x9,x14,x1,x7,x12,x3,x5]).reshape(1, -1))[:, 1]

        c2 = c1 > 0.218366108449497



        st.header("probability to have Anastomotic insufficiency :")
        st.text(f'{int(round(c1[0] * 100))}%')
        st.header("Predicted output(based on Binary Classification cut-off threshold)")
        if c2[0] == False:
         value = "Does not have Anastomotic insufficiency "
        else : 
         value = "Does have Anastomotic insufficiency "
        
        st.text(value)
