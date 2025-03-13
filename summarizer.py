from auth import Authentication

def summarize_and_translate(article):
    """
    Summarizes and translates the article using OpenAI's GPT-4 model.
    Uses the Authentication class for OpenAI client management.
    """
    # Initialize authentication
    auth = Authentication()
    openai_client = auth.get_openai_client()
    
    if not openai_client:
        print("OpenAI authentication failed")
        return None

    prompt = f"""
    Haberi sadece Türkçe olarak iki cümlede özetle. 
    İlk cümlede haberin en önemli detayını açıkla. 
    İkinci cümlede takipçilere yönelik bir cümle yaz. Haberin içeriğine göre buna sahip 
    olmak istermiydin, sen ne düşünüyorsun, burda kiminle sürmek isterdin gibi cümle ile bitir. 
    
    Haber başlığı: {article['title']}
    """
    
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",  # Fixed typo in model name from "gpt-4o" to "gpt-4"
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in summarizing article: {e}")
        return None

    
