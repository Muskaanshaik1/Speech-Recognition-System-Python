from pydub import AudioSegment

def convert_to_standard_wav(input_file, output_file="standard_audio.wav"):
    try:
        audio = AudioSegment.from_file(input_file)
        # Export as 16-bit PCM WAV, mono, 16kHz (common standard for speech)
        audio.export(output_file, format="wav", parameters=["-acodec", "pcm_s16le", "-ac", "1", "-ar", "16000"])
        print(f"Successfully converted '{input_file}' to '{output_file}'")
        return True
    except Exception as e:
        print(f"Error converting audio file: {e}")
        print("Ensure FFmpeg is installed and added to your system's PATH.")
        return False

if __name__ == "__main__":
    input_wav_path = "my_audio.wav" # Your problematic WAV file
    output_wav_path = "my_audio_standard.wav" # New, standardized WAV file name
    if convert_to_standard_wav(input_wav_path, output_wav_path):
        print(f"\nNow try transcribing '{output_wav_path}' in your speech_to_text.py script.")
        print("Remember to change the line in speech_to_text.py from:")
        print('transcribe_audio_file("my_audio.wav")')
        print("to:")
        print('transcribe_audio_file("my_audio_standard.wav")')