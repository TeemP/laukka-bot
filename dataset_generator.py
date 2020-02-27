from os import path
from pydub import AudioSegment

# Read data
def read_files(source_path, ending):
    data_list = []
    for file_name in os.listdir(source_path):
        if file_name[-len(ending):] ==ending                                 
            sound = AudioSegment.from_mp3(os.join(source_path,file_name))
            data_list.append(sound)

def write_files(audio_data_list, target_path):
    for i,audio_data in enumerate(audio_data_list):
        sound.export(os.join(target_path,i), format="mp3")

def generate_dataset(source_audio_data_list):
    source_audio_data_list_size = len(source_audio_data_list)
    for i,source_audio_data in enumerate(source_audio_data_list):
        for j in range(i,source_audio_data_list_size):
            #todo mix audio

def main():
    # Paths
    source_path = './data/source'
    target_path = './data/target'                                                                       
    ending = ".mp3"
    write_files(generate_dataset(read_files(source_path, ending)))
    print('Dataset generated to directory:',target_path)
