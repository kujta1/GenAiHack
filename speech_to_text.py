import speech_recognition as sr
from moviepy.editor import VideoFileClip
from gtts import gTTS
from playsound import playsound

# Create a recognizer object
def speech_to_text_microphone():
    
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError as e:
            print("Error occurred; {0}".format(e))
            

def speech_to_text_audio_file(file_location):
    
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.AudioFile(file_location) as source:
        audio = recognizer.record(source)  # Read the entire audio file

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError as e:
            print("Error occurred; {0}".format(e))

def speech_to_text_video(video_path, audio_output_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_output_path)
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_output_path) as source:
        audio = recognizer.record(source)  # Read the entire audio file

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError as e:
            print("Error occurred; {0}".format(e))
            
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    audio_file = "output.mp3"
    tts.save(audio_file)
    playsound(audio_file)

# Example usage
# video_path = 'path/to/video.mp4'
# audio_output_path = 'path/to/output/audio.wav'

# text_to_speech_video(video_path, audio_output_path)