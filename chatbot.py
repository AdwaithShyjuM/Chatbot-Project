import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample responses
responses = {
    "hello,hi,hey": "Hi there! How can I help you today?",
    "how are you": "I'm just a program, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "what's the weather like": "I can't provide real-time weather information. Please check a weather website or app.",
    "tell me a joke": "Sure, here's a joke: Why did the chicken cross the road? To get to the other side!"
}

def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase
    stop_words = set(stopwords.words('english'))  # Set of stopwords
    stemmer = PorterStemmer()  # Initialize stemmer

    # Tokenize and remove stopwords for the current user input
    tokens = [word for word in word_tokenize(user_input) if word not in stop_words]
    
    # If user input is exactly matching a predefined key, return the response directly
    if user_input in responses:
        return responses[user_input]

    # Stem the tokens
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    responses_list = []  # To collect responses for each prompt

    # Check for responses based on stemmed tokens
    for key in responses:
        key_tokens = [stemmer.stem(word) for word in word_tokenize(key)]  # Stem the key phrase
        # Check if any token from key matches the stemmed tokens from user input
        if any(token in stemmed_tokens for token in key_tokens):
            responses_list.append(responses[key])  # Add response to list

    # If no responses were found, return a default message
    if not responses_list:
        return "I'm sorry, I didn't understand that."
    
    return " ".join(responses_list)  # Return combined responses

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Start the chat
chat()
