pip install nltk

import os

import json

class LearningChatbot:
    def __init__(self, data_file='chatbot_data.json'):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f)

    def learn(self, user_input):
        key = input("What keyword would you like to associate with this information? ")
        self.data[key] = user_input
        self.save_data()
        print(f"Learned: '{user_input}' associated with keyword '{key}'.")

    def respond(self, user_input):
        for key, value in self.data.items():
            if key.lower() in user_input.lower():
                return f"I remember you mentioned '{value}' when talking about '{key}'."
        return "I'm not sure about that. Can you teach me something?"

    def forget(self, key):
        """Remove learned information associated with a keyword."""
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"Forgot information associated with keyword '{key}'.")
        else:
            print(f"No information found for keyword '{key}'.")

    def chat(self):
        print("Hello! I'm a learning chatbot. You can teach me things or ask me questions.")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            elif user_input.lower().startswith('learn '):
                self.learn(user_input[6:])
            elif user_input.lower().startswith('forget '):
                self.forget(user_input[7:])
            else:
                response = self.respond(user_input)
                print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = LearningChatbot()
    chatbot.chat()
