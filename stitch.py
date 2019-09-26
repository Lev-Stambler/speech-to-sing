import wav_lib
import numpy

def stitch(total_elems):
    data_fin = []
    for i in range(total_elems):
        print(f"sounds-music/{str(i)}.wav")
        sr, data = wav_lib.open_wav(f"sounds-music/{str(i)}.wav")
        data_fin.extend(data)
    wav_lib.save_wav(numpy.asarray(data_fin), sr, "final.wav")
