"""
Streamlit UI untuk Password Generator + Strength Checker
Interface yang user-friendly untuk generate dan check password strength
"""

import streamlit as st
import sys
import os

# Add src folder ke path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from password_generator import generate_password, get_rules_summary
from strength_checker import check_password_strength, get_strength_emoji
from file_export import export_to_file, list_exports, read_export_file


# Konfigurasi Streamlit
st.set_page_config(
    page_title="Password Generator & Strength Checker",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        font-weight: 600;
    }
    
    .password-box {
        background-color: #f0f0f0;
        padding: 1rem;
        border-radius: 0.5rem;
        font-family: monospace;
        font-size: 1.2rem;
        border: 2px solid #ddd;
    }
    
    .strength-weak { color: #d32f2f; }
    .strength-medium { color: #f57f17; }
    .strength-strong { color: #388e3c; }
    .strength-very-strong { color: #1976d2; }
    
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🔐 Password Generator & Strength Checker")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Pengaturan")
    
    # Password Length
    st.subheader("Panjang Password")
    password_length = st.slider(
        "Pilih panjang password (karakter)",
        min_value=4,
        max_value=128,
        value=12,
        step=1,
        help="Minimum 4 karakter untuk security basic, recommended 12+ untuk security tinggi"
    )
    
    # Rules Selection
    st.subheader("Aturan Password")
    use_uppercase = st.checkbox("📌 Huruf Besar (A-Z)", value=True)
    use_lowercase = st.checkbox("📌 Huruf Kecil (a-z)", value=True)
    use_numbers = st.checkbox("📌 Angka (0-9)", value=True)
    use_symbols = st.checkbox("📌 Simbol (!@#$%^&*)", value=True)
    
    # Validate minimal 1 rule
    if not any([use_uppercase, use_lowercase, use_numbers, use_symbols]):
        st.error("❌ Minimal pilih 1 aturan!")
        st.stop()

# Main Content - Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🎲 Generator",
    "📊 Strength Checker",
    "📁 History Export",
    "ℹ️ Informasi"
])

# TAB 1: Password Generator
with tab1:
    st.subheader("Generate Password Baru")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        if st.button("🎲 Generate Password", use_container_width=True, type="primary"):
            try:
                # Generate password
                generated_pwd = generate_password(
                    length=password_length,
                    use_uppercase=use_uppercase,
                    use_lowercase=use_lowercase,
                    use_numbers=use_numbers,
                    use_symbols=use_symbols
                )
                
                # Store in session state
                st.session_state.generated_password = generated_pwd
                st.session_state.show_result = True
                
            except ValueError as e:
                st.error(f"❌ Error: {str(e)}")
    
    # Display generated password
    if st.session_state.get('show_result', False) and st.session_state.get('generated_password'):
        st.markdown("---")
        
        pwd = st.session_state.generated_password
        rules_summary = get_rules_summary(use_uppercase, use_lowercase, use_numbers, use_symbols)
        
        # Display password
        st.markdown("#### 🔑 Password yang Dihasilkan:")
        st.code(pwd, language="text")
        
        # Display rules
        st.markdown("#### 📋 Aturan yang Digunakan:")
        st.info(f"✓ {rules_summary}")
        
        # Display length info
        st.markdown(f"#### 📏 Informasi Panjang:")
        st.write(f"Panjang: **{len(pwd)} karakter**")
        
        # Strength analysis
        st.markdown("---")
        st.markdown("#### 📊 Analisis Kekuatan:")
        result = check_password_strength(pwd)
        
        strength = result['strength']
        score = result['score']
        emoji = get_strength_emoji(strength)
        
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.metric("Level", f"{emoji} {strength.value}")
        with col_s2:
            st.metric("Skor", f"{score}/100")
        
        st.progress(score / 100, text=f"{score}% Kuat")
        
        # Generate more options
        st.markdown("---")
        st.markdown("#### 🔄 Opsi Lainnya:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎲 Generate Ulang", use_container_width=True):
                st.rerun()
        
        with col2:
            if st.button("💾 Simpan ke File", use_container_width=True, type="primary"):
                try:
                    filepath = export_to_file(pwd, result, rules_summary)
                    st.success(f"✅ File berhasil disimpan!")
                    st.info(f"📁 {filepath}")
                except IOError as e:
                    st.error(f"❌ Gagal menyimpan: {str(e)}")
        
        with col3:
            if st.button("➕ Lanjut ke Strength Check", use_container_width=True):
                st.session_state.check_strength = True
                st.rerun()
        
        # Check strength automatically
        if st.session_state.get('check_strength', False):
            st.info("Silakan buka tab '📊 Strength Checker' untuk lihat analisis password")


# TAB 2: Strength Checker
with tab2:
    st.subheader("Analisis Kekuatan Password")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        password_input = st.text_input(
            "Masukkan password untuk dicek kekuatannya:",
            type="password",
            placeholder="Masukkan password di sini...",
            help="Password tidak akan disimpan atau dikirim ke server"
        )
    
    with col2:
        st.write("")  # Spacing
        if st.button("✓ Analisis", use_container_width=True, type="primary"):
            if password_input:
                st.session_state.password_to_check = password_input
                st.session_state.show_analysis = True
    
    # Display analysis
    if st.session_state.get('show_analysis', False) and st.session_state.get('password_to_check'):
        pwd = st.session_state.password_to_check
        result = check_password_strength(pwd)
        
        st.markdown("---")
        st.markdown("#### 📊 Hasil Analisis:")
        
        # Strength gauge
        strength = result['strength']
        score = result['score']
        emoji = get_strength_emoji(strength)
        
        # Color coding based on strength
        if score >= 80:
            color = "🟢"
            strength_class = "strength-very-strong"
        elif score >= 60:
            color = "🟢"
            strength_class = "strength-strong"
        elif score >= 40:
            color = "🟡"
            strength_class = "strength-medium"
        else:
            color = "🔴"
            strength_class = "strength-weak"
        
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Level Kekuatan", f"{emoji} {strength.value}")
        
        with col2:
            st.metric("Skor", f"{score}/100")
        
        with col3:
            st.metric("Panjang", f"{len(pwd)} karakter")
        
        with col4:
            st.metric("Tipe Karakter", "")
        
        # Progress bar
        st.markdown("##### 📈 Progress:")
        st.progress(score / 100, text=f"{score}% Kuat")
        
        # Details
        st.markdown("##### ✓ Kriteria yang Terpenuhi:")
        
        details = result['details']
        col1, col2, col3 = st.columns(3)
        
        with col1:
            status_len = "✅" if details['panjang'] else "❌"
            st.write(f"{status_len} Minimal 8 karakter")
            
            status_upper = "✅" if details['huruf_besar'] else "❌"
            st.write(f"{status_upper} Huruf Besar (A-Z)")
        
        with col2:
            status_len_ex = "✅" if details['panjang_extra'] else "❌"
            st.write(f"{status_len_ex} Minimal 12 karakter")
            
            status_lower = "✅" if details['huruf_kecil'] else "❌"
            st.write(f"{status_lower} Huruf Kecil (a-z)")
        
        with col3:
            status_num = "✅" if details['angka'] else "❌"
            st.write(f"{status_num} Angka (0-9)")
            
            status_sym = "✅" if details['simbol'] else "❌"
            st.write(f"{status_sym} Simbol (!@#$%)")
        
        # Recommendations
        if result['feedback']:
            st.markdown("##### 💡 Saran Perbaikan:")
            for i, rec in enumerate(result['feedback'], 1):
                st.write(f"{i}. {rec}")
        else:
            st.success("🎉 Password Anda sudah sangat kuat! Tidak ada saran perbaikan.")
        
        # Export option
        st.markdown("---")
        if st.button("💾 Export Hasil ke File", use_container_width=True):
            try:
                rules_summary = "Password dari Strength Checker"
                filepath = export_to_file(pwd, result, rules_summary)
                st.success(f"✅ File berhasil disimpan!\n\n📁 Path: `{filepath}`")
                st.session_state.last_export = filepath
            except IOError as e:
                st.error(f"❌ Gagal menyimpan file: {str(e)}")


# TAB 3: History & Exports
with tab3:
    st.subheader("📁 History File Export")
    
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    
    # List all exports
    exports = list_exports(output_dir)
    
    if exports:
        st.info(f"📊 Total file yang di-export: **{len(exports)}**")
        
        selected_file = st.selectbox(
            "Pilih file untuk dibaca:",
            options=exports,
            format_func=lambda x: f"📄 {x}"
        )
        
        if selected_file:
            filepath = os.path.join(output_dir, selected_file)
            
            # Read file
            try:
                content = read_export_file(filepath)
                
                # Display content
                st.markdown("##### 📄 Isi File:")
                st.text(content)
                
                # Download button
                st.download_button(
                    label="⬇️ Download File",
                    data=content,
                    file_name=selected_file,
                    mime="text/plain"
                )
                
            except FileNotFoundError as e:
                st.error(f"❌ File tidak ditemukan: {str(e)}")
    else:
        st.info("📭 Belum ada file export. Generate password terlebih dahulu dan export hasilnya!")


# TAB 4: Information
with tab4:
    st.subheader("ℹ️ Informasi Aplikasi")
    
    st.markdown("""
    ### 🎯 Tentang Aplikasi
    Aplikasi **Password Generator & Strength Checker** membantu Anda untuk:
    1. ✅ Generate password yang kuat dan aman
    2. ✅ Menganalisis kekuatan password
    3. ✅ Mendapatkan saran untuk meningkatkan keamanan password
    4. ✅ Export hasil ke file .txt
    
    ---
    
    ### 🔐 Konsep Keamanan Password
    
    #### Jenis-jenis Karakter:
    - **Huruf Besar (A-Z)**: 26 kombinasi
    - **Huruf Kecil (a-z)**: 26 kombinasi
    - **Angka (0-9)**: 10 kombinasi
    - **Simbol**: 32+ simbol spesial
    
    #### Kategori Kekuatan:
    - **🔴 Lemah (Weak)**: Skor < 40 - Sangat rentan terhadap serangan
    - **🟡 Sedang (Medium)**: Skor 40-60 - Cukup aman untuk penggunaan sehari-hari
    - **🟢 Kuat (Strong)**: Skor 60-80 - Baik untuk akun yang penting
    - **🔵 Sangat Kuat (Very Strong)**: Skor 80+ - Sangat aman, recommended untuk akun kritikal
    
    ---
    
    ### 🛡️ Best Practices
    
    1. **Panjang Minimal**: Gunakan minimal 12 karakter
    2. **Kombinasi Karakter**: Campurkan semua jenis karakter
    3. **Hindari Pattern**: Jangan gunakan tanggal, nama, atau urutan keyboard
    4. **Unique Password**: Gunakan password berbeda untuk setiap akun
    5. **Password Manager**: Pertimbangkan menggunakan password manager untuk menyimpan password
    
    ---
    
    ### 🔧 Fitur Utama
    
    - **🎲 Password Generator**: Generate password random dengan aturan custom
    - **📊 Strength Analyzer**: Analisis kekuatan dengan scoring dan saran
    - **📁 File Export**: Simpan hasil ke file .txt dengan format rapi
    - **🔄 Retry Logic**: Validasi input dengan multiple retry attempts
    - **📝 Detailed Feedback**: Saran spesifik untuk improve password
    
    ---
    
    ### 📦 Teknologi yang Digunakan
    
    - **Python 3.8+**: Bahasa pemrograman
    - **Streamlit**: Web framework untuk UI
    - **Regular Expressions (Regex)**: Pattern matching untuk validasi
    - **Random Module**: Generate password random
    
    ---
    
    ### 📌 Tips Penggunaan
    
    1. **Generating**: Sesuaikan panjang dan aturan sesuai kebutuhan
    2. **Checking**: Analisis password Anda atau yang lain untuk tips improvement
    3. **Exporting**: Simpan hasil penting ke file untuk referensi
    4. **History**: Lihat riwayat semua export yang sudah dibuat
    
    """)
    
    st.markdown("---")
    st.info("💡 **Tips**: Password yang kuat adalah kombinasi dari panjang (12+ karakter) + keragaman karakter (huruf + angka + simbol)")


# Initialize session state
if 'generated_password' not in st.session_state:
    st.session_state.generated_password = None
if 'show_result' not in st.session_state:
    st.session_state.show_result = False
if 'check_strength' not in st.session_state:
    st.session_state.check_strength = False
if 'password_to_check' not in st.session_state:
    st.session_state.password_to_check = None
if 'show_analysis' not in st.session_state:
    st.session_state.show_analysis = False
if 'last_export' not in st.session_state:
    st.session_state.last_export = None
