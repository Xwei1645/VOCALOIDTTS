# -*- coding: UTF-8 -*-
import webbrowser
from time import sleep
import pyaudio
import wave

word_list = []
data= []
cmd = 0
word = 0
helpurl = "https://www.bilibili.com/read/cv16155309"
outfile = "output.wav"

def playwav(wav):
    CHUNK = 1024
    wf = wave.open(wav, "rb")
    data = wf.readframes(CHUNK)
    p = pyaudio.PyAudio()
    
    FORMAT = p.get_format_from_width(wf.getsampwidth())
    CHANNELS = wf.getnchannels()
    RATE = wf.getframerate()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    frames_per_buffer=CHUNK,
                    output=True)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

def play():
    global index
    index = 0
    while index < len(word_list):
        playwav("voices/"+str(word_list[index])+".wav")
        index = index + 1

print("指令说明：开始（start）    播放（play）   关于/更新说明（about）   帮助（help）")
while True:
    cmd = input("请输入指令：")
    if cmd == "start":
        word_list = []
        while True:
            word = input("开始输入：")
            if word == "play":
                print("开始播放")
                play()
                break
            else:
                word_list.append(word)
                print(str(word)+"输入成功")
                word = 0
            
    if cmd == "about":
        print("更新说明：")
        print("1.使用“play”暂时替代“done”,输入“play”时会按序播放wav，请用内录软件录制")
        print("********************")
        print("*   VOCALOIDTTS    *")
        print("*  ver.0.2-220416  *")
        print("* Created by Xwei  *")
        print("*  uid:573734644   *")
        print("********************")
    if cmd == "help":
        if input("即将打开帮助专栏，输入y确认：") == "y":
            webbrowser.open(helpurl, new=0, autoraise=True)