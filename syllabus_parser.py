from groq import Groq

client = Groq(api_key="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")

def extract_topics(syllabus_text):
    prompt = f"""
    Read this syllabus and extract all the main topics and subtopics.
    Return ONLY a Python list of topic names as strings, nothing else.
    Example: ["Newton's Laws", "Thermodynamics", "Wave Motion"]
    
    Syllabus:
    {syllabus_text}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    import ast
    try:
        topics = ast.literal_eval(response.choices[0].message.content.strip())
        return topics
    except:
        return [line.strip() for line in response.choices[0].message.content.split('\n') if line.strip()]
