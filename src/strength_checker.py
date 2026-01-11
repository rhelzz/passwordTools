"""
Password Strength Checker Module
Mengecek kekuatan password menggunakan regex dan kategori
"""

import re
from enum import Enum


class PasswordStrength(Enum):
    """Enum untuk kategori kekuatan password"""
    WEAK = "Lemah"
    MEDIUM = "Sedang"
    STRONG = "Kuat"
    VERY_STRONG = "Sangat Kuat"


def check_password_strength(password: str) -> dict:
    """
    Cek kekuatan password menggunakan regex dan scoring.
    
    Args:
        password: Password yang akan dicek
    
    Returns:
        Dictionary berisi:
        - strength: Enum PasswordStrength
        - score: Skor 0-100
        - feedback: List saran untuk improve password
        - details: Dictionary detail kriteria yang terpenuhi
    """
    
    score = 0
    feedback = []
    details = {
        "panjang": False,
        "huruf_besar": False,
        "huruf_kecil": False,
        "angka": False,
        "simbol": False,
        "panjang_extra": False,
    }
    
    # Regex patterns
    pattern_uppercase = r'[A-Z]'
    pattern_lowercase = r'[a-z]'
    pattern_numbers = r'[0-9]'
    pattern_symbols = r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]'
    
    # Cek panjang dasar (minimal 8)
    if len(password) >= 8:
        score += 20
        details["panjang"] = True
    else:
        feedback.append(f"Password terlalu pendek (minimal 8 karakter, saat ini: {len(password)})")
    
    # Cek panjang extra (12+)
    if len(password) >= 12:
        score += 15
        details["panjang_extra"] = True
    
    # Cek huruf besar
    if re.search(pattern_uppercase, password):
        score += 15
        details["huruf_besar"] = True
    else:
        feedback.append("Tambahkan huruf besar (A-Z)")
    
    # Cek huruf kecil
    if re.search(pattern_lowercase, password):
        score += 15
        details["huruf_kecil"] = True
    else:
        feedback.append("Tambahkan huruf kecil (a-z)")
    
    # Cek angka
    if re.search(pattern_numbers, password):
        score += 20
        details["angka"] = True
    else:
        feedback.append("Tambahkan angka (0-9)")
    
    # Cek simbol
    if re.search(pattern_symbols, password):
        score += 15
        details["simbol"] = True
    else:
        feedback.append("Tambahkan karakter spesial (!@#$%^&*)")
    
    # Tentukan kategori berdasarkan score
    if score >= 80:
        strength = PasswordStrength.VERY_STRONG
    elif score >= 60:
        strength = PasswordStrength.STRONG
    elif score >= 40:
        strength = PasswordStrength.MEDIUM
    else:
        strength = PasswordStrength.WEAK
    
    return {
        "strength": strength,
        "score": min(score, 100),  # Cap score di 100
        "feedback": feedback,
        "details": details
    }


def get_strength_color(strength: PasswordStrength) -> str:
    """
    Dapatkan warna untuk setiap level strength (untuk CLI)
    
    Returns:
        String ANSI color code
    """
    colors = {
        PasswordStrength.WEAK: "\033[91m",        # Red
        PasswordStrength.MEDIUM: "\033[93m",      # Yellow
        PasswordStrength.STRONG: "\033[92m",      # Green
        PasswordStrength.VERY_STRONG: "\033[94m", # Blue
    }
    return colors.get(strength, "\033[0m")


def get_strength_emoji(strength: PasswordStrength) -> str:
    """
    Dapatkan emoji untuk setiap level strength
    
    Returns:
        String emoji
    """
    emojis = {
        PasswordStrength.WEAK: "🔴",
        PasswordStrength.MEDIUM: "🟡",
        PasswordStrength.STRONG: "🟢",
        PasswordStrength.VERY_STRONG: "🔵",
    }
    return emojis.get(strength, "❓")
