# Voice Assistant in Python
<br>Author- Amarthya S George</br>
This project is a simple voice-controlled assistant built using Python. The assistant can recognize your voice commands, respond with spoken words, search Wikipedia, open popular websites, play music, tell the current time and date, and even fetch weather data for a specific city. It also includes functionality to send emails and shutdown on voice command.

    Features
- Voice recognition and text-to-speech interaction.
- Wikipedia search functionality.
- Open websites like YouTube, Google, and Stack Overflow.
- Play music from your local directory.
- Provide the current time and date.
- Fetch weather information using the OpenWeatherMap API.
- Send emails.
- Shutdown command to stop the assistant.

    Python Version
This project is built using   Python 3.8   or later. Please ensure that you have the correct Python version installed.

    Installation

1. Clone the repository.
   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
   ```

2. Install the required packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. You will need to:
   - Update the `sendEmail()` function with your email credentials.
   - Get an API key from OpenWeatherMap and update it in the `get_weather()` function.
   - Set your city in the weather query section.

4. Run the program:
   ```bash
   python assistant.py
   ```

    Requirements
All the required Python libraries can be installed using the `requirements.txt` file. Make sure you have pip installed, then use the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

This list includes the libraries used in the project. Make sure your system has the correct audio drivers for `pyaudio`, as it is required for microphone access.
