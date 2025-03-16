import streamlit as st

# Judul Aplikasi
st.title("Kuisioner Evaluasi Gaya Belajar")

st.write("### Petunjuk:")
st.write("Jawablah pertanyaan di bawah ini untuk mengetahui gaya belajar Anda.")

# Variabel untuk menyimpan skor gaya belajar
skor_visual = 0
skor_auditori = 0
skor_kinestetik = 0
skor_membaca = 0

# ---- Pertanyaan Kuisioner ----
st.write("## 1. Bagaimana cara terbaik bagi Anda untuk memahami materi pelajaran?")
q1 = st.radio("", ["Membaca buku atau modul", "Mendengarkan penjelasan guru", "Melihat gambar, diagram, atau video", "Praktik langsung atau diskusi kelompok"])
if q1 == "Membaca buku atau modul":
    skor_membaca += 1
elif q1 == "Mendengarkan penjelasan guru":
    skor_auditori += 1
elif q1 == "Melihat gambar, diagram, atau video":
    skor_visual += 1
elif q1 == "Praktik langsung atau diskusi kelompok":
    skor_kinestetik += 1

st.write("## 2. Saat mengikuti pembelajaran, saya lebih suka jika...")
q2 = st.radio("", ["Guru menjelaskan dengan presentasi dan gambar", "Guru menjelaskan dengan suara cerita", "Guru memberikan latihan dan praktik langsung", "Guru memberikan tugas individu untuk memahami materi"])
if q2 == "Guru menjelaskan dengan presentasi dan gambar":
    skor_visual += 1
elif q2 == "Guru menjelaskan dengan suara cerita":
    skor_auditori += 1
elif q2 == "Guru memberikan latihan dan praktik langsung":
    skor_kinestetik += 1
elif q2 == "Guru memberikan tugas individu untuk memahami materi":
    skor_membaca += 1

st.write("## 3. Apakah materi yang disampaikan oleh guru selama ini mudah dipahami?")
q3 = st.radio("", ["Sangat mudah dipahami", "Cukup mudah dipahami", "Sulit dipahami", "Sangat sulit dipahami"])
# Pertanyaan ini tidak mempengaruhi gaya belajar

st.write("## 4. Metode pembelajaran mana yang menurut Anda paling efektif?")
q4 = st.radio("", ["Tatap muka di kelas dengan penjelasan guru", "Pembelajaran berbasis buku atau modul cetak", "Pembelajaran digital (video, animasi, atau simulasi online)", "Diskusi kelompok atau praktik langsung"])
if q4 == "Pembelajaran berbasis buku atau modul cetak":
    skor_membaca += 1
elif q4 == "Pembelajaran digital (video, animasi, atau simulasi online)":
    skor_visual += 1
elif q4 == "Diskusi kelompok atau praktik langsung":
    skor_kinestetik += 1
elif q4 == "Tatap muka di kelas dengan penjelasan guru":
    skor_auditori += 1

st.write("## 5. Bagaimana cara penyampaian materi oleh guru selama ini?")
q5 = st.radio("", ["Sangat menarik dan jelas", "Cukup menarik, tapi masih perlu perbaikan", "Kurang menarik dan sering membingungkan", "Tidak menarik dan sulit dipahami"])
# Pertanyaan ini tidak mempengaruhi gaya belajar

st.write("## 6. Ketika saya kesulitan memahami materi, saya lebih suka...")
q6 = st.radio("", ["Membaca ulang materi dari buku atau catatan", "Menonton video pembelajaran terkait", "Bertanya langsung kepada guru", "Berdiskusi dengan teman"])
if q6 == "Membaca ulang materi dari buku atau catatan":
    skor_membaca += 1
elif q6 == "Menonton video pembelajaran terkait":
    skor_visual += 1
elif q6 == "Bertanya langsung kepada guru":
    skor_auditori += 1
elif q6 == "Berdiskusi dengan teman":
    skor_kinestetik += 1

st.write("## 7. Seberapa sering Anda menggunakan teknologi (laptop, handphone, aplikasi edukasi) dalam belajar?")
q7 = st.radio("", ["Setiap hari", "Beberapa kali seminggu", "Jarang", "Tidak pernah"])
# Pertanyaan ini tidak mempengaruhi gaya belajar

st.write("## 8. Bagaimana tingkat kepuasan Anda terhadap pembelajaran yang telah dilakukan selama ini?")
q8 = st.radio("", ["Sangat puas", "Cukup puas", "Kurang puas", "Tidak puas"])
# Pertanyaan ini tidak mempengaruhi gaya belajar

st.write("## 9. Jika ada perubahan dalam metode pembelajaran, Anda ingin lebih banyak...")
q9 = st.radio("", ["Materi dalam bentuk video atau gambar", "Materi dalam bentuk teks atau modul cetak", "Diskusi dan praktik langsung di kelas", "Latihan soal dan evaluasi mandiri"])
if q9 == "Materi dalam bentuk video atau gambar":
    skor_visual += 1
elif q9 == "Materi dalam bentuk teks atau modul cetak":
    skor_membaca += 1
elif q9 == "Diskusi dan praktik langsung di kelas":
    skor_kinestetik += 1
elif q9 == "Latihan soal dan evaluasi mandiri":
    skor_membaca += 1

st.write("## 10. Apa yang bisa diperbaiki dari sistem pembelajaran saat ini?")
q10 = st.text_area("Jawaban terbuka")

# ---- Hasil Gaya Belajar ----
if st.button("Lihat Gaya Belajar Anda"):
    hasil = {
        "Visual": skor_visual,
        "Auditori": skor_auditori,
        "Kinestetik": skor_kinestetik,
        "Membaca/Menulis": skor_membaca
    }

    gaya_belajar = max(hasil, key=hasil.get)

    st.success(f"Gaya belajar utama Anda adalah {gaya_belajar}.")

    # Menampilkan penjelasan gaya belajar
    if gaya_belajar == "Visual":
        st.write("Anda lebih mudah belajar melalui gambar, diagram, video, dan presentasi.")
    elif gaya_belajar == "Auditori":
        st.write("Anda lebih mudah belajar dengan mendengarkan penjelasan atau diskusi verbal.")
    elif gaya_belajar == "Kinestetik":
        st.write("Anda lebih suka belajar dengan praktik langsung dan aktivitas fisik.")
    elif gaya_belajar == "Membaca/Menulis":
        st.write("Anda lebih suka belajar dengan membaca buku, mencatat, dan menulis ringkasan.")
