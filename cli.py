"""
CLI Version - Password Generator & Strength Checker
Versi command line untuk testing tanpa Streamlit
"""

import sys
import os

# Add src folder ke path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from password_generator import generate_password, get_rules_summary
from strength_checker import check_password_strength, get_strength_emoji, get_strength_color
from input_validator import validate_password_length, get_user_input_with_retry, validate_yes_no
from file_export import export_to_file, list_exports, read_export_file

# ANSI Colors
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"


def print_header(text):
    """Print header dengan styling"""
    print(f"\n{BOLD}{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}{CYAN}{text.center(60)}{RESET}")
    print(f"{BOLD}{CYAN}{'='*60}{RESET}\n")


def print_section(text):
    """Print section dengan styling"""
    print(f"\n{BOLD}{YELLOW}▶ {text}{RESET}")
    print(f"{YELLOW}{'-'*60}{RESET}")


def print_success(text):
    """Print success message"""
    print(f"{GREEN}✓ {text}{RESET}")


def print_error(text):
    """Print error message"""
    print(f"{RED}✗ {text}{RESET}")


def print_info(text):
    """Print info message"""
    print(f"{BLUE}ℹ {text}{RESET}")


def menu_generate_password():
    """Menu untuk generate password"""
    print_header("🎲 PASSWORD GENERATOR")
    
    # Input panjang
    print_section("1. Tentukan Panjang Password")
    
    def validator(input_str):
        return validate_password_length(input_str, min_length=4, max_length=128)
    
    length_str = get_user_input_with_retry(
        f"{CYAN}Masukkan panjang password (4-128): {RESET}",
        validator_func=validator,
        max_retries=3
    )
    length = int(length_str)
    
    # Select rules
    print_section("2. Tentukan Rules")
    print_info("Pilih tipe karakter yang akan digunakan:")
    
    use_uppercase = get_user_input_with_retry(
        f"{CYAN}Gunakan huruf besar (A-Z)? [y/n]: {RESET}",
        validator_func=lambda x: validate_yes_no(x),
        max_retries=2
    )
    use_uppercase = use_uppercase == "True"
    
    use_lowercase = get_user_input_with_retry(
        f"{CYAN}Gunakan huruf kecil (a-z)? [y/n]: {RESET}",
        validator_func=lambda x: validate_yes_no(x),
        max_retries=2
    )
    use_lowercase = use_lowercase == "True"
    
    use_numbers = get_user_input_with_retry(
        f"{CYAN}Gunakan angka (0-9)? [y/n]: {RESET}",
        validator_func=lambda x: validate_yes_no(x),
        max_retries=2
    )
    use_numbers = use_numbers == "True"
    
    use_symbols = get_user_input_with_retry(
        f"{CYAN}Gunakan simbol (!@#$%^&*)? [y/n]: {RESET}",
        validator_func=lambda x: validate_yes_no(x),
        max_retries=2
    )
    use_symbols = use_symbols == "True"
    
    # Generate password
    print_section("3. Generate Password")
    
    try:
        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_numbers=use_numbers,
            use_symbols=use_symbols
        )
        
        rules = get_rules_summary(use_uppercase, use_lowercase, use_numbers, use_symbols)
        
        # Display result
        print_section("4. Hasil")
        print(f"\n{BOLD}Password:{RESET}")
        print(f"{BOLD}{GREEN}{'█' * 60}{RESET}")
        print(f"{BOLD}{GREEN}{password}{RESET}")
        print(f"{BOLD}{GREEN}{'█' * 60}{RESET}\n")
        
        print(f"{BOLD}Rules yang digunakan:{RESET}")
        print(f"{BLUE}✓ {rules}{RESET}\n")
        
        print(f"{BOLD}Informasi:{RESET}")
        print(f"  Panjang: {len(password)} karakter\n")
        
        # Check strength
        print_section("5. Analisis Kekuatan")
        strength_result = check_password_strength(password)
        display_strength(password, strength_result)
        
        # Export option
        print_section("6. Opsi Lanjutan")
        export_choice = get_user_input_with_retry(
            f"{CYAN}Simpan hasil ke file? [y/n]: {RESET}",
            validator_func=lambda x: validate_yes_no(x),
            max_retries=2
        )
        
        if export_choice == "True":
            try:
                filepath = export_to_file(password, strength_result, rules)
                print_success(f"File berhasil disimpan: {filepath}\n")
            except IOError as e:
                print_error(f"Gagal menyimpan file: {str(e)}\n")
        
        # Retry option
        retry = get_user_input_with_retry(
            f"{CYAN}Generate password lagi? [y/n]: {RESET}",
            validator_func=lambda x: validate_yes_no(x),
            max_retries=2
        )
        
        if retry == "True":
            menu_generate_password()
    
    except ValueError as e:
        print_error(str(e))


def menu_check_strength():
    """Menu untuk check password strength"""
    print_header("📊 PASSWORD STRENGTH CHECKER")
    
    password = input(f"{CYAN}Masukkan password untuk dicek: {RESET}").strip()
    
    if not password:
        print_error("Password tidak boleh kosong!")
        return
    
    print_section("Analisis Kekuatan")
    result = check_password_strength(password)
    display_strength(password, result)
    
    # Export option
    print_section("Opsi")
    export_choice = get_user_input_with_retry(
        f"{CYAN}Simpan hasil ke file? [y/n]: {RESET}",
        validator_func=lambda x: validate_yes_no(x),
        max_retries=2
    )
    
    if export_choice == "True":
        try:
            filepath = export_to_file(password, result, "Password dari Strength Checker")
            print_success(f"File berhasil disimpan: {filepath}\n")
        except IOError as e:
            print_error(f"Gagal menyimpan file: {str(e)}\n")


def menu_view_exports():
    """Menu untuk lihat file exports"""
    print_header("📁 HISTORY EXPORTS")
    
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    exports = list_exports(output_dir)
    
    if not exports:
        print_info("Belum ada file export.\n")
        return
    
    print(f"{BLUE}Total file: {len(exports)}\n{RESET}")
    
    for i, filename in enumerate(exports, 1):
        print(f"{YELLOW}{i}. {filename}{RESET}")
    
    print()
    
    try:
        choice = input(f"{CYAN}Pilih file untuk dibaca (nomor): {RESET}").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(exports):
            selected = exports[int(choice) - 1]
            filepath = os.path.join(output_dir, selected)
            content = read_export_file(filepath)
            
            print_section("Isi File")
            print(content)
        else:
            print_error("Pilihan tidak valid!")
    
    except Exception as e:
        print_error(f"Error: {str(e)}")


def display_strength(password, result):
    """Display strength analysis"""
    strength = result['strength']
    score = result['score']
    emoji = get_strength_emoji(strength)
    color = get_strength_color(strength)
    
    print(f"\n{color}{BOLD}Level Kekuatan: {emoji} {strength.value}{RESET}")
    print(f"{color}Skor: {score}/100{RESET}")
    print(f"{CYAN}Panjang: {len(password)} karakter{RESET}\n")
    
    # Progress bar
    progress = int((score / 100) * 30)
    bar = "█" * progress + "░" * (30 - progress)
    print(f"{CYAN}Progress: [{bar}] {score}%{RESET}\n")
    
    # Details
    print(f"{BOLD}Kriteria yang Terpenuhi:{RESET}")
    details = result['details']
    
    criteria = [
        ("Minimal 8 karakter", details['panjang']),
        ("Minimal 12 karakter", details['panjang_extra']),
        ("Huruf Besar (A-Z)", details['huruf_besar']),
        ("Huruf Kecil (a-z)", details['huruf_kecil']),
        ("Angka (0-9)", details['angka']),
        ("Simbol (!@#$%^&*)", details['simbol']),
    ]
    
    for criterion, status in criteria:
        symbol = f"{GREEN}✓{RESET}" if status else f"{RED}✗{RESET}"
        print(f"  {symbol} {criterion}")
    
    # Recommendations
    print()
    if result['feedback']:
        print(f"{BOLD}Saran Perbaikan:{RESET}")
        for i, rec in enumerate(result['feedback'], 1):
            print(f"  {i}. {rec}")
    else:
        print(f"{GREEN}{BOLD}🎉 Password Anda sudah sangat kuat!{RESET}")
    
    print()


def main_menu():
    """Main menu"""
    while True:
        print_header("🔐 PASSWORD GENERATOR & STRENGTH CHECKER")
        
        print(f"{BOLD}Pilih Menu:{RESET}")
        print(f"{CYAN}1. 🎲 Generate Password Baru{RESET}")
        print(f"{CYAN}2. 📊 Check Password Strength{RESET}")
        print(f"{CYAN}3. 📁 Lihat History Export{RESET}")
        print(f"{CYAN}4. ℹ️  Informasi{RESET}")
        print(f"{CYAN}5. ❌ Keluar{RESET}")
        print()
        
        choice = input(f"{CYAN}Masukkan pilihan (1-5): {RESET}").strip()
        
        if choice == "1":
            menu_generate_password()
        elif choice == "2":
            menu_check_strength()
        elif choice == "3":
            menu_view_exports()
        elif choice == "4":
            show_info()
        elif choice == "5":
            print_success("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print_error("Pilihan tidak valid!\n")


def show_info():
    """Show informasi aplikasi"""
    print_header("ℹ️  INFORMASI APLIKASI")
    
    info_text = f"""
{BOLD}Password Generator & Strength Checker{RESET}

{BOLD}Fitur Utama:{RESET}
  ✓ Generate password random dengan rules custom
  ✓ Analisis kekuatan password dengan scoring
  ✓ Regex pattern matching untuk validasi
  ✓ Export hasil ke file .txt dengan timestamp
  ✓ Retry logic untuk input validation
  ✓ Modularisasi fungsi yang clean

{BOLD}Kategori Strength:{RESET}
  🔴 Weak (< 40)       - Tidak aman
  🟡 Medium (40-60)    - Cukup aman
  🟢 Strong (60-80)    - Baik untuk akun penting
  🔵 Very Strong (80+) - Sangat aman (recommended)

{BOLD}Best Practices:{RESET}
  1. Gunakan minimal 12 karakter
  2. Campurkan semua jenis karakter (huruf+angka+simbol)
  3. Hindari pattern (tanggal, nama, urutan keyboard)
  4. Gunakan password berbeda untuk setiap akun
  5. Simpan password di password manager

{BOLD}Teknologi:{RESET}
  • Python 3.8+
  • Regular Expressions (Regex)
  • Random Module
  • File I/O

"""
    
    print(info_text)
    input(f"{CYAN}Tekan Enter untuk kembali...{RESET}")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Program dihentikan oleh user.{RESET}")
        sys.exit(0)
    except Exception as e:
        print_error(f"Terjadi error: {str(e)}")
        sys.exit(1)
