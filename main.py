import streamlit as st
from streamlit_option_menu import option_menu
import opencv-python as cv2
import mediapipe as mp
import pyautogui


st.set_page_config(
        page_title="TUBES ALPRO", #nama websitenya
        page_icon=":ice_cube:", #icon disamping namanya
        layout="wide",
    )

with st.sidebar:
    selected = option_menu('Menu',# halaman menu
                ['Main', #pilihan 1
                 'Anggota',#pilihan 2
                 'Tentang'], #Pilihan3
                 default_index=0)      

def fungsi(): #membuat fungsi
    x1 = y1 = x2 = y2 = 0  #titik koordinat
    webcam = cv2.VideoCapture(0) #membuka kamera
    my_hands = mp.solutions.hands.Hands() #membuat penanda titik tangan
    drawing_utils = mp.solutions.drawing_utils #menggambar garis penghubung
    while True:
        _ , image = webcam.read() #mengambil gambar dari kamera
        image = cv2.flip(image,1) #membalik gambar secara horizontal
        frame_height, frame_width, _ = image.shape #mengambil ukuran gambar 
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #konversi gambar dari BGR ke RGB
        output = my_hands.process(rgb_image) #proses gambar yang telah dikonversi
        hands = output.multi_hand_landmarks #ambil data tentang titik koordinat tangan yang telah terdeteksi dan diikuti.
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(image, hand) #memberikan tanda pada tangan
                landmarks = hand.landmark #simpan tanda pada tangan kedalam variable landmarks
                for id, landmark in enumerate(landmarks): #buat iterasi untuk menampilkan koordinat setiap landmark menggunakan enumerate()
                    x = int(landmark.x * frame_width) #ini mengalikan koordinat x landmark dengan lebar frame video, kemudian menggunakan fungsi int() untuk mengonversi hasilnya menjadi bilangan bulat
                    y = int(landmark.y * frame_height) #ini melakukan hal yang sama untuk koordinat y, yaitu mengalikan koordinat y landmark dengan tinggi frame video, kemudian menggunakan fungsi int() untuk mengonversi hasilnya menjadi bilangan bulat
                    if id == 8:
                        cv2.circle(img=image, center=(x,y), radius=8, color=(0,255,255), thickness=3) #memberikan lingkaran warna pada telunjuk 
                        x1 = x
                        y1 = y
                    if id == 4:
                        cv2.circle(img=image, center=(x,y), radius=8, color=(0,0,255), thickness=3) #memberikan lingkaran warna pada jempol
                        x2 = x
                        y2 = y
            dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//4 #menghitung jarak jari
            cv2.line(image, (x1,y1), (x2,y2),(0, 255, 0), 5) #memberikan warna hijau untuk jarak jari
            if dist > 50: #jika jarak lebih dari 50
                pyautogui.press("volumeup") #menaikan volume 
            else :
                pyautogui.press("volumedown") #menurunkan volume 
        cv2.imshow("Hand volume Control Using python", image)
        key = cv2.waitKey(10)
        if key == 27: #jika pencet tombol escape
            break
    webcam.release()
    cv2.destroyAllWindows() #tutup program

#Isi Halaman Utama
if (selected == "Main"): #untuk halamain main
    st.title("Mengatur volume dengan jari") #judulnya

    st.write('<h4 style="font-size:24px;">Klik tombol run untuk menjalankan program</h4>', unsafe_allow_html=True) 
    jalan = st.button('Run') 
    if jalan: #jika tombol run di klik
        fungsi() #jalankan fungsi
        st.success('Terima kasih telah mencoba program kami :sparkles: ') #akan tampil ketika aplikasi ditutup
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col2:
        st.image("img/ux.png", width=700) #gambar design
    with col3:
        print("")



#Isi Halaman Anggota
if (selected == "Anggota"): #halaman anggota
    st.title("Anggota Kelompok 1") #judul

    st.markdown("### Berikut merupakan anggota kelompok :") 
    col1, col2, col3, col4, col5 = st.columns(5) #kolom untuk menata foto

    with col1:
       st.image("img/eksanty.jpg")
       st.write('<h4 style="font-size:24px;">1. Eksanty F Sugma I</h4>', unsafe_allow_html=True)
       st.write('<h5 style="font-size:20px;">122450001 </h5>', unsafe_allow_html=True)

    with col2:
       st.image("img/jerem.jpg")
       st.write('<h4 style="font-size:24px;">2. Jeremia Susanto</h4>', unsafe_allow_html=True)
       st.write('<h5 style="font-size:20px;">122450022</h5>', unsafe_allow_html=True)

    with col3:
       st.image("img/vita.jpg")
       st.write('<h4 style="font-size:24px;">3. Vita Anggraini </h4>', unsafe_allow_html=True)
       st.write('<h5 style="font-size:20px;">122450046</h5>', unsafe_allow_html=True)

    with col4:
       st.image("img/fadhil.jpg")
       st.write('<h4 style="font-size:24px;">4. Fadhil Fitra Wijaya</h4>', unsafe_allow_html=True) 
       st.write('<h5 style="font-size:20px;">122450082</h5>', unsafe_allow_html=True)
    
    with col5:
       st.image("img/aji.jpg")
       st.write('<h4 style="font-size:24px;">5. Nurul Alfajar Gumel</h4>', unsafe_allow_html=True)
       st.write('<h5 style="font-size:20px;">122450127</h5>', unsafe_allow_html=True)

    st.image('img/kerkom.jpg')
    st.write('<h5 style="font-size:20px; text-align:center;">Foto Kerja Kelompok 1</h5>', unsafe_allow_html=True)

#Isi Halaman Tentang
if (selected == "Tentang"): #halaman tentang
    st.title("Tentang") #judulnya
    st.write("""<h5 align="justify", style="font-size:24px;">
             Selamat datang dalam program inovatif kami yang memungkinkan Anda mengontrol volume perangkat Anda dengan menggunakan gestur jari yang sederhana. Dengan memanfaatkan teknologi deteksi gestur menggunakan webcam dan pustaka MediaPipe, program ini memungkinkan Anda menyesuaikan volume dengan lebih intuitif dan tanpa perlu menyentuh keyboard atau mouse.   
            Dengan hanya menggerakkan jari Anda di depan webcam, Anda dapat dengan mudah meningkatkan atau mengurangi volume perangkat sesuai keinginan Anda. 
             </h5>""", unsafe_allow_html=True)
    
    st.write("""<h5 align="justify", style="font-size:24px;">
             Proses deteksi gestur ini didasarkan pada analisis posisi dua titik kunci pada tangan, memberikan pengalaman pengguna yang lebih interaktif dan modern.
            Program ini tidak hanya memberikan kemudahan penggunaan, tetapi juga memberikan sentuhan inovatif pada cara kita berinteraksi dengan teknologi. Selamat menggunakan program pengaturan volume berbasis gestur jari ini, dan nikmati pengalaman kontrol yang lebih intuitif dan menyenangkan!
             </h5>""", unsafe_allow_html=True)
    
    st.markdown('') #jarak baris
    st.image("img/lampiran.png") 
