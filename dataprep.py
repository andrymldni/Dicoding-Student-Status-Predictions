import joblib
import numpy as np
import pandas as pd

scaler_Admission_grade = joblib.load('./model/scaler_Admission_grade.joblib')
scaler_Age_at_enrollment = joblib.load('./model/scaler_Age_at_enrollment.joblib')
scaler_Application_mode = joblib.load('./model/scaler_Application_mode.joblib')
scaler_Application_order = joblib.load('./model/scaler_Application_order.joblib')
scaler_Curricular_units_1st_sem_approved = joblib.load('./model/scaler_Curricular_units_1st_sem_approved.joblib')
scaler_Curricular_units_1st_sem_enrolled = joblib.load('./model/scaler_Curricular_units_1st_sem_enrolled.joblib')
scaler_Curricular_units_1st_sem_evaluations = joblib.load('./model/scaler_Curricular_units_1st_sem_evaluations.joblib')
scaler_Curricular_units_1st_sem_grade = joblib.load('./model/scaler_Curricular_units_1st_sem_grade.joblib')
scaler_Curricular_units_1st_sem_without_evaluations = joblib.load('./model/scaler_Curricular_units_1st_sem_without_evaluations.joblib')
scaler_Curricular_units_2nd_sem_approved = joblib.load('./model/scaler_Curricular_units_2nd_sem_approved.joblib')
scaler_Curricular_units_2nd_sem_enrolled = joblib.load('./model/scaler_Curricular_units_2nd_sem_enrolled.joblib')
scaler_Curricular_units_2nd_sem_evaluations = joblib.load('./model/scaler_Curricular_units_2nd_sem_evaluations.joblib')
scaler_Curricular_units_2nd_sem_grade = joblib.load('./model/scaler_Curricular_units_2nd_sem_grade.joblib')
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load('./model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib')
scaler_Daytime_evening_attendance = joblib.load('./model/scaler_Daytime_evening_attendance.joblib')
scaler_Debtor = joblib.load('./model/scaler_Debtor.joblib')
scaler_Displaced = joblib.load('./model/scaler_Displaced.joblib')
scaler_Gender = joblib.load('./model/scaler_Gender.joblib')
scaler_Marital_status = joblib.load('./model/scaler_Marital_status.joblib')
scaler_Mothers_qualification = joblib.load('./model/scaler_Mothers_qualification.joblib')
scaler_Previous_qualification_grade = joblib.load('./model/scaler_Previous_qualification_grade.joblib')
scaler_Scholarship_holder = joblib.load('./model/scaler_Scholarship_holder.joblib')
scaler_Tuition_fees_up_to_date = joblib.load('./model/scaler_Tuition_fees_up_to_date.joblib')

pca_1 = joblib.load('./model/pca_1.joblib')
pca_2 = joblib.load('./model/pca_2.joblib')

pca_columns_1 = ['Curricular_units_2nd_sem_grade',
                'Curricular_units_2nd_sem_approved',
                'Curricular_units_1st_sem_grade',
                'Curricular_units_1st_sem_approved',
                'Tuition_fees_up_to_date',
                'Scholarship_holder',
                'Curricular_units_2nd_sem_evaluations',
                'Curricular_units_2nd_sem_enrolled',
                'Curricular_units_1st_sem_enrolled',
                'Displaced',
                'Admission_grade',
                'Curricular_units_1st_sem_evaluations',
                'Daytime_evening_attendance',
                'Previous_qualification_grade',
                'Application_order']
pca_columns_2 = ['Curricular_units_1st_sem_without_evaluations',
                'Mothers_qualification',
                'Curricular_units_2nd_sem_without_evaluations',
                'Marital_status',
                'Application_mode',
                'Gender',
                'Debtor',
                'Age_at_enrollment']

def data_preprocessing(data):
    data = data.copy()
    df = pd.DataFrame()
    
    data['Curricular_units_2nd_sem_grade'] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data['Curricular_units_2nd_sem_grade']).reshape(-1, 1))[0]
    data['Curricular_units_2nd_sem_approved'] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data['Curricular_units_2nd_sem_approved']).reshape(-1, 1))[0]
    data['Curricular_units_1st_sem_grade'] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data['Curricular_units_1st_sem_grade']).reshape(-1, 1))[0]
    data['Curricular_units_1st_sem_approved'] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data['Curricular_units_1st_sem_approved']).reshape(-1, 1))[0]
    data['Scholarship_holder'] = scaler_Scholarship_holder.transform(np.asarray(data['Scholarship_holder']).reshape(-1, 1))[0]
    data['Tuition_fees_up_to_date'] = scaler_Tuition_fees_up_to_date.transform(np.asarray(data['Tuition_fees_up_to_date']).reshape(-1, 1))[0]
    data['Curricular_units_2nd_sem_evaluations'] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data['Curricular_units_2nd_sem_evaluations']).reshape(-1, 1))[0]
    data['Curricular_units_2nd_sem_enrolled'] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data['Curricular_units_2nd_sem_enrolled']).reshape(-1, 1))[0]
    data['Curricular_units_1st_sem_enrolled'] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data['Curricular_units_1st_sem_enrolled']).reshape(-1, 1))[0]
    data['Displaced'] = scaler_Displaced.transform(np.asarray(data['Displaced']).reshape(-1, 1))[0]
    data['Admission_grade'] = scaler_Admission_grade.transform(np.asarray(data['Admission_grade']).reshape(-1, 1))[0]
    data['Curricular_units_1st_sem_evaluations'] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data['Curricular_units_1st_sem_evaluations']).reshape(-1, 1))[0]
    data['Daytime_evening_attendance'] = scaler_Daytime_evening_attendance.transform(np.asarray(data['Daytime_evening_attendance']).reshape(-1, 1))[0]
    data['Previous_qualification_grade'] = scaler_Previous_qualification_grade.transform(np.asarray(data['Previous_qualification_grade']).reshape(-1, 1))[0]
    data['Application_order'] = scaler_Application_order.transform(np.asarray(data['Application_order']).reshape(-1, 1))[0]
    
    df[['pc1_1', 'pc1_2', 'pc1_3', 'pc1_4', 'pc1_5', 'pc1_6', 'pc1_7', 'pc1_8', 'pc1_9', 'pc1_10']] = pca_1.transform(data[pca_columns_1])
    
    data['Curricular_units_1st_sem_without_evaluations'] = scaler_Curricular_units_1st_sem_without_evaluations.transform(np.asarray(data['Curricular_units_1st_sem_without_evaluations']).reshape(-1, 1))[0]
    data['Mothers_qualification'] = scaler_Mothers_qualification.transform(np.asarray(data['Mothers_qualification']).reshape(-1, 1))[0]
    data['Curricular_units_2nd_sem_without_evaluations'] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data['Curricular_units_2nd_sem_without_evaluations']).reshape(-1, 1))[0]
    data['Marital_status'] = scaler_Marital_status.transform(np.asarray(data['Marital_status']).reshape(-1, 1))[0]
    data['Application_mode'] = scaler_Application_mode.transform(np.asarray(data['Application_mode']).reshape(-1, 1))[0]
    data['Gender'] = scaler_Gender.transform(np.asarray(data['Gender']).reshape(-1, 1))[0]
    data['Debtor'] = scaler_Debtor.transform(np.asarray(data['Debtor']).reshape(-1, 1))[0]
    data['Age_at_enrollment'] = scaler_Age_at_enrollment.transform(np.asarray(data['Age_at_enrollment']).reshape(-1, 1))[0]

    df[['pc2_1', 'pc2_2', 'pc2_3', 'pc2_4', 'pc2_5', 'pc2_6']] = pca_2.transform(data[pca_columns_2])

    return df