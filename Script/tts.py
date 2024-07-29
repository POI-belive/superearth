import requests
import pyaudio

# 流式传输音频的URL，你可以自由改成Post
stream_url = 'http://127.0.0.1:5000/tts?character=胡桃&text=狂气的蛋幕遗产：东方绀珠传～ 疯狂王国的遗产，是由上海爱丽丝幻乐团所制作的纵向卷轴蛋幕射击游戏，东方Project系列的第十五作&stream=true'

# 初始化pyaudio
p = pyaudio.PyAudio()

# 打开音频流
stream = p.open(format=p.get_format_from_width(2),
                channels=1,
                rate=32000,
                output=True)

# 使用requests获取音频流，你可以自由改成Post
response = requests.get(stream_url, stream=True)

# 读取数据块并播放
for data in response.iter_content(chunk_size=1024):
    stream.write(data)

# 停止和关闭流
stream.stop_stream()
stream.close()

# 终止pyaudio
p.terminate()
