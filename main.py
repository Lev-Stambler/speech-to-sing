#!/usr/bin/python

import sys
from gtts import gTTS
import os


def get_text(path):
  f = open(path, "r")
  contents = f.read()
  f.close()
  return contents

def make_to_audio(words):
  for word in words:
    tts = gTTS(text=word, lang='en')
    tts.save(f"{word}.mp3")
    os.system(f"mpg321 {word}.mp3")

def main():
  text_path = "words.txt"
  if len(sys.argv) > 0 and sys.argv[0] != "":
    text_path = sys.argv[0]
  text = get_text(text_path)
  words = text.split(" ")
  audio_words = make_to_audio(words)

if __name__ == "__main__":
  main() 