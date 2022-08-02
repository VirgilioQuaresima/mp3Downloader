import os
import logging

def timeConverter(millis):

    # numerical conversion from milliseconds to minute
    seconds=int((millis/1000)%60)
    minutes=int((millis/(1000*60))%60)

    # convert int to string in formato ->  00h:00m:00s
    str_minutes=str(minutes)
    str_seconds=str(seconds)
    if minutes<10:
        str_minutes="0"+str(minutes)
    if seconds<10:
        str_seconds="0"+str(seconds)

    response="00:"+str_minutes+":"+str_seconds
    return response

def downloader(filename,url):
    import youtube_dl

    ydl_opts = {
        'format': 'bestaudio/best',
        'logger':logging,
        'outtmpl':filename,
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        logging.info("download video: "+video_title)
        ydl.download([str(url)])

def cutter(filename, startMin, startSec, endMin, endSec):
    from pydub import AudioSegment
    try:
        #importing file from location by giving its path
        sound = AudioSegment.from_mp3(filename+'mp3')
        
        total_duration=timeConverter(len(sound))
        # Time to milliseconds conversion
        StrtTime = startMin*60*1000+startSec*1000
        EndTime = endMin*60*1000+endSec*1000
        logging.info("**************")
        logging.info("Start time: " +timeConverter(StrtTime))
        logging.info("**************")
        logging.info("End time: " +timeConverter(EndTime))
        logging.info("**************")

        # cutting
        if StrtTime == 0:
            extract= sound[:EndTime]
        elif EndTime == 0:
            RestTime=len(sound)-StrtTime
            extract= sound[-RestTime:]
        else:            
            extract = sound[StrtTime:EndTime]

        logging.info("Durata video originale: "+total_duration)
        logging.info("**************")
        logging.info("Durata video tagliato: "+timeConverter(len(extract)))
        logging.info("**************")
        # Saving file in required location
        extract.export(filename+"mp3", format="mp3")
    except Exception as e:
        logging.error(e)
