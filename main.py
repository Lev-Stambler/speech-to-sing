import sys
from gtts import gTTS
import os
import soundmanip
import wav_lib
import stitch

import re

def get_text(text_path):
  f = open(text_path, "r")
  contents = f.read()
  print("text path:", text_path)
  print("text contents: ", contents)
  f.close()
  return contents

def make_to_audio(words):
  for word in words:
    tts = gTTS(text=word, lang='en')
    tts.save(f"sounds/{word}.mp3")
    os.system(f"mpg321 sounds/{word}.mp3")

def get_words(text):
  return re.sub(r"[.,]", "", text).split(" ")

def main():
  notes = ["C4", "C4", "G4", "G4", "A4", "A4", "G4", "F4", "E4", "D4", "C4"]
  text_path = "words.txt"
  if len(sys.argv) > 1 and sys.argv[1] != "":
    text_path = sys.argv[1]
  text = get_text(text_path)
  words = get_words(text)
  # audio_words = make_to_audio(words)
  for i in range(0, len(notes)):
    soundmanip.make_freq(words[i], notes[i], i)
  stitch.stitch(len(notes))

if __name__ == "__main__":
  main() 