"""
Input Validation Module
Untuk validasi dan retry logic
"""

import re


def validate_password_length(length_input: str, min_length: int = 4, 
                            max_length: int = 128) -> tuple[bool, int, str]:
    """
    Validasi input panjang password dari user.
    
    Args:
        length_input: Input string dari user
        min_length: Panjang minimal
        max_length: Panjang maksimal
    
    Returns:
        Tuple (is_valid, length, error_message)
    """
    
    # Cek apakah input adalah angka
    if not re.match(r'^\d+$', str(length_input).strip()):
        return False, 0, "Input harus berupa angka"
    
    length = int(length_input)
    
    # Cek range
    if length < min_length:
        return False, 0, f"Panjang minimal {min_length} karakter"
    
    if length > max_length:
        return False, 0, f"Panjang maksimal {max_length} karakter"
    
    return True, length, ""


def get_user_input_with_retry(prompt: str, validator_func=None, max_retries: int = 3) -> str:
    """
    Dapatkan input dari user dengan retry logic.
    
    Args:
        prompt: Pesan yang ditampilkan
        validator_func: Function untuk validasi (return tuple (is_valid, value, error_msg))
        max_retries: Jumlah maksimal retry
    
    Returns:
        Input yang valid dari user
    
    Raises:
        ValueError: Jika semua retry gagal
    """
    
    for attempt in range(max_retries):
        try:
            user_input = input(prompt).strip()
            
            if validator_func is None:
                return user_input
            
            # Gunakan validator
            is_valid, value, error_msg = validator_func(user_input)
            
            if is_valid:
                return str(value)
            else:
                remaining = max_retries - attempt - 1
                if remaining > 0:
                    print(f"❌ Error: {error_msg}")
                    print(f"📝 Coba lagi ({remaining} kesempatan tersisa)\n")
                else:
                    raise ValueError(f"Input tidak valid: {error_msg}")
        
        except ValueError as e:
            raise ValueError(str(e))
        except KeyboardInterrupt:
            raise ValueError("Input dibatalkan oleh user")
    
    raise ValueError("Gagal mendapatkan input setelah beberapa percobaan")


def validate_yes_no(input_str: str) -> tuple[bool, bool, str]:
    """
    Validasi input yes/no
    
    Returns:
        Tuple (is_valid, result, error_message)
        result: True untuk yes, False untuk no
    """
    
    input_lower = input_str.strip().lower()
    
    if input_lower in ['y', 'yes', 'ya', '1']:
        return True, True, ""
    elif input_lower in ['n', 'no', 'tidak', '0']:
        return True, False, ""
    else:
        return False, False, "Input harus 'y' atau 'n'"
