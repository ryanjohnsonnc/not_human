import openai

def askGPT(text):
  openai.key = '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'
  response = openai.Completion.create(
      engine = "text-davinci-003",
      prompt = text,
      temperature = 0.6,
      max_tokens = 150
  )
  return print(response.choices[0].text)