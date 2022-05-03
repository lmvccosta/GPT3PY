import openai
import config

# Defining GPT3's configuration
def gpt3(stext):
    response = openai.Completion.create(
        # Engine has to be DaVinci to use Summarization
        engine="text-davinci-001",
        prompt=stext,
        # Temperature is emotion
        temperature=0.1,
        # Tokens define answer length
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    # print(content)
    return response.choices[0].text

# Querying GPT3, in this case it would answer "This is a test"
query = 'Say this is a test'
response = gpt3(query)
print(response)
