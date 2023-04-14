from time import sleep
from pytube import YouTube , Playlist
import platform
import os
import socket

class YoutubeDownloader():
    
    def __init__(self) -> None:
        
        if self.checkConnection():

            self.upgradePackage()

            self.main()
            
        else:
            print('Waiting for connection...')
            
            for i in range(20):
                
                if self.checkConnection():
                    
                    self.upgradePackage()
                    self.main()
                    break
                
                sleep(3)
    
    def get_file_instructions(self, file_path):
        with open("test.txt", "r") as file:
            lines = file.readlines()

            instructions = []
            current_instruction = []

            for line in lines:
                if line.strip() == "":
                    instructions.append(current_instruction)
                    current_instruction = []
                else:
                    current_instruction.append(line.strip())
            # Add the last set of instructions after reaching the end of the file
            if current_instruction:
                instructions.append(current_instruction)
        return instructions

    def getInput(self):
        '''Return [link, dest, option]'''

        link = input('Enter the link: ')
        dest = input('Enter destination(optional): ')
        option = int(input('Video(1) or audio(0): '))
        
        if option == 1:
            quality = input('Enter quality(360 or 720): ')+'p'
        else:
            quality = None
        
        print()

        return [link,dest,option,quality]
    
    def getExceptions(self, exception):

        exceptions = []

        str = exception.split(',')
        for s in str:
            if s.__contains__('-'):
                s = s.split('-')
                exceptions += range(int(s[0]), int(s[-1])+1)
            else:
                exceptions.append(int(s))

        return exceptions
    
    def downloadPlaylist(self, inputs):
        '''Expects a nested list of inputs parameter'''
        for item in inputs:
    
            link = item[0].split()
            url = link[0]
            
            if len(link) == 2:
                exception = self.getExceptions(link[1])
            else:
                exception = []

            dest = item[1]
            option = item[2]
            quality = item[3]

            playlist = Playlist(url)
            playlist_length = len(playlist.video_urls)-(len(exception))
            print(f"{playlist_length} video(s)")

            i = 1
            d = 0
            if option == 1:
                for video in playlist.videos:
                    
                    if i in exception:
                        i += 1
                        continue
                    
                    try:
                        print("Downloading {}".format(video.title))
                        v = video.streams.get_by_resolution(quality)

                        if v is None:
                            v = video.streams.get_highest_resolution()
                        
                        v.download(dest)

                        d+=1
                    except:
                        print(f'Download faield for {video.title}')
                        continue
            
            elif option == 0:
                for video in playlist.videos:
                    
                    if i in exception:
                        i += 1
                        continue
                    
                    try:
                        print("Downloading {}".format(video.title))
                        video.streams.get_audio_only().download(dest)
                        d+=1
                    except:
                        print(f'Download failed for {video.title}')
                        continue

            print(f"Downloaded {d} of {playlist_length}")
            print('===============')
            
    def downloadSingleVideo(self, inputs):
        '''Expects a nested list of inputs parameter'''
        for item in inputs:
        
            link = item[0]
            dest = item[1]
            option = item[2]
            quality = item[3]

            video = YouTube(link)
            print("Downloading",video.title)
            
            if option == 1:
                try:
                    video.streams.get_by_resolution(quality).download(dest)
                except:
                    print(f'Download failed for {video.title}')
                    continue

            elif option == 0:
                try:
                    video.streams.get_audio_only().download(dest)
                except:
                    print(f'Download failed for {video.title}')
                    continue

            print("Downloaded!")
            print('===============')

    def notify():
        if platform.system() == 'Windows':
            import winsound
            winsound.MessageBeep()
    
    def main(self):
    
        while True:
            
            c = input("Press s for single video, p for playlist, f for a file or q to quit: ")
            
            if c == 'q':
                break
            
            elif c == 'f':
                path = input('Enter file path: ')
                instructions = self.get_file_instructions(path)
                inputs = None

                for instruction_set in instructions:
                    url_type = instruction_set[0]
                    url = instruction_set[1]
                    dest = instruction_set[2]
                    option = int(instruction_set[3])
                    quality = instruction_set[4]

                    inputs = [[url, dest, option, quality]]
                    if url_type == 'p':
                        self.downloadPlaylist(inputs)
                    elif url_type == 's':
                        self.downloadSingleVideo(inputs)

            else:
                n = int(input('Enter number of trials: '))
                print()
                inputs = []
                
                if c == 'p':
                    for x in range(n):
                        inputs.append(self.getInput())
                    
                    self.downloadPlaylist(inputs)
                
                elif c == 's':
                    for x in range(n):
                        inputs.append(self.getInput())
                    
                    self.downloadSingleVideo(inputs)

            self.notify()

    def checkConnection(self):
        try:
            host = socket.gethostbyname("www.google.com")
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            return False

    def upgradePackage(self):
        stream = os.popen('pip install --upgrade pytube')
        output = stream.readlines()
        

obj = YoutubeDownloader()