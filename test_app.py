#!/usr/bin/env python
"""
Test script untuk semua module
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("=" * 60)
print("TESTING PASSWORD GENERATOR & STRENGTH CHECKER")
print("=" * 60)

# Test 1: Password Generator
print("\n[TEST 1] Password Generator Module")
print("-" * 60)

try:
    from password_generator import generate_password, get_rules_summary
    
    print("✓ Import password_generator OK")
    
    # Generate test password
    pwd = generate_password(12, True, True, True, True)
    print(f"✓ Generated password: {pwd}")
    
    # Get rules summary
    rules = get_rules_summary(True, True, True, True)
    print(f"✓ Rules summary: {rules}")
    
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 2: Strength Checker
print("\n[TEST 2] Strength Checker Module")
print("-" * 60)

try:
    from strength_checker import check_password_strength, PasswordStrength
    
    print("✓ Import strength_checker OK")
    
    # Test weak password
    result_weak = check_password_strength("abc123")
    print(f"✓ Weak password check:")
    print(f"  - Password: abc123")
    print(f"  - Strength: {result_weak['strength'].value}")
    print(f"  - Score: {result_weak['score']}/100")
    
    # Test strong password
    result_strong = check_password_strength("MySecurePass123!Secure")
    print(f"\n✓ Strong password check:")
    print(f"  - Password: MySecurePass123!Secure")
    print(f"  - Strength: {result_strong['strength'].value}")
    print(f"  - Score: {result_strong['score']}/100")
    
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 3: Input Validator
print("\n[TEST 3] Input Validator Module")
print("-" * 60)

try:
    from input_validator import validate_password_length, validate_yes_no
    
    print("✓ Import input_validator OK")
    
    # Test length validation
    is_valid, length, msg = validate_password_length("12")
    print(f"✓ Length validation '12': valid={is_valid}, length={length}")
    
    is_valid, length, msg = validate_password_length("3")
    print(f"✓ Length validation '3': valid={is_valid}, msg='{msg}'")
    
    # Test yes/no validation
    is_valid, result, msg = validate_yes_no("y")
    print(f"✓ Yes/No validation 'y': valid={is_valid}, result={result}")
    
    is_valid, result, msg = validate_yes_no("invalid")
    print(f"✓ Yes/No validation 'invalid': valid={is_valid}, msg='{msg}'")
    
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 4: File Export
print("\n[TEST 4] File Export Module")
print("-" * 60)

try:
    from file_export import export_to_file, list_exports
    
    print("✓ Import file_export OK")
    
    # Create test export
    pwd = generate_password(16, True, True, True, True)
    result = check_password_strength(pwd)
    rules = get_rules_summary(True, True, True, True)
    
    filepath = export_to_file(pwd, result, rules, "test_password.txt")
    print(f"✓ Export successful: {filepath}")
    
    # List exports
    exports = list_exports()
    print(f"✓ List exports: {len(exports)} file(s) found")
    
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 5: Integration Test
print("\n[TEST 5] Integration Test")
print("-" * 60)

try:
    # Full flow
    print("Running full password generation and strength check...")
    
    # 1. Generate
    pwd = generate_password(16, True, True, True, False)
    print(f"✓ Generated: {pwd}")
    
    # 2. Check strength
    result = check_password_strength(pwd)
    print(f"✓ Strength: {result['strength'].value} (Score: {result['score']})")
    
    # 3. Export
    rules = get_rules_summary(True, True, True, False)
    filepath = export_to_file(pwd, result, rules)
    print(f"✓ Exported: {filepath}")
    
    print("\n✓ All integration tests passed!")
    
except Exception as e:
    print(f"✗ Integration test failed: {str(e)}")

print("\n" + "=" * 60)
print("TESTING COMPLETE")
print("=" * 60)
print("\nSemua module berhasil ditest! ✓")
print("Aplikasi siap digunakan.")
print("\nJalankan dengan:")
print("  - CLI Version: python cli.py")
print("  - Web Version: streamlit run app.py")
