import pydub
import numpy
import math
import scipy.io.wavfile
import numpy.fft as fft

def save_wav(data, rate, word):
  scipy.io.wavfile.write(f"sounds-music/{word}.wav", rate, data)

def read_mp3(f, normalized=False):
  """MP3 to numpy array"""
  a = pydub.AudioSegment.from_mp3(f)
  y = numpy.array(a.get_array_of_samples())
  if a.channels == 2:
    y = y.reshape((-1, 2))
  if normalized:
    return a.frame_rate, numpy.float32(y) / 2**15
  else:
    return a.frame_rate, y

# return freq, list of 0 points
def analyze(data, sr):
  indiv_periods = []
  change_indexes = []
  last_change_time = 0
  for i in range(1, len(data)):
    if (data[i] > 0 and data[i - 1] <= 0) or (data[i] <= 0 and data[i-1] > 0):
      curr_change_time = i / sr
      change_indexes.append(i)
      indiv_periods.append(curr_change_time - last_change_time)
      last_change_time = curr_change_time
  
  #  remove first element
  indiv_periods = indiv_periods[1:]
  change_indexes = change_indexes[1:]
  period_sigma = 0
  for period in indiv_periods:
    period_sigma += period
  return (1 / (period_sigma / len(indiv_periods)), change_indexes)

def change_pitch(data, factor, change_indexes):
  new_data = []
  for i in range(0, data[change_indexes[0]]):
    new_data.append(data[i])
  for i in range(0, len(change_indexes) - 1):
    print(change_indexes[i], change_indexes[i+1])
    data_inbetween_count = change_indexes[i + 1] - change_indexes[i]
    filled_in = 0
    count = 0
    while filled_in < data_inbetween_count:
      data_i = change_indexes[i] + math.floor(filled_in)
      new_data.append(data[data_i])
      filled_in += factor
      count += 1
    while count < data_inbetween_count:
      new_data.append(0)
      count += 1
  print(change_indexes[0], change_indexes[-1])
  for i in range(change_indexes[-1], len(data)):
    new_data.append(data[i])
    pass
  np_new_data = numpy.asarray(new_data)
  print(np_new_data)
  return np_new_data

def make_freq(word, note):
  sr, data = read_mp3(f"sounds/{word}.mp3")
  freq, change_indexes = analyze(data, sr)
  print(f"The word {word} frequency is {freq}")
  pitch_factor = 1
  data_new_pitch = change_pitch(data, pitch_factor, change_indexes)
  print(len(data), len(data_new_pitch))
  save_wav(data_new_pitch, sr, word)

# spectrum = fft.fft(data)
#   freqs = fft.fftfreq(len(spectrum))

#   for coef,freq in zip(spectrum,freqs):
#     if coef:
#       print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,f=freq))
#   # freq = fft.fftfreq(len(spectrum)) * sr
#   # print(f"original frequency: {freq}")

