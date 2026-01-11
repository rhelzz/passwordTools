"""
Password Generator Module
Menghasilkan password random berdasarkan rules yang ditentukan
"""

import random
import string


def generate_password(length: int, use_uppercase: bool = True, 
                     use_lowercase: bool = True, use_numbers: bool = True, 
                     use_symbols: bool = True) -> str:
    """
    Generate password random dengan kriteria tertentu.
    
    Args:
        length: Panjang password yang ingin dibuat (minimal 4)
        use_uppercase: Include huruf besar A-Z
        use_lowercase: Include huruf kecil a-z
        use_numbers: Include angka 0-9
        use_symbols: Include simbol spesial
    
    Returns:
        String password yang ter-generate
    
    Raises:
        ValueError: Jika panjang < 4 atau tidak ada rule yang dipilih
    """
    
    # Validasi panjang password
    if length < 4:
        raise ValueError("Panjang password minimal 4 karakter")
    
    # Bangun karakter yang tersedia
    available_chars = ""
    
    if use_uppercase:
        available_chars += string.ascii_uppercase
    if use_lowercase:
        available_chars += string.ascii_lowercase
    if use_numbers:
        available_chars += string.digits
    if use_symbols:
        available_chars += string.punctuation
    
    # Validasi minimal ada 1 rule yang dipilih
    if not available_chars:
        raise ValueError("Minimal harus memilih 1 rule (huruf/angka/simbol)")
    
    # Generate password
    password = ''.join(random.choice(available_chars) for _ in range(length))
    
    return password


def get_rules_summary(use_uppercase: bool = True, 
                     use_lowercase: bool = True, 
                     use_numbers: bool = True, 
                     use_symbols: bool = True) -> str:
    """
    Dapatkan ringkasan rules yang digunakan
    
    Returns:
        String yang merangkum rules yang aktif
    """
    rules = []
    
    if use_uppercase:
        rules.append("Huruf Besar (A-Z)")
    if use_lowercase:
        rules.append("Huruf Kecil (a-z)")
    if use_numbers:
        rules.append("Angka (0-9)")
    if use_symbols:
        rules.append("Simbol (!@#$%^&*)")
    
    return ", ".join(rules)
