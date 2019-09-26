import sys
from gtts import gTTS
import os
import soundmanip

def get_text(text_path):
  f = open(text_path, "r")
  contents = f.read()
  print(text_path)
  print(contents)
  f.close()
  return contents

def make_to_audio(words):
  for word in words:
    tts = gTTS(text=word, lang='en')
    tts.save(f"sounds/{word}.mp3")
    os.system(f"mpg321 sounds/{word}.mp3")

def main():
  text_path = "words.txt"
  print(sys.argv)
  if len(sys.argv) > 1 and sys.argv[1] != "":
    text_path = sys.argv[1]
  text = get_text(text_path)
  words = text.split(" ")
  # audio_words = make_to_audio(words)
  soundmanip.make_freq(words[0], 1000)
if __name__ == "__main__":
  main() 