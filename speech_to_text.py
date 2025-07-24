import speech_recognition as sr
from os import path # This helps us work with file paths

# --- (Keep the listen_and_transcribe function from Step 2 here) ---
def listen_and_transcribe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service; check your internet connection: {e}")

# --- NEW FUNCTION FOR AUDIO FILES ---
def transcribe_audio_file(file_path):
    r = sr.Recognizer()
    # Make sure the audio file exists at this path
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), file_path)

    # Use AudioFile instead of Microphone
    with sr.AudioFile(AUDIO_FILE) as source:
        # Read the entire audio file
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        print(f"Transcription from file '{file_path}': {text}")
    except sr.UnknownValueError:
        print(f"Sorry, I could not understand the audio in '{file_path}'.")
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service for '{file_path}'; check your internet connection: {e}")

# --- MODIFY THE MAIN PART TO CALL BOTH OR CHOOSE ---
if __name__ == "__main__":
    print("--- Testing Microphone Input ---")
    listen_and_transcribe()
    print("\n--- Testing Audio File Input ---")
    # Replace 'my_audio.wav' with the actual name of your .wav file
    transcribe_audio_file("my_audio_standard.wav")