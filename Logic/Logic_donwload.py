from Entity.Entity_donwload import entity_donwload
from Implemet.Implement_donwload import implement_video
from  Complement.complement import on_progress
from pytube import  YouTube

class logic_donwload (implement_video):
    def donwload_video(self, vid : entity_donwload):
        try:
            yt = YouTube(vid.Url, on_progress_callback=on_progress)
            video_stream = yt.streams.get_highest_resolution()
            print(f"TITULO: {video_stream.title}")
            video_stream.download(vid.ruta)
        except Exception as e:
            print(f'ERROR AL DESCARGAR LA VIDEO {e}')

    def donwload_music(self, vid: entity_donwload):
        try:
            yt = YouTube(vid.Url,on_progress_callback = on_progress )
            musica_stream = yt.streams.get_audio_only()
            print(f"TITULO: {musica_stream.title}")
            musica_stream.download(vid.ruta)
        except Exception as e:
            print(f"ERROR AL DESCARGAR LA MUSICA {e}")


