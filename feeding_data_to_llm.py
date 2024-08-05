from dotenv import load_dotenv
import google.generativeai as genai
import logging
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
logging.info('Google Gemini Pro api is configured')

INPUT_PROMPT = '''Your sole purpose is to generate fake news headline. You can generate a proper news hewadline using the context or description about the news and the real headline of that news.
you have to done it properly cause In this case after giving the fake headline we will both compare with the real one. So generate it properly. 
I will give you the description and real headline in a dictionary format of the article then you should generate a fake news headline using that descriptions and the real news headline'''



def get_gemini_response(input,prompt):
    # we are using the gemini 1.5 pro model cause it's free
    model=genai.GenerativeModel('gemini-1.0-pro')
    try:
        response=model.generate_content([input,prompt])
        return response.text
    except:
        logging.info('There is an error with the response')
        return None
