
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_descargados = total_size - bytes_remaining
    porcentaje = (bytes_descargados / total_size) * 100
    print(f"Progreso: {porcentaje:.2f}%", end='\n')