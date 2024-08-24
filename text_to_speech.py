from transformers import pipeline

def text_to_speech(text):
    tts = pipeline('text-to-speech')
    audio = tts(text)
    with open('output.wav', 'wb') as f:
        f.write(audio)
    return 'output.wav'

# Example usage
print(text_to_speech('Hello, this is a text-to-speech example.'))
