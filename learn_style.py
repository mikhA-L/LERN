import streamlit as st

st.set_page_config(page_title="Tes Gaya Belajar", page_icon="📚", layout="centered")

# Judul aplikasi
st.title("Tes Gaya Belajar")

# Penjelasan singkat
st.write("Jawab pertanyaan di bawah ini untuk mengetahui apakah gaya belajar Anda lebih dominan Visual, Auditori, atau Kinestetik.")

# Pertanyaan dan opsi
questions = [
    ("1. Bagaimana cara terbaik kamu memahami pelajaran?", 
     ["Melihat gambar atau diagram", "Mendengarkan penjelasan", "Melakukan langsung"]),
    ("2. Saat belajar, saya lebih suka...", 
     ["Membaca catatan sendiri", "Mendengarkan rekaman", "Membuat model atau eksperimen"]),
    ("3. Saya lebih mudah mengingat informasi ketika...", 
     ["Melihatnya dalam bentuk grafik", "Mendengarnya", "Menyentuh atau mempraktikkannya"]),
    ("4. Saat membaca buku, saya lebih suka...", 
     ["Melihat gambar, grafik, atau tabel", "Membaca dengan suara keras", "Mencatat sambil berjalan"]),
    ("5. Jika belajar keterampilan baru, saya akan...", 
     ["Melihat tutorial atau gambar", "Mendengarkan instruksi", "Langsung mencoba"]),
    ("6. Saat mendengarkan pelajaran, saya sering...", 
     ["Membuat catatan dengan diagram", "Fokus mendengarkan", "Menggerakkan tangan atau mengetuk meja"]),
    ("7. Jika harus menjelaskan sesuatu kepada orang lain, saya lebih suka...", 
     ["Menggunakan gambar atau grafik", "Menjelaskannya secara lisan", "Menunjukkan cara melakukannya"]),
    ("8. Ketika saya lupa sesuatu, saya lebih mudah mengingatnya jika...", 
     ["Melihat catatan atau gambar", "Mengulanginya dalam pikiran", "Melakukan aktivitas terkait"]),
    ("9. Jika menghadiri seminar, saya lebih suka...", 
     ["Slide dengan banyak diagram", "Penjelasan verbal", "Demonstrasi interaktif"]),
    ("10. Saat menghadapi ujian, saya lebih nyaman jika...", 
     ["Ada diagram atau peta konsep", "Diskusi pertanyaan", "Ada tugas praktik"]),
    ("11. Saat menonton film, saya fokus pada...", 
     ["Visual dan efek grafis", "Dialog dan suara", "Adegan aksi"]),
    ("12. Ketika harus mengingat lokasi, saya lebih mudah jika...", 
     ["Melihat peta", "Mendengarkan arahan", "Mengunjungi langsung"]),
]

# Skor awal
visual, auditori, kinestetik = 0, 0, 0

# Loop untuk setiap pertanyaan
for i, (question, options) in enumerate(questions):
    st.markdown(f"<h3 style='font-size:20px; color:#f1f1f1;'>{question}</h3>", unsafe_allow_html=True)  # Perbesar font soal
    answer = st.radio("", options, key=i)  # Kosongkan label untuk menghindari duplikasi
    if answer == options[0]:
        visual += 1
    elif answer == options[1]:
        auditori += 1
    elif answer == options[2]:
        kinestetik += 1

# Tombol untuk melihat hasil
if st.button("Lihat Hasil"):
    st.subheader("Hasil Tes Gaya Belajar")
    if visual > auditori and visual > kinestetik:
        st.write("**Gaya Belajar Anda: Visual**")
        st.write("Anda lebih mudah belajar dengan melihat gambar, diagram, dan warna.")
    elif auditori > visual and auditori > kinestetik:
        st.write("**Gaya Belajar Anda: Auditori**")
        st.write("Anda lebih mudah memahami pelajaran dengan mendengarkan dan berbicara.")
    elif kinestetik > visual and kinestetik > auditori:
        st.write("**Gaya Belajar Anda: Kinestetik**")
        st.write("Anda lebih suka belajar dengan praktik langsung atau eksperimen.")
    else:
        st.write("**Gaya Belajar Anda Kombinasi**")
        st.write("Anda memiliki preferensi yang seimbang antara Visual, Auditori, dan Kinestetik.")

    st.write(f"Skor: Visual ({visual}), Auditori ({auditori}), Kinestetik ({kinestetik})")
