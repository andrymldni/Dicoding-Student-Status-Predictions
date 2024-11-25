import streamlit as st
import pandas as pd
from dataprep import data_preprocessing
from predict import predictions

st.set_page_config(page_title="Student's Status Prediction",
                page_icon=":mortar_board:",
                layout="wide")

# ----- MAINPAGE -----
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #white;
        margin-bottom: 20px;
    }
    .description {
        text-align: center;
        font-size: 20px;
        color: #white;
        margin-bottom: 30px;
    }
    .divider {
        border: 1px solid #ddd;
        margin: 20px auto;
        width: 80%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Tampilkan judul dan deskripsi dengan emoji menggunakan Unicode
st.markdown('<div class="main-title">&#x1F393; Student\'s Status Prediction</div>', unsafe_allow_html=True)  # mortar_board emoji
st.markdown('<div class="description">This app predicts whether a student will graduate or dropout based on various features.</div>', unsafe_allow_html=True)

# Menambahkan pembatas (divider)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ----- SIDEBAR -----
with st.sidebar:
    # Menampilkan gambar
    st.image("./assets/logo.jpg", caption="andrymldni", use_column_width=True)

    # Menambahkan judul dengan CSS
    st.markdown("<h2 style='text-align: center; font-size:20px;'>Let's connect and collaborate!</h2>", unsafe_allow_html=True)
    
    # Menambahkan baris untuk menampilkan ikon media sosial
    st.markdown(
        """
        <style>
        .social-icons {
            display: flex;
            justify-content: center;
            gap: 25px;  /* Jarak antar ikon */
            padding: 10px;
        }
        .social-icons a {
            text-decoration: none;  /* Menghapus garis bawah pada link */
        }
        </style>
        <div class="social-icons">
            <a href="https://www.linkedin.com/in/andrysyvamldni/" target="_blank">
                <img src="https://skillicons.dev/icons?i=linkedin" width="50">
            </a>
            <a href="https://github.com/andrymldni" target="_blank">
                <img src="https://skillicons.dev/icons?i=github" width="50">
            </a>
            <a href="https://www.instagram.com/andrymldni/" target="_blank">
                <img src="https://skillicons.dev/icons?i=instagram" width="50">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----- INPUT FORM -----
st.header("Input Data Mahasiswa")
data = {}

# Pengelompokan input menggunakan tab
tab1, tab2, tab3, tab4, tab5 = st.tabs(["General Information", "Semester 1", "Semester 2", "Additional Information", "Predictions"])

with tab1:
    # Bagian Umum
    st.subheader("General Information")
    data['Age_at_enrollment'] = st.number_input("Age at Enrollment", min_value=18, max_value=70)
    data['Gender'] = st.selectbox("Gender (0: Female, 1: Male)", [0, 1])
    data['Admission_grade'] = st.number_input("Admission Grade", min_value=0, max_value=200)
    data['Scholarship_holder'] = st.selectbox("Scholarship Holder (0: No, 1: Yes)", [0, 1])
    data['Tuition_fees_up_to_date'] = st.selectbox("Tuition Fees Up-to-date (0: No, 1: Yes)", [0, 1])

with tab2:
# Semester 1
    st.subheader("Data Semester 1")
    data['Curricular_units_1st_sem_enrolled'] = st.number_input("Units Enrolled (1st Sem)", min_value=0, max_value=100)
    data['Curricular_units_1st_sem_approved'] = st.number_input("Units Approved (1st Sem)", min_value=0, max_value=100)
    data['Curricular_units_1st_sem_grade'] = st.number_input("Grade (1st Sem)", min_value=0, max_value=20)
    data['Curricular_units_1st_sem_evaluations'] = st.number_input("Evaluations (1st Sem)", min_value=0, max_value=100)
    data['Curricular_units_1st_sem_without_evaluations'] = st.number_input("Units without Evaluations (1st Sem)", min_value=0, max_value=100)

with tab3:
    # Semester 2
    st.subheader("Data Semester 2")
    data['Curricular_units_2nd_sem_enrolled'] = st.number_input("Units Enrolled (2nd Sem)", min_value=0, max_value=100)
    data['Curricular_units_2nd_sem_approved'] = st.number_input("Units Approved (2nd Sem)", min_value=0, max_value=100)
    data['Curricular_units_2nd_sem_grade'] = st.number_input("Grade (2nd Sem)", min_value=0, max_value=20)
    data['Curricular_units_2nd_sem_evaluations'] = st.number_input("Evaluations (2nd Sem)", min_value=0, max_value=100)
    data['Curricular_units_2nd_sem_without_evaluations'] = st.number_input("Units without Evaluations (2nd Sem)", min_value=0, max_value=100)

with tab4:
    # Informasi Tambahan
    st.subheader("Additional Information")
    data['Daytime_evening_attendance'] = st.selectbox("Daytime/Evening Attendance (0: Daytime, 1: Evening)", [0, 1])
    data['Previous_qualification_grade'] = st.number_input("Previous Qualification Grade", min_value=0, max_value=20)
    data['Application_order'] = st.selectbox('Application Order', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    data['Displaced'] = st.selectbox("Displaced Student (0: No, 1: Yes)", [0, 1])
    data['Marital_status'] = st.selectbox("Marital Status (0: Single, 1: Married)", [0, 1])
    data['Application_mode'] = st.selectbox('Application Mode', [1, 2, 5, 7, 10, 16, 17, 18, 26, 27, 39, 43, 44, 51, 53, 57])
    data['Mothers_qualification'] = st.selectbox("Mother's Qualification", [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 18, 19, 22, 26, 27, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])
    data['Debtor'] = st.selectbox("Debtor (0: No, 1: Yes)", [0, 1])

# Convert to DataFrame
data = pd.DataFrame([data])

with tab5:
    # ----- TAMPILKAN DATA MENTAH -----
    with st.expander("View Raw Input Data"):
        st.table(data.T)
        
    # ----- PREDIKSI -----
    if st.button("Predict"):
        try:
            # Preprocess data
            processed_data = data_preprocessing(data)
            
            # Display processed data
            with st.expander("View Preprocessed Data"):
                st.dataframe(processed_data)
            
            # Make predictions
            result = predictions(processed_data)
            st.success(f"The predicted outcome is: {result}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Menambahkan informasi kredit
st.markdown(
    """
    <div style='text-align: center; margin-top: 50px;'>
        <h5 style='color: #888;'>Copyright ©, created by Andry Syva Maldini</h5>
    </div>
    """,
    unsafe_allow_html=True
)