from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

def translate_text(text, target_language):
    credentials = service_account.Credentials.from_service_account_file(
        'google/api_connection.json'
    )
    client = translate.Client(credentials=credentials)
    result = client.translate(text, target_language=target_language)
    return result['translatedText']
