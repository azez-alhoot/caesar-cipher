from caesar_cipher import __version__

from caesar_cipher.caeser_cipher import encrypt, decrypt, break_cipher
def test_version():
    assert __version__ == '0.1.0'

def test_encrypt_normal():
  assert encrypt('cat', 5) == "hfy"

def test_encrypt_bigkey20():
  assert encrypt('cat', 20) == "wun"

def test_encrypt_bigkey26():
  assert encrypt('cat', 26) == "cat"

def test_encrypt_upper():
    assert encrypt('AzIz', 2) == "cbkb"


#**********************************************

def test_decrypt__simple():
  assert decrypt('hfy', 5) == 'cat'

def test_decrypt_bigkey20():
  assert decrypt('wun', 20) == "cat"

def test_decrypt_bigkey26():
  assert decrypt('cat', 26) == "cat"

#**********************************************

def test_encrypt_chrachters_spaces():
    assert encrypt('Aziz was so hapy (:',2) == "cbkb ycu uq jcra (:"

def test_break_cipher_version_encrypt():
    text = 'It was the best of times, it was the worst of times.'
    assert break_cipher(encrypt(text,10)) == text.lower()

def test_break_cipher_version_decrypt():
    text = 'It was the best of times, it was the worst of times.'
    assert break_cipher(decrypt(text,88)) == text.lower()
