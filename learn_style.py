import streamlit as st

# Judul Aplikasi
st.set_page_config(page_title="Tes Gaya Belajar", page_icon="📚", layout="centered")
st.title("Kuisioner Evaluasi Gaya Belajar")

st.write("### Petunjuk:")
st.write("Jawablah pertanyaan di bawah ini untuk mengetahui gaya belajar Anda.")

# Variabel untuk menyimpan skor gaya belajar
skor = {"Visual": 0, "Auditori": 0, "Kinestetik": 0, "Membaca": 0}

# Pertanyaan kuisioner dan kategori skornya
pertanyaan = [
    ("Bagaimana cara terbaik bagi Anda untuk memahami materi pelajaran?", 
        ["Membaca buku atau modul", "Mendengarkan penjelasan guru", "Melihat gambar, diagram, atau video", "Praktik langsung atau diskusi kelompok"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),

    ("Saat mengikuti pembelajaran, saya lebih suka jika...",
        ["Guru menjelaskan dengan presentasi dan gambar", "Guru menjelaskan dengan suara cerita", "Guru memberikan latihan dan praktik langsung", "Guru memberikan tugas individu untuk memahami materi"],
        ["Visual", "Auditori", "Kinestetik", "Membaca"]),

    ("Metode pembelajaran mana yang menurut Anda paling efektif?",
        ["Tatap muka di kelas dengan penjelasan guru", "Pembelajaran berbasis buku atau modul cetak", "Pembelajaran digital (video, animasi, atau simulasi online)", "Diskusi kelompok atau praktik langsung"],
        ["Auditori", "Membaca", "Visual", "Kinestetik"]),

    ("Ketika saya kesulitan memahami materi, saya lebih suka...",
        ["Membaca ulang materi dari buku atau catatan", "Menonton video pembelajaran terkait", "Bertanya langsung kepada guru", "Berdiskusi dengan teman"],
        ["Membaca", "Visual", "Auditori", "Kinestetik"]),

    ("Jika ada perubahan dalam metode pembelajaran, Anda ingin lebih banyak...",
        ["Materi dalam bentuk video atau gambar", "Materi dalam bentuk teks atau modul cetak", "Diskusi dan praktik langsung di kelas", "Latihan soal dan evaluasi mandiri"],
        ["Visual", "Membaca", "Kinestetik", "Membaca"]),

    ("Saat belajar sendiri, saya lebih suka...",
        ["Membaca buku atau modul", "Mendengarkan rekaman penjelasan", "Menonton video pembelajaran", "Melakukan eksperimen atau latihan"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),

    ("Saya lebih mudah mengingat informasi jika...",
        ["Membaca dan mencatat ulang", "Mendengarkan dan berdiskusi", "Melihat diagram atau ilustrasi", "Melakukan praktik langsung"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),

    ("Ketika mengerjakan tugas, saya lebih suka...",
        ["Menulis ringkasan atau catatan", "Mendiskusikan dengan teman atau guru", "Menggunakan peta konsep atau mind map", "Mencoba menyelesaikan dengan eksperimen"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),

    ("Bagaimana cara terbaik bagi Anda untuk mengingat pelajaran?",
        ["Membaca ulang dan mencatat", "Mendengarkan rekaman atau berdiskusi", "Melihat gambar atau peta konsep", "Melakukan kegiatan atau praktik"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),

    ("Saya lebih suka belajar melalui...",
        ["Buku atau teks", "Audio atau podcast", "Video atau gambar", "Percobaan atau kegiatan langsung"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),

    # 🔹 PERTANYAAN TAMBAHAN
    ("Bagaimana cara Anda mencatat materi di kelas?",
        ["Menulis ringkasan atau catatan", "Merekam suara penjelasan guru", "Membuat diagram atau peta konsep", "Tidak mencatat, lebih suka praktik"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),

    ("Ketika membaca buku pelajaran, saya lebih suka...",
        ["Membaca seluruh isi buku dan mencatat", "Mendengarkan audio book atau rekaman", "Melihat ilustrasi dan gambar", "Mencoba menerapkan isi buku dalam latihan"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),

    ("Saat menonton video pembelajaran, saya lebih sering...",
        ["Mencatat poin-poin penting", "Mendengarkan tanpa mencatat", "Melihat gambar dan animasi", "Mencoba praktik langsung dari video"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),

    ("Bagaimana Anda biasanya memahami konsep baru?",
        ["Membaca buku atau catatan", "Mendiskusikan dengan teman/guru", "Melihat gambar, peta konsep, atau video", "Melakukan eksperimen langsung"],
        ["Membaca", "Auditori", "Visual", "Kinestetik"]),
]

# Loop untuk menampilkan pertanyaan dan menyimpan jawaban
for i, (pertanyaan_teks, opsi, kategori) in enumerate(pertanyaan, 1):
    st.write(f"## {i}. {pertanyaan_teks}")
    jawaban = st.radio("", opsi, key=f"q{i}")
    skor[kategori[opsi.index(jawaban)]] += 1

# 🔹 PERTANYAAN TERBUKA
st.write("## 15. Apa yang bisa diperbaiki dari sistem pembelajaran saat ini?")
jawaban_terbuka = st.text_area("Tuliskan pendapat Anda di sini...", key="q15")

# Menentukan gaya belajar dominan
gaya_belajar = max(skor, key=skor.get)

# Tampilkan hasil
if st.button("Lihat Hasil"):
    st.write("Hasil Evaluasi Gaya Belajar Anda")
    st.write(f"**Gaya belajar dominan Anda adalah: {gaya_belajar}**")
    
    st.write("### Rincian Skor:")
    for tipe, nilai in skor.items():
        st.write(f"- {tipe}: {nilai}")

    # Menampilkan jawaban terbuka
    if jawaban_terbuka.strip():
        st.write("### Saran Perbaikan:")
        st.write(jawaban_terbuka)
