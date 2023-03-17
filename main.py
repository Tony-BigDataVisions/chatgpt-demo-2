# Libraries
import openai, streamlit as st, random, warnings, gc as gc

gc.enable()
warnings.filterwarnings('ignore')

# Necessary
openai.api_key = st.secrets.api_key

# Wrapper function for interacting with OpenAI API
def ask_chatgpt(question, model="text-davinci-002"):
    completions = openai.Completion.create(engine=model, prompt=question, max_tokens=1024, temperature=0.7)
    message = completions.choices[0].text
    return message

# # Streamlit Settings
st.set_page_config(layout="wide", page_icon="🧠", page_title="Conversing with AI - Powered by ChatGPT")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Streamlit titles
st.sidebar.title("Click a checkbox to generate questions to ask ChatGPT")

prompt = None
selections = ['Pick a topic', 'Related to major news', 'Related to major US Sports', 'A random prompt', 'Enter in your own question']
idx = selections.index('Pick a topic')

try:
    selection = st.sidebar.selectbox('Generate topics:', selections, index=idx, key='selections')

    if st.session_state['selections']=='Enter in your own question':
        prompt = st.text_area("Enter in your prompt for ChatGPT to respond to", key='enter_prompt')

        st.write("We are going to ask chat GPT about:\n ", prompt)

    elif st.session_state['selections']=='Related to major news':
        resp = ask_chatgpt('Generate 5 topics related to major news, but reply with it in a python string using "-" as a separator')
        temp = resp.split('-')
        prompt = temp[random.randint(1, len(temp)-1)]

        st.write("We are going to ask chat GPT about:\n ", prompt)

    elif st.session_state['selections']=='Related to major US Sports':
        resp = ask_chatgpt('Generate 5 topics related to major US Sports, but reply with it in a python string using "-" as a separator')
        temp = resp.split('-')
        prompt = temp[random.randint(1, len(temp)-1)]    

        st.write("We are going to ask chat GPT about:\n ", prompt)

    elif st.session_state['selections']=='A random prompt':
        resp = ask_chatgpt('Generate 5 random topics to ask you about, but reply with it in a python string using "-" as a separator')
        temp = resp.split('-')
        prompt = temp[random.randint(1, len(temp)-1)]

        st.write("We are going to ask chat GPT about:\n ", prompt)
    else:
        pass        
    
    if st.sidebar.button('Ask ChatGPT!'):
        st.text(ask_chatgpt(prompt))
except Exception as E:
    st.write("ChatGPT is feeling buggy; please try again after refreshing the page!")
