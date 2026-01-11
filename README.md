# 🔐 Password Generator & Strength Checker

Aplikasi untuk generate password yang kuat dan menganalisis kekuatan password menggunakan Python, Regular Expressions (Regex), dan Streamlit.

## 📋 Daftar Fitur

### 10 Steps Implementation:
1. ✅ **Input panjang password** - Slider untuk memilih panjang (4-128 karakter)
2. ✅ **Tentukan rule** - Checkbox untuk huruf, angka, simbol
3. ✅ **Generate password random** - Algoritma random menggunakan module random
4. ✅ **Tampilkan hasil** - Display dengan UI yang user-friendly
5. ✅ **Regex untuk cek strength** - Pattern matching untuk validasi kriteria
6. ✅ **Kategori weak/medium/strong** - Scoring system dengan 4 kategori kekuatan
7. ✅ **Validasi input user** - Fungsi validasi untuk panjang password
8. ✅ **Modularisasi fungsi** - Pisah ke module: generator, checker, validator, export
9. ✅ **Tambahkan loop retry** - Retry logic dengan maximum attempts
10. ✅ **Export ke file .txt** - Simpan hasil ke file dengan timestamp

## 🏗️ Struktur Project

```
passwordTools/
├── venv/                          # Virtual environment
├── src/                           # Source code modules
│   ├── password_generator.py      # Generate password dengan rules
│   ├── strength_checker.py        # Analisis kekuatan password (regex)
│   ├── input_validator.py         # Validasi & retry logic
│   └── file_export.py             # Export ke file .txt
├── output/                        # Folder untuk menyimpan export hasil
├── app.py                         # Streamlit UI
├── requirements.txt               # Dependency project
└── README.md                      # Dokumentasi ini
```

## 🚀 Cara Menggunakan

### 1. Setup Virtual Environment

```bash
# Masuk ke folder project
cd d:\BelajarPython\passwordTools

# Buat venv (sudah dibuat, hanya untuk referensi)
python -m venv venv

# Activate venv
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan membuka di browser pada `http://localhost:8501`

## 🎯 Cara Kerja Setiap Modul

### password_generator.py
- **generate_password()**: Generate random password dengan rules tertentu
- **get_rules_summary()**: Menampilkan ringkasan rules yang digunakan

**Konsep**: String manipulation + random module

### strength_checker.py
- **check_password_strength()**: Analisis kekuatan password
- **Regex patterns**:
  - `[A-Z]` - Huruf besar
  - `[a-z]` - Huruf kecil
  - `[0-9]` - Angka
  - `[!@#$%^&*...]` - Simbol

**Kategori Strength**:
- 🔴 **Weak** (< 40): Tidak memenuhi kriteria dasar
- 🟡 **Medium** (40-60): Cukup aman untuk penggunaan sehari-hari
- 🟢 **Strong** (60-80): Baik untuk akun penting
- 🔵 **Very Strong** (80+): Sangat aman, recommended untuk akun kritikal

### input_validator.py
- **validate_password_length()**: Validasi input panjang password
- **get_user_input_with_retry()**: Retry logic dengan maximum attempts
- **validate_yes_no()**: Validasi input yes/no

### file_export.py
- **export_to_file()**: Export hasil ke file .txt dengan format rapi
- **read_export_file()**: Baca file yang sudah di-export
- **list_exports()**: List semua file export

## 🎨 UI Features (Streamlit)

### Tab 1: 🎲 Generator
- Slider untuk panjang password
- Checkbox untuk rule selection
- Button generate password
- Display password dengan copy button
- Display rules summary

### Tab 2: 📊 Strength Checker
- Text input untuk password yang ingin dicek
- Analisis kekuatan dengan scoring
- Kriteria yang terpenuhi
- Saran perbaikan
- Export hasil ke file

### Tab 3: 📁 History Export
- List semua file export
- Preview isi file
- Download button untuk tiap file

### Tab 4: ℹ️ Informasi
- Penjelasan tentang aplikasi
- Best practices keamanan password
- Tips penggunaan

## 📊 Scoring System

| Kriteria | Poin | Catatan |
|----------|------|---------|
| Panjang 8+ | 20 | Dasar |
| Panjang 12+ | 15 | Extra |
| Huruf Besar | 15 | A-Z |
| Huruf Kecil | 15 | a-z |
| Angka | 20 | 0-9 |
| Simbol | 15 | !@#$%^&* |
| **Total Max** | **100** | |

## 🔐 Best Practices

1. **Panjang Minimal**: Gunakan 12+ karakter
2. **Kombinasi Karakter**: Campurkan semua jenis karakter (huruf+angka+simbol)
3. **Hindari Pattern**: Jangan gunakan tanggal, nama, urutan keyboard
4. **Unique Password**: Gunakan password berbeda untuk setiap akun
5. **Password Manager**: Simpan password di password manager, bukan di notes

## 🛠️ Teknologi

- **Python 3.8+** - Bahasa pemrograman
- **Streamlit** - Framework untuk membuat web UI
- **Regular Expressions (Regex)** - Pattern matching
- **Random Module** - Generate random password
- **Datetime Module** - Timestamp untuk file export

## 📝 Contoh Usage

### 1. Generate Password
```
1. Buka aplikasi
2. Tentukan panjang password (misal: 16)
3. Pilih rules (default semua tercentang)
4. Klik "Generate Password"
5. Password akan ter-generate dan ditampilkan
```

### 2. Check Password Strength
```
1. Buka tab "Strength Checker"
2. Input password yang ingin dicek
3. Klik "Analisis"
4. Lihat hasil scoring dan saran perbaikan
5. Opsi untuk export hasil
```

### 3. Export Hasil
```
1. Setelah generate atau check password
2. Klik "Export Hasil ke File"
3. File .txt akan tersimpan di folder "output"
4. Buka tab "History Export" untuk melihat riwayat
```

## 🐛 Troubleshooting

### Error: ModuleNotFoundError
```
Solusi: Pastikan berada di directory project dan venv sudah di-activate
```

### Error: streamlit not found
```
Solusi: Install requirements
pip install -r requirements.txt
```

### File export tidak tersimpan
```
Solusi: Pastikan folder "output" exist dan permission write OK
```

## 📚 Pembelajaran Konsep

### String Manipulation
- Menggunakan string methods untuk manipulasi
- Concatenation untuk build password rules

### Random Module
- `random.choice()` untuk memilih karakter random
- `random.seed()` bisa digunakan untuk reproducible results

### Regular Expressions (Regex)
- Pattern matching untuk validasi
- `re.search()` untuk mencari pattern
- Character classes `[A-Z]`, `[a-z]`, `[0-9]`, dll

### File I/O
- Baca dan tulis file dengan encoding UTF-8
- Mkdir untuk membuat direktori
- File naming dengan timestamp

### OOP & Modularization
- Pisah functionality ke module terpisah
- Reusable functions
- Clean code practices

## 📄 License

Educational Project - Bebas untuk digunakan dan dimodifikasi

## 👨‍💻 Author

Created for learning purposes - Password Security & Python Programming

---

**Happy Password Generating! 🔐**
