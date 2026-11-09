import streamlit as st

# ----------------- KONFIGURASI HALAMAN -----------------
st.set_page_config(
    page_title="Inlim Ravijai Rumahorbo | Meteorologist & Data Analyst",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------- CUSTOM CSS MODERN (DARK/CYAN AESTHETIC) -----------------
st.markdown("""
<style>
    /* Background & Main Colors */
    .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }
    
    /* Tagline / Subtitle Pill */
    .tag-hero {
        color: #00d8ff;
        font-family: monospace;
        font-size: 0.95rem;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
    }
    
    /* Header Besar */
    .hero-name {
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.1;
        color: #ffffff;
        margin-bottom: 0.8rem;
    }
    
    .hero-desc {
        font-size: 1.1rem;
        color: #8b949e;
        max-width: 800px;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    /* Card Container */
    .custom-card {
        background-color: rgba(22, 27, 34, 0.8);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .custom-card:hover {
        border-color: #00d8ff;
    }

    /* Style Tab Streamlit */
    .stTabs [data-baseweb="tab-list"] {
        gap: 16px;
        border-bottom: 1px solid #30363d;
    }
    .stTabs [data-baseweb="tab"] {
        color: #8b949e;
        font-family: monospace;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 10px 16px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #00d8ff !important;
        border-bottom-color: #00d8ff !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- HERO HEADER (SEPERTI REFERENSI FOTO) -----------------
col_hero_text, col_hero_avatar = st.columns([2.5, 1], vertical_alignment="center")

with col_hero_text:
    st.markdown('<div class="tag-hero">METEOROLOGY · DATA ANALYTICS · CLIMATE RESILIENCE</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-name">Inlim Ravijai<br>Rumahorbo</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-desc">'
        'Civil Servant & Meteorologist passionate about <b>weather forecasting, remote sensing, and data intelligence</b>. '
        'Bridging the gap between raw atmospheric data and actionable insights for aviation safety and climate-resilient agriculture.'
        '</div>',
        unsafe_allow_html=True
    )
    
    btn_c1, btn_c2, _ = st.columns([1, 1, 2])
    with btn_c1:
        st.link_button("🌐 LinkedIn →", "https://www.linkedin.com/in/inlimravijairumahorbo/", use_container_width=True)
    with btn_c2:
        st.link_button("🐙 GitHub →", "https://github.com/inlimrumahorbo0724", use_container_width=True)

with col_hero_avatar:
    # Avatar frame lingkaran dengan warna toska sesuai desain
    st.image(
        "https://media.licdn.com/dms/image/v2/D5603AQEeTpKRywKaDA/profile-displayphoto-crop_800_800/B56Z0n4fOnGYAI-/0/1774490615193?e=1795651200&v=beta&t=kWsRuc7VV5LVlDullMP_6I4_FNpUgHeUdKmkYYtGT-E",
        caption="📍 Medan / Gunungsitoli, Indonesia",
        use_container_width=True
    )

st.write("")
st.divider()

# ----------------- TAB NAVIGASI UTAMA -----------------
tab_about, tab_exp, tab_projects, tab_edu, tab_pub, tab_contact = st.tabs([
    "ABOUT", 
    "EXPERIENCE", 
    "PROJECTS", 
    "EDUCATION", 
    "PUBLICATIONS & HONORS", 
    "CONTACT"
])

# ================= TAB 1: ABOUT =================
with tab_about:
    st.subheader("Overview & Vision")
    st.write("""
    A Civil Servant in the field of meteorology with a deep interest in the application of meteorological data for agriculture and climate resilience. 
    With 3+ years of experience as a weather forecaster dedicated to aviation safety and public welfare, I leverage strategic thinking, 
    remote sensing, weather analysis, and data engineering to solve real-world environmental challenges.
    """)
    
    st.markdown("### 💡 Core Competencies")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Meteorology & Remote Sensing**")
        st.badge("Atmospheric Analysis")
        st.badge("Aviation Meteorology")
        st.badge("CST & MCST Estimation")
        st.badge("Radar & Satellite")
    with c2:
        st.markdown("**Data Analytics & BI**")
        st.badge("Python & Pandas")
        st.badge("SQL Database")
        st.badge("Streamlit BI")
        st.badge("End-to-End ETL")
    with c3:
        st.markdown("**Professional Skills**")
        st.badge("Operational Leadership")
        st.badge("Strategic Thinking")
        st.badge("Problem Solving")
        st.badge("Multi-agency Coordination")

    st.write("")
    with st.expander("📝 Article: Bridging the Gap Between Weather Data and Analytics", expanded=True):
        st.markdown("""
        > *Working in meteorology means dealing with massive amounts of data every single day, from gathering raw observations at monitoring stations to processing, analyzing, and ultimately forecasting weather patterns.*
        
        To sharpen these skills and build a more structured approach, I completed an intensive 4-month data analytics program and earned my **Data Analyst certification**, mastering the full data lifecycle:
        - 🔹 **Identifying data management needs & planning data integration**
        - 🔹 **Collecting, reviewing, & validating raw meteorological data**
        - 🔹 **Defining data objects & rigorous data cleaning**
        - 🔹 **Developing Business Intelligence (BI) dashboards**
        
        Looking ahead, I am excited to apply these analytical tools to develop crop production systems that are resilient to climate change.
        """)

# ================= TAB 2: EXPERIENCE =================
with tab_exp:
    st.subheader("Professional Experience")

    # Experience 1
    with st.container():
        st.markdown("""
        <div class="custom-card">
            <h4 style="color: #00d8ff; margin-bottom: 4px;">Operational Coordinator</h4>
            <p style="color: #8b949e; margin-bottom: 10px;"><b>Stasiun Meteorologi Binaka</b> • Gunungsitoli, North Sumatra, Indonesia<br>
            <small>Jan 2025 - Present</small></p>
            <ul>
                <li>Bertanggung jawab mengoordinasikan, memandu, dan mengawasi kelancaran kegiatan operasional pengamatan, prakiraan, dan peralatan utama.</li>
                <li>Memastikan laporan bulanan dan buletin terkirim tepat waktu sebelum tanggal 5 setiap bulannya.</li>
                <li>Menghilangkan keterlambatan dan meminimalkan koreksi data hingga 0 insiden pada Januari 2025.</li>
                <li>Mempertahankan efisiensi monitoring dan pemeliharaan alat meteorologi utama tanpa kendala operasional.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Experience 2
    with st.container():
        st.markdown("""
        <div class="custom-card">
            <h4 style="color: #00d8ff; margin-bottom: 4px;">Weather Forecaster</h4>
            <p style="color: #8b949e; margin-bottom: 10px;"><b>Stasiun Meteorologi Binaka</b> • Gunungsitoli, North Sumatra, Indonesia<br>
            <small>Jun 2023 - Present</small></p>
            <ul>
                <li>Menyusun dan mendiseminasikan prakiraan cuaca khusus penerbangan (Aviation Weather) serta cuaca publik wilayah Kepulauan Nias dan sekitarnya.</li>
                <li>Melakukan verifikasi, pemrosesan, dan analisis data penginderaan jauh (*remote sensing*) dengan capaian pengiriman informasi meteorologi penerbangan target 100%.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Experience 3
    with st.container():
        st.markdown("""
        <div class="custom-card">
            <h4 style="color: #00d8ff; margin-bottom: 4px;">Weather Observer</h4>
            <p style="color: #8b949e; margin-bottom: 10px;"><b>Stasiun Meteorologi Binaka</b> • Indonesia<br>
            <small>Feb 2023 - Present</small></p>
            <ul>
                <li>Melakukan pengamatan serta pelaporan data cuaca permukaan (*surface weather*) dan udara atas (*upper air*) untuk kebutuhan keselamatan penerbangan.</li>
                <li>Membangun koordinasi intensif dan harmonis dengan Unit Penyelenggara Bandar Udara (UPBU) Binaka dan AirNav Indonesia.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ================= TAB 3: PROJECTS =================
with tab_projects:
    st.subheader("Featured End-to-End Projects")
    
    col_proj, _ = st.columns([2, 1])
    with col_proj:
        st.markdown("""
        <div class="custom-card">
            <h3 style="color: #00d8ff; margin-bottom: 6px;">🌦️ Weather Analyst: Pulau Nias 2025</h3>
            <p><b>End-to-End Data Analysis & Interactive Dashboard</b></p>
            <p>Proyek analisis komprehensif mengenai pola cuaca, anomali curah hujan, dan dinamika iklim lokal di Kepulauan Nias sepanjang tahun 2025. Mencakup siklus data lengkap mulai dari ekstraksi data mentah stasiun, pembersihan data terstruktur, hingga visualisasi interaktif berbasis Business Intelligence.</p>
            <p><b>Tech Stack:</b> Python • Streamlit • Pandas • Data Visualization • Statistical Analysis</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("🚀 Buka Live Interactive Dashboard", "https://datastudio.google.com/reporting/23630b32-2d5a-4e1e-ab55-f062bb1863ed")

# ================= TAB 4: EDUCATION =================
with tab_edu:
    st.subheader("Academic Background")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.markdown("""
        <div class="custom-card">
            <h4 style="color: #00d8ff;">Sekolah Tinggi Meteorologi Klimatologi dan Geofisika (STMKG)</h4>
            <p><b>Bachelor of Applied Meteorology (S.Tr.Met)</b><br>
            <small>2018 – 2022 | IPK: 3.56 / 4.00</small></p>
            <ul>
                <li>Cadet Association: Climatology Meteorology Cadet Association-STMKG</li>
                <li>Aparatur Resimen Korps Taruna (Police Cadets)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_e2:
        st.markdown("""
        <div class="custom-card">
            <h4 style="color: #00d8ff;">SMA Negeri 4 Pematang Siantar</h4>
            <p><b>High School Diploma — Natural Sciences (MIPA)</b><br>
            <small>2015 – 2018</small></p>
            <ul>
                <li>Top Class Student (Kelas Unggulan)</li>
                <li>Bronze Medalist (Peringkat 3) Olimpiade Fisika Sumatera Utara</li>
                <li>Aktif dalam kegiatan Kepanduan (Scouts)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ================= TAB 5: PUBLICATIONS & HONORS =================
with tab_pub:
    st.subheader("Research Publications & Recognitions")
    
    st.markdown("### 📄 Scientific Publication")
    st.markdown("""
    <div class="custom-card">
        <h4 style="color: #00d8ff;">Penerapan Estimasi Curah Hujan Per Jam Memanfaatkan Metode Convective Stratiform Technique (CST) dan Modified Convective Stratiform Technique (MCST) di Deli Serdang</h4>
        <p style="color: #8b949e;"><i>Studi Kasus: 28 Januari 2020</i></p>
        <p>Riset perbandingan algoritma citra satelit/radar cuaca untuk mengestimasi intensitas curah hujan ekstrem secara spasial dan temporal tinggi.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🏆 Awards & Honors")
    st.markdown("""
    <div class="custom-card">
        <h4 style="color: #00d8ff;">🏅 Finalist — AI DATATHON 2024</h4>
        <p><b>Theme:</b> <i>"Advancing Human Wellbeing Through Climate Change Solutions"</i></p>
        <p>Mengembangkan prototipe solusi analitik berbasis data & AI untuk ketahanan masyarakat terhadap dampak perubahan iklim global.</p>
    </div>
    """, unsafe_allow_html=True)

# ================= TAB 6: CONTACT =================
with tab_contact:
    st.subheader("Let's Collaborate")
    st.write("Silakan tinggalkan pesan untuk diskusi seputar data meteorologi, analisis iklim untuk agrikultur, atau kolaborasi proyek analitik.")
    
    cf_col, _ = st.columns([2, 1])
    with cf_col:
        with st.form("contact_form_inlim", clear_on_submit=True):
            user_name = st.text_input("Nama Lengkap*")
            user_email = st.text_input("Alamat Email*")
            user_subject = st.text_input("Subjek Pesan")
            user_msg = st.text_area("Pesan*")
            
            submit_btn = st.form_submit_button("Kirim Pesan", use_container_width=True)
            if submit_btn:
                if user_name and user_email and user_msg:
                    st.success(f"Terima kasih {user_name}! Pesan berhasil dikirim.")
                else:
                    st.error("Mohon lengkapi semua kolom bertanda bintang (*).")