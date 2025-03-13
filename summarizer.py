from auth import Authentication

def summarize_and_translate(article):
    """
    Summarizes and translates the article using OpenAI's GPT-4 model.
    Ensures the output fits Twitter's 280-character limit.
    """
    # Initialize authentication
    auth = Authentication()
    openai_client = auth.get_openai_client()
    
    if not openai_client:
        print("OpenAI authentication failed")
        return None

    prompt = f"""
    Haberi Türkçe olarak özetle. TOPLAM KARAKTER SAYISI BOŞLUKLAR DAHİL 250'I GEÇMEMELIDIR! 
    

    Kurallar:
    1. İlk cümlede haberin en önemli detayını açıkla
    2. İkinci cümlede takipçilere yönelik kısa bir soru/yorum ekle
    3. Yanıt tam olarak 250 karakteri geçmemelidir
    4. Kısa ve öz yaz, gereksiz kelimelerden kaçın
    
    Haber başlığı: {article['title']}
    """
    
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        
        summary = response.choices[0].message.content
        
        # Check if summary is too long
        if len(summary) > 250:
            # If too long, try one more time with stricter prompt
            prompt = f"""
            ÇOK ÖNEMLİ: Önceki yanıt çok uzundu. Aynı haberi daha kısa özetle.
            KESINLIKLE 240 KARAKTERİ GEÇMEMELI (boşluklar dahil).
            
            Sadece iki kısa cümle kullan:
            1. Haberin özü
            2. Kısa bir soru/yorum
            
            Haber: {article['title']}
            """
            
            response = openai_client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            summary = response.choices[0].message.content
        
        # Final length check
        if len(summary) > 250:
            print(f"Warning: Summary still too long ({len(summary)} chars)")
            summary = summary[:247] + "..."
            
        print(f"Character count: {len(summary)}")
        return summary
        
    except Exception as e:
        print(f"Error in summarizing article: {e}")
        return None

    
