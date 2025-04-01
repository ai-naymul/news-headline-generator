from dotenv import load_dotenv
import google.generativeai as genai
import logging
import os
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
logging.info('Google Gemini Pro api is configured')

class ResponseFromLLM():
    def __init__(self) -> None:
        pass
    def get_gemini_response(self,input,prompt):
        # we are using the gemini 1.5 pro model cause it's free
        model=genai.GenerativeModel('gemini-1.0-pro')
        try:
            response=model.generate_content([input,prompt])
            return response.text
        except:
            logging.info('There is an error with the response')
            return None