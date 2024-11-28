
# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan
> Submission andrymldni

  <p align="center">
  <img src="https://github.com/user-attachments/assets/ea11584b-66c3-4d0d-9cf6-dd7eaeb55e52" alt="Institute" width="550">
  </p>

## Business Understanding
Jaya Jaya Institut, sebuah institusi pendidikan terkemuka yang telah beroperasi sejak tahun 2000, memiliki reputasi yang sangat baik dalam mencetak lulusan berkualitas tinggi. Namun, institusi ini menghadapi tantangan serius dengan tingginya angka dropout siswa, yang dapat merusak reputasi dan efisiensi operasionalnya. Dengan mengidentifikasi siswa yang berpotensi untuk dropout lebih awal, Jaya Jaya Institut dapat memberikan bimbingan dan dukungan yang diperlukan untuk meningkatkan retensi siswa dan memastikan kelulusan mereka, sehingga mempertahankan reputasi institusi serta meningkatkan kepuasan dan keberhasilan siswa.

### Problem Statements
Jaya Jaya Institut menghadapi tantangan serius dengan tingginya tingkat dropout mahasiswa. Dropout yang tinggi tidak hanya merugikan institusi dari segi reputasi dan keuangan, tetapi juga berdampak negatif pada mahasiswa yang tidak menyelesaikan pendidikan mereka. Tingginya angka dropout dapat mengurangi kepercayaan calon mahasiswa dan orang tua terhadap kualitas pendidikan yang ditawarkan oleh Jaya Jaya Institut.
1. Implementasi teknologi berbasis data untuk mendeteksi mahasiswa yang berisiko tinggi mengalami dropout secara dini.
2. Menyediakan layanan pendampingan akademik dan personal yang dirancang khusus untuk mahasiswa berisiko.
3. Menggunakan dashboard untuk memantau performa individu mahasiswa dan tren dropout secara keseluruhan.
4. Menyoroti upaya institusi dalam mendukung keberhasilan akademik mahasiswa untuk memperkuat citra institusi.

### Project Scope
1. Melakukan analisis kebutuhan institusi yang mencakup tahapan berikut.
   - **Pemahaman Bisnis** (Busness Understanding)
   - **Pemahaman Data** (Data Understanding)
2. Membangun model yang terdiri dari langkah-langkah berikut.
   - **Persiapan Data** (Data Preparation)
   - **Pembuatan Model** (Modeling)
   - **Evaluasi Model** (Model Evaluation)
   - **Pembuatan Dashboard**
3. Pembuatan Dashboard untuk visualisasi hasil analisis dan prediksi.
   - Memanfaatkan model yang telah dikembangkan untuk memprediksi mahasiswa berpotensi dropout, menggunakan model dengan hasil evaluasi terbaik.

### Persiapan
Informasi dataset dapat dilihat pada tabel dibawah ini.
Jenis | Keterangan
--- | ---
Sumber | [UC Irvine Machine Learning Repository : Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)
Lisensi | This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.
Kategori | Academic Performance, Imbalanced Classes, Multi-class classificatioin
Jenis dan Ukuran Berkas | CSV (520.8 KB)

Dataframe ini memiliki 4424 baris dan 36 kolom.

1. Melakukan setup enviroment terlebih dahulu `institute`.
2. Buka cmd/powershell tuliskan.
   ```
   conda create --name intitute python=3.9
   ```
3. Actifkan virtual enviroment yang sebelumnya dibuat dengan menjalankan kode berikut.
   ```
   conda activate institute
   ```
4. Selanjutnya melakukan install library yang dibutuhkan dengan menjalankan kode berikut.
   ```
    pip install requirements.txt
   ```
   atau
   ```
   pip install joblib==1.3.2 matplotlib==3.8.2 scikit_learn==1.2.2 streamlit==1.24.1 numpy==1.25.1 pandas==2.0.3 seaborn==0.12.2 SQLAlchemy==2.0.31
   ```
   kode diatas untuk menginstall dependensi yang digunakan dalam proyek ini
6. Buka jupyter-notebook dengan menjalankan kode berikut.
   ```
   jupyter-notebook .
   ```

## Business Dashboard
Visualisasi data ini memberikan gambaran awal yang menarik mengenai karakteristik mahasiswa. Namun, untuk mendapatkan pemahaman yang lebih mendalam, diperlukan analisis data yang lebih lanjut dengan menggunakan metode statistik yang sesuai. Analisis yang lebih detail dapat membantu mengidentifikasi tren, pola, dan hubungan yang tidak terlihat pada visualisasi ini.

![andrymldni - Dashboard](https://github.com/user-attachments/assets/d260f851-62af-4da4-853a-cff6fadbfcd2)

Email: root@mail.com Password: root123

### Analisis Dashboard
1. Distribusi Mahasiswa Berdasarkan Gender
Dari total **4.424** mahasiswa, mayoritas merupakan perempuan dengan jumlah **2.868** (64,8%), sementara jumlah mahasiswa laki-laki adalah **1.556** (35,2%).
2. Penerima Beasiswa Berdasarkan Gender
Sebagian besar mahasiswa tidak menerima beasiswa, dengan jumlah mahasiswa perempuan **2.001** dan laki-laki **1.324**. Namun, untuk penerima beasiswa, perempuan tetap lebih banyak dengan jumlah **867**, dibandingkan laki-laki yang hanya **232**.
3. Status Mahasiswa
   - **Enrolled (Pendaftaran)**: Dari total **794** mahasiswa yang mendaftar, **61,3%** merupakan perempuan dan **38,7%** laki-laki.
   - **Graduate (Lulusan)**: Terdapat **2.209** lulusan, dengan **75,2%** perempuan dan **24,8%** laki-laki.
   - **Dropout (Putus Kuliah)**: Dari total **1.421** mahasiswa yang dropout, **50,7%** adalah perempuan dan **49,3%** laki-laki.
4. Distribusi Mahasiswa Berdasarkan Jurusan <br>
   Berikut adalah distribusi mahasiswa berdasarkan jurusan:
   - **Nursing (Keperawatan)**: 17,31%
   - **Management**: 8,59%
   - **Social Service**: 8,02%
   - **Veterinary Nursing**: 7,62%
   - **Journalism and Communication**: 7,48%
   - **Advertising and Marketing Management**: 6,06%
   - **Management (Evening Attendance)**: 6,06%
   - **Tourism**: 5,70%
   - **Communication Design**: 5,11%
   - **Animation and Multimedia Design**: 4,86%
   - **Social Service (Evening Attendance)**: 4,86%
   - **Agronomy**: 4,75%
   - **Basic Education**: 4,34%
   - **Informatics Engineering**: 3,84%
   - **Equiculture**: 3,19%
   - **Other**: 2,22%

5. Status Kelulusan Berdasarkan Jurusan dan Gender <br>
   Data kelulusan menunjukkan bahwa mayoritas lulusan adalah perempuan. Beberapa jurusan dengan jumlah lulusan signifikan adalah:
   - **Nursing (Keperawatan)**: 548 lulusan (mayoritas perempuan).
   - **Social Service**: 248 lulusan.
   - **Journalism and Communication**: 196 lulusan.
   - **Management**: 138 lulusan.
   - **Communication Design**: 133 lulusan.

## Implementing a Machine Learning System
Prototipe dapat dijalankan melalui terminal cmd/powershell di direktori proyek.
Jalankan perintah berikut
1. Jalankan `app.py` di terminal dengan kode berikut.
   ```
   streamlit run app.py
   ```
2. Deploy aplikasi streamlit dapat diakses melalui link berikut [streamlit.app](https://andrymldni-status-predictions.streamlit.app/)
   ```
   https://andrymldni-status-predictions.streamlit.app/
   ```

## Conclusion

Berdasarkan hasil analisis data dan pengembangan model prediktif, ditemukan bahwa tingginya angka dropout di Jaya Jaya Institute dipengaruhi oleh beberapa faktor utama, yaitu kondisi ekonomi, prestasi akademik, faktor demografis, serta tingkat dukungan yang diterima mahasiswa. Mahasiswa yang tidak menerima beasiswa atau bantuan keuangan lebih rentan mengalami dropout, terutama mereka yang berasal dari latar belakang keluarga berpenghasilan rendah. Selain itu, mahasiswa dengan nilai rata-rata rendah dan yang gagal memenuhi syarat kelulusan (passing grade) juga memiliki risiko lebih tinggi untuk keluar dari program.

Faktor usia juga berperan penting, di mana mahasiswa yang lebih tua, terutama yang memiliki tanggung jawab tambahan seperti pekerjaan atau keluarga, lebih berisiko mengalami dropout. Secara sosial, mahasiswa yang merasa kurang mendapat dukungan akademik dan tidak terlibat aktif dalam kegiatan kampus juga cenderung tidak mampu menyelesaikan studi. Meskipun jumlah mahasiswa perempuan lebih banyak dibandingkan laki-laki, data menunjukkan bahwa laki-laki lebih rentan mengalami dropout di beberapa jurusan tertentu.

Melalui implementasi model prediktif dan dashboard yang dikembangkan, institusi kini memiliki alat yang efektif untuk mengidentifikasi mahasiswa berisiko dropout secara dini. Dengan demikian, langkah-langkah preventif seperti pemberian beasiswa, peningkatan dukungan akademik, dan bimbingan yang lebih terarah dapat dilakukan. Pendekatan berbasis data ini diharapkan mampu meningkatkan retensi mahasiswa, menjaga reputasi institusi, serta memperkuat efisiensi operasional Jaya Jaya Institute.

### Action Recommendations
Untuk mengurangi tingkat dropout siswa di Jaya Jaya Institut, berikut adalah beberapa langkah strategis yang dapat diambil:  

1. **Peningkatan Program Beasiswa dan Bantuan Keuangan**  
   - Perluasan program beasiswa untuk mencakup lebih banyak siswa yang membutuhkan bantuan finansial, terutama mereka yang memiliki risiko tinggi dropout.  
   - Evaluasi kebijakan beasiswa secara berkala guna memastikan bahwa penerima manfaat adalah siswa yang benar-benar membutuhkan dukungan.  
2. **Penguatan Dukungan Akademik dan Konseling**  
   - Sediakan program bimbingan belajar melalui tutor atau mentor untuk membantu siswa yang mengalami kesulitan akademik.  
   - Berikan layanan konseling akademik dan karier yang berfokus pada membantu siswa mengatasi tantangan akademik dan merencanakan masa depan mereka.  
3. **Pemantauan dan Evaluasi Berkala**  
   - Implementasikan sistem monitoring real-time untuk mendeteksi siswa yang menunjukkan tanda-tanda potensi dropout.  
   - Lakukan evaluasi berkala terhadap program-program yang telah dijalankan untuk memastikan efektivitasnya dalam mengurangi tingkat dropout.  
4. **Kerja Sama dengan Orang Tua dan Komunitas**  
   - Libatkan orang tua secara aktif dalam mendukung perjalanan akademik siswa, termasuk memberikan wawasan terkait perkembangan anak mereka.  
   - Bangun kemitraan dengan komunitas atau organisasi lokal untuk menyediakan sumber daya tambahan yang mendukung kebutuhan siswa.  

Dengan mengadopsi langkah-langkah ini, Jaya Jaya Institut dapat menciptakan lingkungan pembelajaran yang lebih inklusif dan mendukung, sehingga membantu siswa menyelesaikan studi mereka dengan sukses dan mengurangi risiko dropout.
