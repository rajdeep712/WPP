import re

def tokenize(text):
    patterns = {
        'url': r'https?://[^\s]+',
        'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        'date': r'\d{1,2}/\d{1,2}/\d{2,4}|\d{1,2}-\d{1,2}-\d{2,4}',
        'number': r'\d{1,3}(,\d{3})*(\.\d+)?|\d+/\d+',
        'username': r'@[a-zA-Z0-9_]+',
        'punctuation': r'[।,!?;:"\'()\-]',
        'hindi_word': r'[\u0900-\u097F]+'
    }

    combined_pattern = '|'.join(f'(?P<{key}>{pattern})' for key, pattern in patterns.items())

    tokens = []
    for match in re.finditer(combined_pattern, text):
        for key, value in match.groupdict().items():
            if value:
                tokens.append((key, value))
                break

    return tokens

text = "नमस्ते! मेरा नाम राज है। मेरी ईमेल है raj@example.com और मेरी वेबसाइट है https://example.com। आज की तारीख 11/03/2025 है। मैंने 3,22,243 रुपये खर्च किए। मेरा ट्विटर हैंडल @raj_user है।"

tokens = tokenize(text)
for token_type, token in tokens:
    print(f'{token_type}: {token}')