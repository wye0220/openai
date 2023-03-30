import os
import openai

# get your API key from https://beta.openai.com/account/api-keys
openai.api_key = os.getenv("OPENAI_API_KEY")
# get the model ID from https://beta.openai.com/models
COMPLETION_MODEL = "text-davinci-003"
SCREEN_WIDTH = 160

def get_response(prompt):
  completions = openai.Completion.create(
    engine=COMPLETION_MODEL,
    prompt=prompt,
    max_tokens=512,
    n=1,
    stop=None,
    temperature=0.5,
  )
  message = completions.choices[0].text.strip()
  return message

def chatbot_start():
    print("Welcome to the chatbot!")
    print("Ask me a question, I'll try my best to answer it!")
    print("If you want to quit, type 'quit'!")

    while True:
        question = input("Q : ")
        if question == "quit":
          print("Bye!")
          break
        answer = get_response(question)
        print("A : " + answer)

if __name__ == '__main__':
    chatbot_start()