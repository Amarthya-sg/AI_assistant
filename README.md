# Voice Assistant

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Customization](#customization)
- [Copying the Project](#copying-the-project-to-your-system)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview
This Voice Assistant is a Python-based application that can perform various tasks through voice commands. It uses speech recognition to understand user input and text-to-speech to communicate responses.

## Features
- Voice interaction using speech recognition and text-to-speech
- Wikipedia search
- Web browsing (YouTube, Google, Stack Overflow)
- Music playback
- Time and date information
- Weather updates
- Email sending capability

## Requirements
- Python 3.x
- pyttsx3
- SpeechRecognition
- wikipedia
- requests

## Setup
1. Clone this repository or download the `main.py` file.
2. Install the required dependencies:
   ```
   pip install pyttsx3 SpeechRecognition wikipedia requests
   ```
3. Obtain an API key from OpenWeatherMap for weather functionality.
4. Update the following in the `main.py` file:
   - Replace `'your_api_key_here'` with your actual OpenWeatherMap API key.
   - Replace `'your_city_name_here'` with your desired default city for weather updates.
   - For email functionality, update the email and password in the `sendEmail` function.

## Usage
Run the script using Python:
```
python main.py
```

The assistant will greet you based on the time of day and wait for your voice command. You can ask it to:

- Search Wikipedia: "Wikipedia [your query]"
- Open websites: "Open YouTube/Google/Stack Overflow"
- Play music: "Play music" (ensure you've set the `music_dir` variable)
- Get the time: "What's the time?"
- Get the date: "What's the date?"
- Check weather: "What's the climate?"
- Send an email: Implement the email sending logic as needed

To exit the program, say "shutdown".

## Customization
- To change the voice, modify the `engine.setProperty('voice', voices[0].id)` line in the initialization.
- Add more functionalities by extending the if-elif statements in the main loop.

## Note
This project uses the Google Speech Recognition API, which requires an internet connection. Ensure you're connected to the internet while using the voice assistant.

## Copying the Project to Your System

1. Install Git on your system if you haven't already (https://git-scm.com/downloads).
2. Open a terminal or command prompt.
3. Navigate to the directory where you want to store the project.
4. Clone the repository:
   ```
   git clone https://github.com/yourusername/voice-assistant.git
   ```
   Replace `yourusername` with the actual GitHub username where the project is hosted.
5. Navigate into the project directory:
   ```
   cd voice-assistant
   ```
6. Follow the setup instructions above to install dependencies and configure the project.

## Contributing

We welcome contributions to improve the Voice Assistant project! Here's how you can contribute:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature/your-feature-name
   ```
4. Make your changes and commit them with a descriptive commit message:
   ```
   git commit -m "Add a brief description of your changes"
   ```
5. Push your changes to your fork on GitHub:
   ```
   git push origin feature/your-feature-name
   ```
6. Open a pull request from your fork to the main repository.

### Contribution Guidelines

- Follow the existing code style and conventions.
- Write clear, concise commit messages.
- Include comments in your code where necessary.
- Update the README if you're adding new features or changing functionality.
- Add unit tests for new features to ensure reliability.
- Make sure all existing tests pass before submitting a pull request.

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check the GitHub Issues to see if it has already been reported.
2. If not, open a new issue, providing as much detail as possible, including:
   - A clear, descriptive title
   - A detailed description of the issue or suggestion
   - Steps to reproduce (for bugs)
   - Expected and actual behavior
   - Your environment (OS, Python version, etc.)

## Contact
For any questions or feedback, please reach out to the project maintainer:
[GitHub Profile](https://github.com/Amarthya-sg)
