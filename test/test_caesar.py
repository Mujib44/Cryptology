from assertpy import assert_that
from cryptology import caesar

def test_encrypts_text_with_default_key():
    message = 'a'

    translated = caesar(message)

    assert_that(translated).is_equal_to('G')


def test_encrypts_text_with_given_key():
    message = 'a'

    translated = caesar(message, key=1)

    assert_that(translated).is_equal_to('B')


def test_decrypts_text_with_default_key():
    message = 'g'

    translated = caesar(message, mode='decrypt')

    assert_that(translated).is_equal_to('A')


