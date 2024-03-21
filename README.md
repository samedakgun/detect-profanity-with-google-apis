Introduction
Welcome to our Speech and Text Processing Project! This project leverages the power of Google's API to perform several tasks related to speech and text processing, including speech-to-text conversion, language detection, translation, and profanity detection. It's designed to handle inputs in both audio and text formats, making it versatile for various use cases. Whether you're looking to analyze audio files or text, this project aims to provide a comprehensive solution.

Features
Speech Processing: For audio inputs, the project adjusts the sample rate (Hertz correction), converts speech to text, detects the language, and translates non-English audio to English.
Text Processing: For text inputs, the project detects the language and translates non-English text to English.
Profanity Detection: Utilizes a custom model to detect profanity in the processed text, regardless of the original input format.
Support for Multiple Languages: The project supports several languages including English, Spanish, French, Turkish, Italian, Arabic, German, and Chinese, with easy extensibility for more languages.
How It Works
Language Support: The project includes predefined language codes for supported languages, allowing for accurate speech recognition and translation.

Speech to Text: Audio files undergo Hertz correction for optimal speech recognition. The speech is then converted to text using Google's Speech-to-Text API, with language detection and translation handled for non-English languages.

Text Translation: Text inputs are first detected for language and then translated to English if necessary, readying the text for profanity detection.

Profanity Detection: Both converted texts from audio and direct text inputs are analyzed for profanity using a custom model trained for this purpose.

Installation
To set up the project, follow these steps:

Clone the repository to your local machine.
Ensure you have Python installed.
Install the required dependencies by running pip install -r requirements.txt.
Obtain Google API credentials and place them in the specified location within the project.
Usage
Run main.py and follow the prompts to input either an audio file or text. Choose the appropriate language for audio inputs. The script will process the input accordingly and display whether the text contains profanity.

Components
main.py: The entry point of the application. Handles user inputs and integrates all components.
predict_for_swear.py: Contains functions for loading the profanity detection model and making predictions.
speech_to_text.py: Facilitates speech to text conversion and language translation using Google's APIs.
Contributing
Contributions to improve the project are welcome. Please follow the standard fork and pull request workflow.

