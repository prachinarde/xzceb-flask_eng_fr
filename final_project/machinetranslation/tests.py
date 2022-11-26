"""import all the modules"""
import os
from ibm_watson import LanguageTranslatorV3
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']

url = os.environ['url']
def english_to_french(english_text):
    """will translate"""
    url.set_service_url(url)
    french_text = url.translate(text = english_text, model_id = 'en-fr').get_result()
    return french_text
def french_to_english(french_text):
    """will translate"""
    url.set_service_url(url)
    english_text = url.translate(text = french_text, model_id ='fr-en').get_result()
    return english_text
    print(english_to_french("Hello"), french_to_english("Bonjour"))
