#Program to Convert Text To Speech 
from gtts import gTTS
text="Hi Welcome To Belgin Android"
out=gTTS(text=text,lang='en',slow=False)
out.save("spc.mp3")

 
