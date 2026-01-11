# 🚀 Setup & Run Guide

## Prasyarat
- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Terminal/Command Prompt

## Step 1: Navigasi ke Folder Project

```bash
cd d:\BelajarPython\passwordTools
```

## Step 2: Setup Virtual Environment

Virtual environment sudah dibuat, sekarang tinggal mengaktifkannya:

### Windows (Command Prompt):
```bash
venv\Scripts\activate
```

### Windows (PowerShell):
```powershell
venv\Scripts\Activate.ps1
```

### Linux/Mac:
```bash
source venv/bin/activate
```

**Tanda virtualenv sudah aktif**: Prompt akan berubah menjadi:
```
(venv) C:\...\passwordTools>
```

## Step 3: Install Dependencies (Opsional - hanya untuk Streamlit UI)

```bash
pip install -r requirements.txt
```

Atau langsung install Streamlit:
```bash
pip install streamlit
```

## Step 4: Jalankan Aplikasi

### Opsi A: CLI Version (Recommended untuk testing awal)
CLI version tidak memerlukan Streamlit, jadi bisa langsung dijalankan:

```bash
python cli.py
```

**Keuntungan:**
- ✓ Tidak perlu install Streamlit
- ✓ Interface yang interaktif dengan menu
- ✓ Semua fitur berfungsi dengan baik
- ✓ Cocok untuk testing di terminal

### Opsi B: Web UI Version (Streamlit)
Setelah install requirements.txt:

```bash
streamlit run app.py
```

Aplikasi akan membuka di browser: `http://localhost:8501`

**Keuntungan:**
- ✓ Interface grafis yang cantik
- ✓ Tab-based navigation
- ✓ Real-time display
- ✓ Download file support

## Step 5: Test Aplikasi

Jalankan test script untuk memverifikasi semua module:

```bash
python test_app.py
```

Output akan menampilkan:
```
✓ All integration tests passed!
```

## 📁 Struktur File Penting

```
passwordTools/
├── venv/                    # Virtual environment
├── src/                     # Module source code
│   ├── password_generator.py    # Password generation logic
│   ├── strength_checker.py      # Strength analysis dengan regex
│   ├── input_validator.py       # Input validation & retry
│   └── file_export.py           # File export functionality
├── output/                  # Folder untuk export hasil
├── app.py                   # Streamlit web UI
├── cli.py                   # Command line interface
├── test_app.py             # Integration tests
├── requirements.txt         # Dependencies
└── README.md               # Dokumentasi lengkap
```

## 🎯 Fitur Utama

### 1. Password Generator
- Input panjang password (4-128 karakter)
- Pilih aturan: huruf besar, huruf kecil, angka, simbol
- Generate password random
- Display hasil dengan informasi

### 2. Strength Checker
- Input password untuk dicek
- Analisis kekuatan dengan scoring (0-100)
- Regex pattern matching untuk 5 kriteria
- Kategori: Weak/Medium/Strong/Very Strong
- Saran perbaikan password

### 3. File Export
- Simpan password dan analisis ke file .txt
- Timestamp otomatis untuk setiap file
- Format rapi dan readable
- Bisa dibaca kembali dari history

### 4. Validasi Input
- Validasi panjang password (4-128)
- Retry logic dengan max 3 attempts
- Error handling yang user-friendly

## 🔍 Testing & Validation

### Run Integration Tests:
```bash
python test_app.py
```

Ini akan test:
- ✓ Password generator module
- ✓ Strength checker dengan regex
- ✓ Input validator dengan retry
- ✓ File export functionality
- ✓ Full workflow integration

## 📊 Contoh Output

### CLI Version Output:
```
══════════════════════════════════════════════════════════
               🔐 PASSWORD GENERATOR & STRENGTH CHECKER
══════════════════════════════════════════════════════════

Pilih Menu:
1. 🎲 Generate Password Baru
2. 📊 Check Password Strength
3. 📁 Lihat History Export
4. ℹ️  Informasi
5. ❌ Keluar

Masukkan pilihan (1-5): _
```

### File Export Example:
```
═══════════════════════════════════════════════════════════
               PASSWORD GENERATOR RESULT
═══════════════════════════════════════════════════════════

Generated At: 2026-01-11 10:39:58

PASSWORD
────────────────────────────────────────────────────────────
o"p%rvFN0IoAzm5!

STRENGTH ANALYSIS
────────────────────────────────────────────────────────────
Level: Sangat Kuat
Score: 100/100
```

## 🐛 Troubleshooting

### Issue: "command not found: python"
**Solusi**: Gunakan `python3` atau set Python path dengan benar

### Issue: "No module named streamlit"
**Solusi**: Install streamlit
```bash
pip install streamlit
```

### Issue: "venv not found"
**Solusi**: Buat venv baru
```bash
python -m venv venv
```

### Issue: File tidak tersimpan
**Solusi**: Pastikan folder `output` ada dan permissions OK

### Issue: Regex pattern tidak match
**Solusi**: Sudah built-in, tidak perlu config manual

## 💡 Tips Penggunaan

1. **Mulai dari CLI**: Coba CLI version terlebih dahulu untuk familiarize dengan fitur
2. **Test dengan weak password**: Input `abc123` untuk lihat weakness detection
3. **Coba berbagai kombinasi rules**: Generate dengan kombinasi rule berbeda
4. **Lihat history**: Buka tab History di Streamlit untuk melihat export sebelumnya
5. **Export results**: Simpan hasil penting ke file untuk referensi

## 🎓 Konsep yang Dipelajari

- ✓ **String Manipulation**: Password generation dan processing
- ✓ **Random Module**: Generate random character selection
- ✓ **Regular Expressions (Regex)**: Pattern matching untuk validation
- ✓ **File I/O**: Write/read text files dengan encoding
- ✓ **Modularization**: Pisah code ke module yang reusable
- ✓ **Input Validation**: Validasi dengan retry logic
- ✓ **Web Framework**: Streamlit UI development
- ✓ **CLI Development**: Interactive command-line interface

## 📝 Debugging Tips

Jika ada error, cek:

1. **Python version**: 
   ```bash
   python --version
   ```

2. **Module imports**:
   ```bash
   python -c "import src.password_generator"
   ```

3. **Streamlit install**:
   ```bash
   pip show streamlit
   ```

4. **Output folder**:
   ```bash
   ls -la output/  # atau dir output\ (Windows)
   ```

## ✅ Checklist Setup Sukses

- [x] Python 3.8+ terinstall
- [x] Virtual environment tersedia
- [x] semua module dapat di-import
- [x] Integration tests passed
- [x] CLI version berjalan
- [x] File export berfungsi
- [x] (Optional) Streamlit installed untuk web UI

---

**Semuanya siap! Mulai generate dan check password Anda sekarang! 🔐**
