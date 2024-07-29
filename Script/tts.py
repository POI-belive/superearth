import requests
import pyaudio

class AudioStreamer:
    def __init__(self, character: str, text: str):
        self.character = character
        self.text = text
        self.stream_url = self._generate_stream_url()

    def _generate_stream_url(self) -> str:
        # 根据传入的 character 和 text 生成流式传输音频的 URL
        base_url = 'http://127.0.0.1:5000/tts'
        return f'{base_url}?character={self.character}&text={self.text}&stream=true'

    def play_audio(self):
        # 初始化pyaudio
        p = pyaudio.PyAudio()

        # 打开音频流
        stream = p.open(format=p.get_format_from_width(2),
                        channels=1,
                        rate=32000,
                        output=True)

        # 使用requests获取音频流
        response = requests.get(self.stream_url, stream=True)

        # 读取数据块并播放
        for data in response.iter_content(chunk_size=1024):
            stream.write(data)

        # 停止和关闭流
        stream.stop_stream()
        stream.close()

        # 终止pyaudio
        p.terminate()

