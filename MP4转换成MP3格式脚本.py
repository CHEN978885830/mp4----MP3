import os
from ffmpy3 import FFmpeg

def convert_to_mp3(input_file, output_file):
    ff = FFmpeg(
        executable=r'C:\Users\chen\Desktop\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe',
        inputs={input_file: None},
        outputs={output_file: '-vn -ar 44100 -ac 2 -ab 192k -f mp3'}
    )
    ff.run()

def batch_convert_to_mp3(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(('.mp4', '.avi', '.mkv')):  
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.mp3'
            output_path = os.path.join(output_folder, output_filename)

            # 转换视频到 MP3
            convert_to_mp3(input_path, output_path)
            print(f'{filename} 转换完成.')

# 替换为实际的输入和输出文件夹路径
input_folder_path = r"C:\Users\chen\Desktop\测试"
output_folder_path = r"C:\Users\chen\Desktop\输出"

batch_convert_to_mp3(input_folder_path, output_folder_path)
