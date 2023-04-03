from pydub import AudioSegment

mp3_file_path = "shindara.m4a"
wav_file_path = "shindara.wav"

audio = AudioSegment.from_file(mp3_file_path, format="m4a")
audio.export(wav_file_path, format="wav")
