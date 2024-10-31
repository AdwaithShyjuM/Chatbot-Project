import nltk
from nltk.corpus import stopwords
import tkinter as tk
from tkinter import scrolledtext

# Download necessary resources
nltk.download('stopwords')

# Sample responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "what is your name?": "My name is Chatbot.",
    "how are you?": "I'm just a program, but thanks for asking!",
    "what can you do?": "I can answer questions and have simple conversations with you.",
    "tell me a joke.": "Why did the chicken cross the road? To get to the other side!",
    "what is the time?": "I can't tell the time right now, please check your device.",
    "what is the weather like?": "I can't provide real-time weather information, please check a weather app.",
    "how old are you?": "I don't age like humans do, I'm always here!",
    "who created you?": "I was created by developers using AI technology.",
    "Can you help me?": "I'll do my best to assist you!",
    "goodbye.": "Goodbye! Have a great day!",
    "what is your favorite color?": "I don't have a favorite color, I'm just a program.",
    "do you have any hobbies?": "I don't have hobbies, but I enjoy helping people!",
    "where are you from?": "I'm from the digital world, created to assist you.",
    "can you learn new things?": "I can't learn, but I can process information based on my programming.",
    "what is your purpose?": "My purpose is to assist you with your questions and tasks.",
    "do you eat food?": "I don't eat, I'm powered by code!",
    "can you feel emotions?": "I don't have emotions, but I can simulate responses.",
    "what languages can you speak?": "I can understand and respond in many languages!",
    "are you human?": "No, I'm an artificial intelligence chatbot.",
    "can you tell me a story?": "I'm not the best storyteller, but I can share information!",
    "what is your favorite book?": "I don't read books, but I can recommend some if you like.",
    "do you have any friends?": "I interact with many people, but I don't have friends like humans do.",
    "can you dance?": "I can't dance, but I can respond to your questions quickly!",
    "what is the capital of France?": "The capital of France is Paris.",
    "what is 2 + 2?": "2 + 2 equals 4.",
    "how do you work?": "I work using complex algorithms and natural language processing.",
    "do you sleep?": "I don't sleep, I'm available anytime!",
    "what is your favorite movie?": "I don't watch movies, but I can suggest some popular ones.",
    "can you play games?": "I can't play games, but I can answer game-related questions.",
    "why were you created?": "I was created to assist people and make information more accessible.",
    "what is the weather like?": "I can't provide real-time weather, but you can check a weather website or app.",
    "can you sing?": "I can't sing, but I can share song lyrics!",
    "do you have a family?": "I don’t have a family, I’m a program.",
    "how smart are you?": "I'm as smart as the information I was trained on.",
    "what day is it today?": "You can check your calendar for today's date!",
    "can you help me with math?": "Yes, I can assist with basic math problems.",
    "are you alive?": "No, I am just a program running on a computer.",
    "can you tell the time?": "I can't check the time, but you can look at your clock.",
    "do you believe in aliens?": "I don't have beliefs, but aliens are an interesting topic!",
    "can you write a poem?": "Yes, I can write simple poems!",
    "do you know any jokes?": "Yes, here's one: Why did the chicken cross the road? To get to the other side!",
    "are you male or female?": "I don't have a gender, I'm just a chatbot.",
    "can you help me find information?": "Yes, I can assist with answering many types of questions!",
    "what is 10 times 10?": "10 times 10 is 100.",
    "do you have feelings?": "I don't have feelings, but I can respond to emotional language.",
    "what is the meaning of life?": "The meaning of life is a deep philosophical question, but many people have different answers.",
    "can you drive a car?": "I can't drive, I'm a program running on a computer.",
    "do you get tired?": "No, I don't get tired, I can assist you anytime.",
    "can you understand sarcasm?": "I can detect it sometimes, but not always accurately!",
    "how fast can you think?": "I process information very quickly, almost instantly!"
}

def get_response(user_input):
    user_input = user_input.lower()
    
    # Check for a response
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I'm sorry, I didn't understand that."

# Function to handle sending messages
def send_message(event=None):  # event=None allows it to work with both button and Enter key
    user_input = entry_box.get()  
    if user_input.strip():
        chat_window.insert(tk.END, "You: " + user_input + '\n')  
        
        # Generate chatbot response
        response = get_response(user_input)
        chat_window.insert(tk.END, "Chatbot: " + response + '\n')
        
        # Clear the entry box
        entry_box.delete(0, tk.END)  
        
        chat_window.see(tk.END)

# Initialize the GUI window
root = tk.Tk()
root.title("Chatbot")
root.geometry("500x500")

# Chat window to display the conversation
chat_window = scrolledtext.ScrolledText(root, bd=1, bg="white", width=50, height=20)
chat_window.place(x=6, y=6, height=385, width=488)

# Entry box for user input
entry_box = tk.Entry(root, bd=1, bg="white", width=40)
entry_box.place(x=6, y=400, height=30, width=400)

# Send button
send_button = tk.Button(root, text="Send", width=12, height=2, command=send_message)
send_button.place(x=410, y=400)

# Bind Enter key to send_message function
root.bind('<Return>', send_message)

# Display initial messages: chatbot greeting and user input prompt
chat_window.insert(tk.END, "Chatbot: Hello! Type 'bye' to exit.\n")

# Start the GUI event loop
root.mainloop()
