import sounddevice as sd
import soundfile as sf
import queue
import numpy
import sys

q = queue.Queue()

fileText = '/Users/mac/OtherProjects/ProcessSound/Homework1/data/Tam_su/Tam_su.txt'
nameWav = 'Cau_6.wav'
filename = '/Users/mac/OtherProjects/ProcessSound/Homework1/data/Tam_su/' + nameWav

def callback(indata, frames, time, status):
    #Callback from another thread 
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def recordingFile(filename, sentence, fileText, nameWav):
    print('Read the below sentence:\n')
    print(sentence)
    try:
        with sf.SoundFile(filename, mode='x', samplerate = 22000,
                        channels = 1) as file:
            with sd.InputStream(samplerate = 22000, device = sd.default.device,
                                channels = 1, callback = callback):
                print('Press Ctrl+C to stop the recording')
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))

    file = open(fileText, "a")
    file.write(nameWav + '\n')
    file.write(sentence + '\n')
    file.close()

sentence = 'Phải làm sao để sống và tồn tại?'


recordingFile(filename, sentence, fileText, nameWav)
