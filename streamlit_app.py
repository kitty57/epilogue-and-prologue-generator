import streamlit as st
import google.generativeai as genai

# Configure GenerativeAI
genai.configure(api_key="AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY")
model = genai.GenerativeModel(model_name="gemini-pro")

# Define function to generate prologue and epilogue
def generate_epipro(name, genre, protagonist):
    prompt = f'''
    "As an experienced and witty writer, write a prologue (it should be something like a backstory of some kind of incident happening to the main characters, explain the incident as a scene in a character's POV, before they actually meet, add descriptions, dialogues, and other such elements, the characters shouldn't meet yet, it should just show a backstory of how their real lives are) and an epilogue (this should be some sort of incident with dialogues and such elements after the main story is over) of 1500 words each that seems as though written by a human, for a novel named {name}, of the genre/genres {genre}, with the protagonists {protagonist}. Add a lot of funny and witty dialogues and remarks whenever possible. Both of that should be from a character's POV only, that is the number 1 rule!!
    The output should be of the following form :
    Novel name -- and a catchphrase
    Prologue:
    ### the prologue goes here!
    -----
    Epilogue:
    ### the epilogue goes here!
    '''
    response = model.generate_content([prompt])
    return response.text

# Streamlit UI
st.title("Novel Prologue & Epilogue Generator")

name = st.text_input("Enter Novel Name:")
genre = st.text_input("Enter Genre:")
protagonist = st.text_area("Enter Protagonists (Character Names and Descriptions):")

if st.button("Generate Prologue & Epilogue"):
    if name and genre and protagonist:
        result = generate_epipro(name, genre, protagonist)
        r1,r2=result.split('Epilogue')
        st.info(r1)
        st.markdown('Epilogue:')
        st.info(r2)
    else:
        st.error("Please fill in all fields.")

