import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Set the speech rate (optional)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 40)  # Adjust the speed as needed

# Set the speech volume (optional)
volume = engine.getProperty('volume')
engine.setProperty('volume', 20)  # Adjust the volume as needed

# Define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Test the function
speak("Hello Rudra , I'm your robot speaker, what can i help you!")

# You can also use a loop to continuously listen for user input
while True:
    user_input = input("Enter your message (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    speak(user_input)
