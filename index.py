import openai
import config


def gpt3(stext):
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=stext,
        temperature=0.1,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    # print(content)
    return response.choices[0].text


query = 'What is up dog'
response = gpt3(query)
print(response)
