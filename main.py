import streamlit as st
import pandas as pd
from dataprep import data_preprocessing
from predict import predictions

# Fungsi untuk menampilkan input form
def get_student_data():
    data = {}

    st.title('Student Dropout Prediction')
    st.write('This web app predicts whether a student is likely to drop out based on their academic and personal data.')
    st.write('Fill in the details below:')

    data['Admission_grade'] = st.number_input('Admission Grade', min_value=0, max_value=200, value=0)
    data['Age_at_enrollment'] = st.number_input('Age at Enrollment', min_value=16, max_value=70, value=18)
    data['Application_mode'] = st.selectbox('Application Mode', [1, 2, 5, 7, 10, 16, 17, 18, 26, 27, 39, 43, 44, 51, 53, 57])
    data['Application_order'] = st.selectbox('Application Order', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Input for 1st semester data
    st.subheader('1st Semester Data')
    data['Curricular_units_1st_sem_approved'] = st.number_input('Approved Units', min_value=0, max_value=100, value=0)
    data['Curricular_units_1st_sem_enrolled'] = st.number_input('Enrolled Units', min_value=0, max_value=100, value=0)
    data['Curricular_units_1st_sem_evaluations'] = st.number_input('Evaluations', min_value=0, max_value=100, value=0)
    data['Curricular_units_1st_sem_grade'] = st.number_input('Grade', min_value=0, max_value=20, value=0)
    data['Curricular_units_1st_sem_without_evaluations'] = st.number_input('Units Without Evaluations', min_value=0, max_value=100, value=0)

    # Input for 2nd semester data
    st.subheader('2nd Semester Data')
    data['Curricular_units_2nd_sem_approved'] = st.number_input('Approved Units', min_value=0, max_value=100, value=0)
    data['Curricular_units_2nd_sem_enrolled'] = st.number_input('Enrolled Units', min_value=0, max_value=100, value=0)
    data['Curricular_units_2nd_sem_evaluations'] = st.number_input('Evaluations', min_value=0, max_value=100, value=0)
    data['Curricular_units_2nd_sem_grade'] = st.number_input('Grade', min_value=0, max_value=20, value=0)
    data['Curricular_units_2nd_sem_without_evaluations'] = st.number_input('Units Without Evaluations', min_value=0, max_value=100, value=0)

    # Input for personal data
    st.subheader('Personal Data')
    data['Daytime_evening_attendance'] = st.selectbox('Daytime/Evening Attendance', [0, 1])
    data['Debtor'] = st.selectbox('Debtor', [0, 1])
    data['Displaced'] = st.selectbox('Displaced', [0, 1])
    data['Gender'] = st.selectbox('Gender', [0, 1])
    data['Marital_status'] = st.selectbox('Marital Status', [1, 2, 3, 4, 5, 6])
    data['Mothers_qualification'] = st.selectbox("Mother's Qualification", [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 18, 19, 22, 26, 27, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])
    data['Previous_qualification_grade'] = st.number_input('Previous Qualification Grade', min_value=0, max_value=200, value=0)
    data['Scholarship_holder'] = st.selectbox('Scholarship Holder', [0, 1])
    data['Tuition_fees_up_to_date'] = st.selectbox('Tuition Fees Up to Date', [0, 1])

    return pd.DataFrame([data])

# Fungsi utama
def main():
    data = get_student_data()

    with st.expander('View Raw Data'):
        st.dataframe(data)

    if st.button('Predict'):
        preprocessed_data = data_preprocessing(data)
        
        with st.expander('View Preprocessed Data'):
            st.dataframe(preprocessed_data)
        
        result = predictions(preprocessed_data)
        st.write(f'Prediction: The student is likely to **{result}**.')

if __name__ == '__main__':
    main()
