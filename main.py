import os
import shutil

# --- Configuracion ---
FILE_TYPES = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Audios": [".mp3", ".wav", ".aac", ".flac"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Ejecutables": [".exe", ".msi", ".dmg"],
    "Programacion": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".php", ".json", ".xml"],
    "Otros": [] # Para archivos que no encajan en ninguna categoría
}

def get_file_type_category(file_extension):
    """
    Determina la categoria de un archivo basandose en su extension.
    """
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return "Otros"

def organize_folder(source_folder):
    """
    Organiza los archivos en la carpeta especifica.
    """
    if not os.path.isdir(source_folder):
        print(f"Error: La ruta '{source_folder}' no es una carpeta valida.")
        return
    
    print(f"Iniciando organizacion en: {source_folder}")

    # Itera sobre todos los elementos en la carpeta
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Ignorar directorios, solo procesar archivos
        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(filename)
            category = get_file_type_category(file_extension)

            print(f"Archivo: {filename} -> Categoria: {category} (Extension: {file_extension})")

            # --- Logica para crear carpetas y mover archivos ---

            print("Proceso de categorizacion inicial completado.")

if __name__ == "__main__":
    # Pide al usuario la ruta de la carpeta a organizar
    folder_to_organize = input("Introduce la ruta completa de la carpeta a organizar: ")
    organize_folder(folder_to_organize)