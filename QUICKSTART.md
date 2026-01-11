# 🚀 QUICK START GUIDE

## ⚡ Mulai dalam 3 Menit

### 1️⃣ Navigate ke Folder
```bash
cd d:\BelajarPython\passwordTools
```

### 2️⃣ Run Aplikasi (Pilih Salah Satu)

**Option A: CLI Version (Recommended)**
```bash
python cli.py
```
✓ Langsung bisa dijalankan (tanpa install extra)
✓ Full fitur berfungsi
✓ Menu-based interface

**Option B: Web UI Version (Streamlit)**
```bash
pip install streamlit
streamlit run app.py
```
✓ Beautiful web interface
✓ Tab-based navigation
✓ Browser-based

### 3️⃣ Test Semua Fitur
```bash
python test_app.py
```
✓ Verifikasi semua module bekerja
✓ Integration tests

---

## 📋 Menu Opsi (CLI Version)

```
1. Generate Password       → Create new random password
2. Check Strength          → Analyze password kekuatan
3. View History            → Lihat file yang sudah di-export
4. Info                    → About aplikasi & tips
5. Exit                    → Keluar
```

---

## 💡 Contoh Penggunaan

### Generate Strong Password
1. Select: `1. Generate Password`
2. Input: Panjang (misal: `16`)
3. Rules: Pilih semua (default)
4. Result: `o"p%rvFN0IoAzm5!` (Very Strong 🔵)
5. Export: Simpan ke file? Yes
6. File saved: `output/password_20260111_103958.txt`

### Check Weak Password
1. Select: `2. Check Strength`
2. Input: `abc123`
3. Result: Weak 🔴 (Score: 35/100)
4. Suggestions:
   - Add uppercase letters
   - Add more characters
   - Add symbols

---

## 📁 File Locations

| File | Purpose |
|------|---------|
| `src/password_generator.py` | Password generation logic |
| `src/strength_checker.py` | Strength analysis dengan regex |
| `src/input_validator.py` | Input validation & retry |
| `src/file_export.py` | File export functionality |
| `output/` | Folder untuk hasil export |
| `cli.py` | Command line interface |
| `app.py` | Streamlit web UI |

---

## 🔐 Security Tips

1. **Use 12+ characters**
2. **Mix: Huruf + Angka + Simbol**
3. **Avoid: Names, Dates, Keyboard patterns**
4. **Different password per account**
5. **Use password manager to store**

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| "command not found: python" | Use `python3` or check PATH |
| Module not found | Run from project root directory |
| Streamlit not found | `pip install streamlit` |
| File not saved | Check `output/` folder exists |

---

## 📊 Strength Categories

| Category | Score | Meaning |
|----------|-------|---------|
| 🔴 Weak | < 40 | Not safe |
| 🟡 Medium | 40-60 | OK for daily use |
| 🟢 Strong | 60-80 | Good for important accounts |
| 🔵 Very Strong | 80+ | Excellent (recommended) |

---

## 📚 Files to Read

- **README.md** - Full documentation
- **SETUP_GUIDE.md** - Detailed setup instructions
- **PROJECT_SUMMARY.md** - Complete project overview

---

## ✨ Features Implemented

✅ Generate random password dengan custom rules
✅ Strength checking dengan regex patterns
✅ Input validation dengan retry logic
✅ File export ke .txt dengan timestamp
✅ CLI interface yang interactive
✅ Streamlit web UI (optional)
✅ Integration tests
✅ Comprehensive documentation

---

**Happy Password Generating! 🔐**

---

*Last updated: January 11, 2026*
*Status: ✅ Production Ready v1.0*
