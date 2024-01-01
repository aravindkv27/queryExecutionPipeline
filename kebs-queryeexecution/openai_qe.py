import openai
import json

# Set your OpenAI API key

def query_optimization_suggestion(queries):

    openai.api_key = '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'


    openai_input = queries.split('\n')
    messages = [
        {"role": "system", "content": "You are a kind helpful assistant."},
    ]

    message = f'{openai_input}, provide me and optimized suggestion for the query. Dont add query in the response.'


    messages.append(
        {"role": "user", "content": message},
    )

    # print("ChatGPT: Processing your request")


    chat = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106", messages=messages
    )


    reply = chat.choices[0].message.content
    return reply

def lambda_handler(event, context):
    
    # if 'body' in event:
    queries = json.loads(event['body'])
    response = query_optimization_suggestion(queries)
    
    return response
    