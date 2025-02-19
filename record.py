from array import array
from struct import pack
from sys import byteorder
import copy
import pyaudio
import wave
import time 

THRESHOLD = 5000
CHUNK_SIZE = 1024
RATE = 16000
SILENT_CHUNKS = 3 * RATE / CHUNK_SIZE
FORMAT = pyaudio.paInt16
FRAME_MAX_VALUE = 2 ** 15 - 1
NORMALIZE_MINUS_ONE_dB = 10 ** (-1.0 / 20)
CHANNELS = 1
TRIM_APPEND = RATE / 4

def isSilent(data_chunk):
    # print(max(data_chunk))
    return max(data_chunk) < THRESHOLD

def normalize(data_all):
    normalize_factor = (float(NORMALIZE_MINUS_ONE_dB * FRAME_MAX_VALUE)
                        / max(abs(i) for i in data_all))

    r = array('h')
    for i in data_all:
        r.append(int(i * normalize_factor))
    return r

def trim(data_all):
    _from = 0
    _to = len(data_all) - 1
    for i, b in enumerate(data_all):
        if abs(b) > THRESHOLD:
            _from = max(0, i - TRIM_APPEND)
            break

    for i, b in enumerate(reversed(data_all)):
        if abs(b) > THRESHOLD:
            _to = min(len(data_all) - 1, len(data_all) - 1 - i + TRIM_APPEND)
            break

    return copy.deepcopy(data_all[int(_from):int(_to + 1)])

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    silence = [0] * int(seconds * RATE)
    r = array('h', silence)
    r.extend(snd_data)
    r.extend(silence)
    return r

def record():
    silent_chunks = 0
    audio_started = False
    data_all = array('h')
    print("record")
    count = 0
    while True:
        data_chunk = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            data_chunk.byteswap()
        data_all.extend(data_chunk)
        silent = isSilent(data_chunk)

        if count > 100:
            if silent:
                silent_chunks += 1
                if silent_chunks > SILENT_CHUNKS:
                    break
            else:
                silent_chunks = 0
        count+=1
        if(count == 100):
            print('Fale agora!')
        # elif not silent:
            # print('audio started')
            # audio_started = True

    sample_width = p.get_sample_size(FORMAT)
    #stream.stop_stream()
    #stream.close()
    #p.terminate()

    data_all = trim(data_all)
    data_all = normalize(data_all)
    data_all = add_silence(data_all, 0.5)
    return sample_width, data_all

def recordToFile(path):
    sample_width, data = record()
    wave_file = wave.open(path, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(sample_width)
    wave_file.setframerate(RATE)
    wave_file.writeframes(data)
    wave_file.close()

def sample():
    _, data = record()
    return data

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, output=True, frames_per_buffer=CHUNK_SIZE)
