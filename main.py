import os
import shutil
import argparse

class FileOrganizer:
    """
    Clase para organizar archivos en una carpeta especifica por tipo.
    """
    def __init__(self, source_folder, dry_run=False):
        """
        Inicializa el organizador con la carpeta fuente.
        """
        self.source_folder = source_folder
        self.dry_run = dry_run
        self.file_types = {
            "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
            "Documentos": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx"],
            "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
            "Audios": [".mp3", ".wav", ".aac", ".flac"],
            "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Ejecutables": [".exe", ".msi", ".dmg"],
            "Programacion": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".php", ".json", ".xml"],
            "Otros": []
        }
        self.files_moved = 0
        self.files_skipped = 0
        self.folders_created = 0
    
    def _get_file_type_category(self, file_extension):
        """
        Metodo interno para determinar la categoria de un archivo.
        """
        for category, extensions in self.file_types.items():
            if file_extension.lower() in extensions:
                return category
        return "Otros"
    
    def organize(self):
        """
        Ejecuta el proceso de organizacion de archivos.
        """
        if not os.path.isdir(self.source_folder):
            print(f"Error: La ruta '{self.source_folder}' no es una carpeta valida o no existe.")
            return False
        
        print(f"\n--- Iniciando organizacion en: {self.source_folder} ---")
        if self.dry_run:
            print("--- MODO SIMULACION (Dry Run): No se moveran archivos ---")

        for filename in os.listdir(self.source_folder):
            file_path = os.path.join(self.source_folder, filename)

            if os.path.isfile(file_path) and filename != os.path.basename(__file__):
                file_name, file_extension = os.path.splitext(filename)
                category = self._get_file_type_category(file_extension)

                destination_folder = os.path.join(self.source_folder, category)

                try:
                    if not os.path.exists(destination_folder) and not self.dry_run:
                        os.makedirs(destination_folder, exist_ok=True)
                        self.folders_created += 1
                        print(f"Carpeta creada: '{category}/")
                    elif os.path.exists(destination_folder):
                        print(f"Carpeta existente: '{category}/")

                    if not self.dry_run:    
                        shutil.move(file_path, destination_folder)
                        print(f"Movido: '{filename}' a '{category}/'")
                        self.files_moved += 1
                    else:
                        print(f"Simulando movimiento: '{filename}' a '{category}/'")
                        self.files_moved += 1
                except Exception as e:
                    print(f'Error al mover "{filename}": {e}')
                    self.files_skipped += 1
            elif os.path.isdir(file_path):
                print(f'Saltando directorio: "{filename}"')
            else:
                print(f'Saltando elemento no archivado: "{filename}"')

                print(f"\n--- Proceso de organizacion completado ---")
                print(f'Archivos procesados (movidos/simulados): {self.files_moved}')
                print(f'Archivos omitidos (errores o directorios): {self.files_skipped}')
                print(f'Carpetas ceradas: {self.folders_created}')
                return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organiza archivos en una carpeta por tipo.")
    parser.add_argument("folder", type=str, help="La ruta completa de la carpeta a organizar.")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Simula la organizacion sin mover archivos.")

    args = parser.parse_args()

    organizer = FileOrganizer(args.folder, dry_run=args.dry_run)
    organizer.organize()