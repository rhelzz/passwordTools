"""
File Export Module
Untuk export hasil password dan informasi ke file .txt
"""

import os
from datetime import datetime


def export_to_file(password: str, strength_info: dict, rules_summary: str, 
                   filename: str = None) -> str:
    """
    Export password dan hasil checking ke file .txt
    
    Args:
        password: Password yang di-generate
        strength_info: Dictionary hasil strength checker
        rules_summary: Ringkasan rules yang digunakan
        filename: Nama file (opsional, auto-generate jika tidak diberikan)
    
    Returns:
        Path lengkap file yang telah dibuat
    
    Raises:
        IOError: Jika ada masalah saat menulis file
    """
    
    # Tentukan directory output
    output_dir = os.path.join(os.path.dirname(__file__), "..", "output")
    
    # Create directory jika belum ada
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename jika tidak diberikan
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"password_{timestamp}.txt"
    
    # Full path
    filepath = os.path.join(output_dir, filename)
    
    # Prepare content
    content = f"""═══════════════════════════════════════════════════════════
               PASSWORD GENERATOR RESULT
═══════════════════════════════════════════════════════════

Generated At: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

PASSWORD
────────────────────────────────────────────────────────────
{password}

RULES USED
────────────────────────────────────────────────────────────
{rules_summary}

STRENGTH ANALYSIS
────────────────────────────────────────────────────────────
Level: {strength_info['strength'].value}
Score: {strength_info['score']}/100

Criteria Met:
  ✓ Panjang Password (8+ karakter): {'YA' if strength_info['details']['panjang'] else 'TIDAK'}
  ✓ Panjang Extra (12+ karakter):   {'YA' if strength_info['details']['panjang_extra'] else 'TIDAK'}
  ✓ Huruf Besar (A-Z):              {'YA' if strength_info['details']['huruf_besar'] else 'TIDAK'}
  ✓ Huruf Kecil (a-z):              {'YA' if strength_info['details']['huruf_kecil'] else 'TIDAK'}
  ✓ Angka (0-9):                    {'YA' if strength_info['details']['angka'] else 'TIDAK'}
  ✓ Simbol (!@#$%^&*):              {'YA' if strength_info['details']['simbol'] else 'TIDAK'}

Recommendations:
────────────────────────────────────────────────────────────
"""
    
    if strength_info['feedback']:
        for i, rec in enumerate(strength_info['feedback'], 1):
            content += f"{i}. {rec}\n"
    else:
        content += "Tidak ada rekomendasi. Password sudah sangat kuat!\n"
    
    content += "\n═══════════════════════════════════════════════════════════\n"
    
    # Write to file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filepath
    except IOError as e:
        raise IOError(f"Gagal menulis file: {str(e)}")


def read_export_file(filepath: str) -> str:
    """
    Baca isi file export
    
    Args:
        filepath: Path ke file yang akan dibaca
    
    Returns:
        Isi file sebagai string
    
    Raises:
        FileNotFoundError: Jika file tidak ditemukan
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File tidak ditemukan: {filepath}")


def list_exports(output_dir: str = None) -> list:
    """
    List semua file export yang sudah dibuat
    
    Returns:
        List nama file dalam direktori output
    """
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(__file__), "..", "output")
    
    if not os.path.exists(output_dir):
        return []
    
    return [f for f in os.listdir(output_dir) if f.endswith('.txt')]
