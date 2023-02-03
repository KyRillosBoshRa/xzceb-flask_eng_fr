import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=auth
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    translation_response = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation_response['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    translation_response = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation_response['translations'][0]['translation']
    return english_text
