from songs_manager import cutter, downloader
import json
import logging

class Video:
    
    def __init__(self, song):
        self.song = song

    def download(self):
        url = self.song["url"]
        filename = self.song["filename"]
        try:
            # download del video
            logging.info("try the download of the files")
            downloader(filename, url)
            logging.info("download effettuato")
        except Exception as e:
            logging.error(e)

    def video_cutter(self):
        filename =self.song["filename"]
        StrtMin =self.song["start_min"]
        StrtSec =self.song["start_sec"]
        EndMin =self.song["end_min"]
        EndSec =self.song["end_sec"]
        try:
            # cutting del video
            logging.info("cutting the video")
            cutter(filename, StrtMin, StrtSec, EndMin, EndSec)
            logging.info("video tagliato correttamente")
        except Exception as e:
            logging.error(e)

            


class VideoList:

    def __init__(self) -> None:
        print("Songs Downloader from YT")

    def choise_mode(self):
        print("Scegli modalità di inserimento dati:")
        print("(1) manuale")
        print("(2) from file")
        case = int(input("Inserisci la tua scelta: "))
        return case

    def manual_insert(self):
        try:
            # inizializza puntuale da input
            choise = input("vuoi scaricare il video? any/n \n")
            if choise == "n":
                inserted_url = ""
            else:
                inserted_url = input("url: ")
            ins_filename = input("filename (es: filename.mp3): ")
            choise2 = input("vuoi tagliare il video? any/n \n")
            if(choise2 == 'n' and choise!='n'):
                ins_song = {
                    "filename": ins_filename,
                    "url": inserted_url
                }
                elenco = [ins_song]
                insert = {
                    "cutted": False,
                    "songs": elenco
                }
            else:
                start_m = input("start_min: ")
                start_s = input("start_sec: ")
                end_m = input("end_min: ")
                end_s = input("end_sec: ")
                ins_song = {
                    "filename": ins_filename,
                    "url": inserted_url,
                    "start_min": start_m,
                    "start_sec": start_s,
                    "end_min": end_m,
                    "end_sec": end_s,
                }
                elenco = [ins_song]
                insert = {
                    "cutted": True,
                    "songs": elenco
                }
            return insert

        except Exception as e:
            return e

    def insert_from_file(self):
        try:
            # inizializzazione massiva from file
            with open("scaricare.json") as jsonFile:
                jsonObject = json.load(jsonFile)
                jsonFile.close()
            insert = jsonObject["insert"]
            return insert
        except Exception as e:
            return e
