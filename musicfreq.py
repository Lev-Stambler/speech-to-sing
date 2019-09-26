import math

A4 = 440
C0 = A4*math.pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
def pitch(freq):
  h = round(12 * math.log2(freq / C0))
  octave = h // 12
  n = h % 12
  return name[n] + str(octave)

def freq(note):
  note_split = list(note)
  n = note_split[0]
  octave = note_split[1]
  h = name.index(n) + int(octave) * 12
  return round((2 ** (h / 12)) * C0)

if __name__ == "__main__":
  print(freq("C8"))