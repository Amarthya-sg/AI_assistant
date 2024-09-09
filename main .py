# Importing necessary libraries for various functionalities
import pyttsx3  # For text-to-speech conversion
import speech_recognition as sr  # For speech recognition from microphone
import datetime  # To handle date and time
import wikipedia  # To fetch information from Wikipedia
import webbrowser  # To open web pages
import os  # To interact with the operating system (like opening files)
import smtplib  # To send emails
import requests  # To fetch data from APIs (like weather data)

# Initialize the text-to-speech engine with the SAPI5 voice (used for Windows systems)
engine = pyttsx3.init('sapi5')

# Get the available voices and set the desired voice (0 is the default male voice)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # You can change to voices[1].id for female voice if available

def speak(audio):
    """
    Convert the given text (audio) into speech.
    
    Parameters:
    audio (str): Text to be spoken by the engine.
    
    """
    engine.say(audio)
    engine.runAndWait()  # Ensures the speech is delivered before the program continues

def wishMe():
    """
    Greet the user based on the current time of the day.
    This function will greet with 'Good Morning', 'Good Afternoon', or 'Good Evening' depending on the hour.
    """
    hour = int(datetime.datetime.now().hour)  # Get the current hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hey, what can I do for you?")  # Additional prompt after greeting

def takeCommand():
    """
    Listens to the user's voice, recognizes speech, and converts it into text.
    
    Returns:
    query (str): The recognized command in text format.
    If recognition fails, it returns "None".
    """
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause time before processing the next phrase
        audio = r.listen(source)  # Capture the audio from the microphone

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognize the audio using Google Speech API
        print(f"User said: {query}\n")  # Print what the user said

    except Exception as e:
        print("Say that again please...")  # If recognition fails, ask the user to repeat
        return "None"  # Return 'None' if speech is not recognized
    return query

def sendEmail(to, content):
    """
    Sends an email to the specified recipient with the provided content.
    
    Parameters:
    to (str): Email address of the recipient.
    content (str): The content/body of the email.
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Initialize the SMTP server with Gmail's SMTP
    server.ehlo()  # Establish connection to the server
    server.starttls()  # Secure the connection using TLS
    server.login('youremail@gmail.com', 'your-password')  # Login to the Gmail account
    server.sendmail('youremail@gmail.com', to, content)  # Send the email
    server.close()  # Close the SMTP connection

def get_weather(city_name, api_key):
    """
    Fetch the current weather information for the given city.
    
    Parameters:
    city_name (str): The name of the city for which the weather is to be fetched.
    api_key (str): The API key for authenticating with the OpenWeatherMap service.
    
    Returns:
    weather_info (str): A description of the current weather including temperature and weather conditions.
    If the API call fails, returns an error message.
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'  # Weather API URL
    response = requests.get(url)  # Make the HTTP request to the API
    data = response.json()  # Parse the JSON response
    if data['cod'] == 200:  # If the city is found
        weather_description = data['weather'][0]['description']  # Get the weather description
        temperature = data['main']['temp']  # Get the temperature in Celsius
        return f"The weather in {city_name} is {weather_description} with a temperature of {temperature}°C."
    else:
        return "Unable to fetch weather data."  # Error if city is not found or API fails

# Main function that executes the voice assistant's logic
if __name__ == '__main__':
    wishMe()  # Call the greeting function

    # The assistant runs continuously until the 'shutdown' command is given
    while True:
        query = takeCommand().lower()  # Convert the user’s command to lowercase for easy matching

        # Logic to handle different types of commands:
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")  # Remove 'wikipedia' from the query to get the search term
            results = wikipedia.summary(query, sentences=2)  # Fetch the summary from Wikipedia (2 sentences)
            speak("According to Wikipedia")
            print(results)  # Print the result in the console
            speak(results)  # Speak the result

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  # Open YouTube in the web browser

        elif 'open google' in query:
            webbrowser.open("google.com")  # Open Google in the web browser

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  # Open StackOverflow in the web browser

        elif 'play music' in query:
            music_dir = ''  # Path to the folder containing music files
            songs = os.listdir(music_dir)  # List all files in the music directory
            print(songs)  # Print the list of songs
            os.startfile(os.path.join(music_dir, songs[0]))  # Play the first song in the list

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")  # Get the current time in 12-hour format
            speak(f"Sir, the time is {strTime}")  # Speak the time

        elif 'date' in query:
            strdate = datetime.datetime.now().strftime("%A %d %B, %Y")  # Get the current date
            speak(f"Sir, the date is {strdate}")  # Speak the date

        elif 'climate' in query:
            api_key = 'your_api_key_here'  # Insert your OpenWeatherMap API key
            city_name = 'your_city_name_here'  # Insert your city name
            weather_info = get_weather(city_name, api_key)  # Fetch the weather information
            speak(weather_info)  # Speak the weather information
            print(weather_info)  # Print the weather information in the console

        elif 'shutdown' in query:
            speak("Have a good day sir, bye")  # Farewell message before shutting down
            break  # Exit the loop, stopping the assistant
