from openai import OpenAI
import os
from dotenv import load_dotenv
import random 

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_and_translate(article):
    prompt = f"""
    Haberi sadece Türkçe olarak iki cümlede özetle. 
    İlk cümlede haberin en önemli detayını açıkla. 
    İkinci cümlede MTB severler için neden önemli olduğunu belirt. 
    
    
    Haber başlığı: {article['title']}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
        
    )
    
    return  response.choices[0].message.content

    
