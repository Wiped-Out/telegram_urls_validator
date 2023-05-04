import pytest

from telegram_urls_validator import validate_url


@pytest.mark.parametrize(
    ('input_url', 'expected_url'),
    (
            ('@Durov', 'https://t.me/Durov'),

            ('t.me/@Durov', 'https://t.me/Durov'),
            ('http://t.me/@Durov', 'https://t.me/Durov'),
            ('https://t.me/@Durov', 'https://t.me/Durov'),

            ('telegram.me/@Durov', 'https://t.me/Durov'),
            ('http://telegram.me/@Durov', 'https://t.me/Durov'),
            ('https://telegram.me/@Durov', 'https://t.me/Durov'),

            ('t.me/Durov', 'https://t.me/Durov'),
            ('http://t.me/Durov', 'https://t.me/Durov'),
            ('https://t.me/Durov', 'https://t.me/Durov'),

            ('telegram.me/Durov', 'https://t.me/Durov'),
            ('http://telegram.me/Durov', 'https://t.me/Durov'),
            ('https://telegram.me/Durov', 'https://t.me/Durov'),

            ('https://t.me/Durov/', 'https://t.me/Durov'),
    )
)
def test_correct_urls(input_url: str, expected_url: str):
    assert validate_url(input_url) == expected_url
