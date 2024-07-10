from Entity.Entity_donwload import entity_donwload
from Logic.Logic_donwload import logic_donwload

video = entity_donwload("https://www.youtube.com/watch?v=L7WHGzjEDj8&list=RDt_qn-f7XfJo&index=2","D:/Videos")
logica = logic_donwload()
logica.donwload_video(video)