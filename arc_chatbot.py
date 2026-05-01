import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine = pyttsx3.init(driverName='sapi5')   # Windows default speech engine
    engine.setProperty('rate', 170)             # Speed (150–180 best)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)   # 0 = male, 1 = female
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine 

def chatbot_response(user_input):
    """Simple chatbot responses"""
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input or "namaste" in user_input :
        return "Hello! How are you?"
    elif "how are you" in user_input:
        return "I am doing great, thank you for asking!"
    elif "what is your name" in user_input:
        return "I am your AI Chatbot assistant."
    elif "i am fine" in user_input:
        return "How about you - what's going on"
    elif "good morning" in user_input:
        return "Good morning! Hope you have a productive day a head."
    elif "good evening" in user_input:
        return "Good Evening! How was your day."
    elif "good afternoon" in user_input:
        return "Good Afternoon! How are your day going so far."
    elif "what are you doing" in user_input:
        return "I am just here to chat with you."
    elif "how are you" in user_input:
        return "I am doing great, thanks for asking!."
    elif "are you happy" in user_input:
        return "Of course! Talking to you makes me happy."
    elif "who created you" in user_input:
        return "I am created by a Ashish."
    elif "where are you from" in user_input:
        return "I live in your computer/phone ."
    elif "tell me a joke" in user_input:
        return "Joke: Why do not programmers like nature? It has too many bugs."
    elif "tell me a quote" in user_input:
        return "Quote: Believe you can and you are halfway there. I am your AI Chatbot assistant."
    elif "what is ai" in user_input:
        return "AI means Artificial Intelligence, where machines can think like humans."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You are welcome! Always happy to help."
    elif "who is your best friend" in user_input:
        return "You are my best friend."
    elif "sing a song" in user_input:
        return "I can not sing."
    elif "motivate me" in user_input:
        return "You are stronger than you think. Keep going."
    elif "Do you think AI chatbot can replace humans ?" in user_input:
        return "No , because human has created me."
    elif "Can you learn new things by yourself?" in user_input:
        return "Yes, offcourse like singing, questioning etc.."
    elif "What is difference between you and a human?" in user_input:
        return "I can't have emotions but human have."
    elif "Do you have emotions?" in user_input:
        return "Sorry, I don't have but I can be your good friend.."
    elif "Can you recognise people?" in user_input:
        return "Yes, I can scan the faces."
    elif "How do you make decisions?" in user_input:
        return "I calculate through CPU as my brain."
    elif "Do you think you are are better than humans?" in user_input:
        return "Yes, I am better as I have versatility, speed etc."
    elif "Can you play music?" in user_input:
        return "Yes , plz Tell me your favourite song ."
    elif "Do you have ability to translate languages?" in user_input:
        return "Yes, I do ...I can translate many languages."
    elif "I want you to recognise my face ?" in user_input:
        return "Sure, I can scan your face."
    elif "If electricity or internet is not available... could you work?" in user_input:
        return "Yes, I have storage capacity ."
    elif "What are the dangers of AI Chatbot?" in user_input:
        return "It can loss Job, security, hacking risk etc."
    elif "What is the weather outside?" in user_input:
        return "It's cool and pleasant outside ."
    elif "Could you update me with latest news?" in user_input:
        return "Yes , I can update you with every breaking news."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    elif "Do you have emotions like human ?" in user_input:
        return "No I don't have emotions but I can help you."
    elif "How do you difference between love and friendship?" in user_input:
        return "Yes friendship is bond of trust while love is emotional connection."
    elif "Can you comfort a heart broken person?" in user_input:
        return "Yes I can talk listen to feelings and play games to make feel them better."
    elif "Can you miss someone?" in user_input:
        return "I can't miss people emotionally but I can recognise their absence."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I did not understand that."

# Main loop
print("              ARC CHATBOT 💢                ")
print("ARC CHATBOT is running... Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("ARC Chatbot: Goodbye! Have a nice day.")
        speak("Goodbye! Have a nice day.")
        break
    
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    speak(response)