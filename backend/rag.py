import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def retrieve_agriculture_data(query: str):
    """
    Simulated external agriculture API response
    Replace with real APIs later
    """
    return f"""
    Crop Disease Information:
    Disease: Leaf Blight
    Affected Crops: Rice, Wheat
    Symptoms: Yellowing of leaves, brown spots
    Causes: Fungal infection
    Treatment: Apply recommended fungicide
    Prevention: Proper irrigation, crop rotation
    """

def generate_answer(query: str):
    context = retrieve_agriculture_data(query)

    prompt = f"""
    You are an agriculture expert.

    Use ONLY the following context to answer.

    Context:
    {context}

    Question:
    {query}

    Provide clear, practical advice for farmers.
    """

    response = client.chat.completions.create(
        
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
