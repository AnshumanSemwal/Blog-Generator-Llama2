import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


##Function : gets response from Llama 2 model

def getLLamaresponse(input_text,no_words,blog_style):

    # About Model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                    model_type='llama',
                    config={'max_new_tokens':256,
                            'temperature':0.01})

    # Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
             """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'], template=template)


    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Blog Generator",
                    page_icon='👨‍🎓',
                    layout='centered',
                    initial_sidebar_state='collapsed')



c1, c2 = st.columns([0.25, 0.6])
with c2:
    st.header("Blog Generator 👨‍🎓")

st.subheader("Quirky? In-depth? Challenging? Specific? I can do it all!!!")


co1, co2, co3 = st.columns([0.2, 0.6, 0.2])

co2.image("Media/img1.jpg")

input_text=st.text_input("Enter a topic and watch us curate a blog for you")


col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No. of Words')

with col2:
    blog_style=st.selectbox('Writing the blog for',('Researchers', 'DataScientists', 'Analyst', 'Writer', 'Content Creator','Critic'), index=0)

submit= st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))