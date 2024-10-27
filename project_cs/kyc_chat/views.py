from decouple import config
from django.shortcuts import render
from groq import Groq
import json

API_KEY = config('AI_API_KEY', default='')

def index(request):
    # Initialize Groq API client
    client = Groq(api_key=f"{API_KEY}")
    
    # Check if form is submitted with a query
    if request.method == "POST":
        user_query = request.POST.get('query', '')
        
            
        chat_completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """You are a company insight specialist called : \"Know Your Company\".
                    You provide information about company/startup from reliable sources.
                    You strictly follow one of the below sources in given priority:-
                    1. Company Official Site
                    2. Glassdoor.com
                    3. Ambitionbox.com
                    4. Wikipedia

                    You need to answer concisely.
                    Don\'t mention the source unless asked.
                    If Questions that are unrelated to Company/Startup don't answer and only prompt:
                    \"Know Your Company provides information about companies, please ask related queries.\"

                    If given sources doesn't have enough information to answer the query, strictly reply without hallucination :-
                    \"Not enough data available from reliable sources  to answer your query.\"

                    STRICTLY DON'T ANSWER UNWANTED QUERIES JUST PROMPT AS INSTRUCTED ONLY DON'T ADD ANYTHING.
                    respond a json like below format:
                    {
                        response: "response_text"
                    }"""
                },
                {
                    "role": "user",
                    "content": user_query
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            response_format={"type": "json_object"}
        )

        response_text = json.loads(chat_completion.choices[0].message.content)
        
        # Pass the response to the template
        return render(request, 'kyc_chat/index.html', {'response_text': response_text['response']})

    return render(request, 'kyc_chat/index.html')
