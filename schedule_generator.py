from groq import Groq

client = Groq(api_key="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")

def generate_schedule(topics, exam_days):
    topics_str = "\n".join(topics)
    prompt = f"""
    Create a detailed day-by-day study schedule for a student.
    
    Topics to cover:
    {topics_str}
    
    Total days available: {exam_days}
    
    Rules:
    - Spread topics evenly across the days
    - Include revision days in the last week
    - Keep Day 1 light to build momentum
    - Format it clearly as Day 1, Day 2, etc.
    - Each day should have 2-3 hours of study max
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
