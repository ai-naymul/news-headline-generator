import streamlit as st
from feeding_data_to_llm import ResponseFromLLM
from fetch_article_headline import FetchArticleHeadlines
import ast
st.set_page_config(page_title='News Paper Headline Comparison')


dictionary_format = {
    'real_headline': 'the real headline from the article data',
    'fake_headline': 'the generated fake headline one' 
}

INPUT_PROMPT = f'''Your sole purpose is to generate fake news headline. You can generate a proper news hewadline using the context or description about the news and the real headline of that news.
you have to done it properly cause In this case after giving the fake headline we will both compare with the real one. So generate it properly. 
I will give you the description and real headline in a dictionary format of the article then you should generate a fake news headline using that descriptions and the real news headline.
Give me back the response in a dictionary, where the format will look like the following: {dictionary_format}'''

fetch_data = FetchArticleHeadlines()
all_data = fetch_data.get_article_headline()

INPUT = f'''Here are the article description in dictionary format, according to the article number there are title in the title key and there are description in the description key. Generate a fake title according the article using the real title and the description
            here is the article data: {all_data} '''



get_response = ResponseFromLLM()
data_in_dict = get_response.get_gemini_response(input=INPUT, prompt=INPUT_PROMPT)
# convert the data_in_dict string to a dictionary
response = ast.literal_eval(data_in_dict)
print(response)
print(type(response))
# print(response['real_headline'])