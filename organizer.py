import os
import shutil
from pathlib import Path

# Category mapping based on file extensions
EXTENSION_MAP = {
    # Documents
    '.pdf': 'Documents', '.docx': 'Documents', '.doc': 'Documents',
    '.txt': 'Documents', '.pptx': 'Documents', '.xlsx': 'Documents',
    # Images
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
    # Videos
    '.mp4': 'Videos', '.mkv': 'Videos', '.avi': 'Videos',
    # Archives
    '.zip': 'Archives', '.rar': 'Archives', '.tar': 'Archives', '.gz': 'Archives',
    # Code
    '.py': 'Code', '.js': 'Code', '.html': 'Code', '.css': 'Code'
}

def organize_directory(target_dir='.'):
    target_path = Path(target_dir).resolve()
    print(f"=== Starting File Organization in: {target_path} ===\n")
    
    files_moved = 0
    categories_created = set()

    # Use os.scandir for efficient filesystem traversal
    with os.scandir(target_path) as entries:
        for entry in entries:
            # Skip directories and the script itself
            if entry.is_dir() or entry.name == 'organizer.py':
                continue

            file_ext = Path(entry.name).suffix.lower()
            category = EXTENSION_MAP.get(file_ext, 'Others')

            # Create destination category folder if it doesn't exist
            dest_dir = target_path / category
            dest_dir.mkdir(exist_ok=True)
            categories_created.add(category)

            dest_file_path = dest_dir / entry.name

            try:
                # Handle naming collisions if file already exists in target folder
                if dest_file_path.exists():
                    base_stem = Path(entry.name).stem
                    counter = 1
                    while dest_file_path.exists():
                        new_name = f"{base_stem}_{counter}{file_ext}"
                        dest_file_path = dest_dir / new_name
                        counter += 1

                shutil.move(entry.path, dest_file_path)
                print(f"[MOVED] {entry.name} -> {category}/")
                files_moved += 1

            except PermissionError:
                print(f"[ERROR] Permission denied: {entry.name}")
            except FileExistsError:
                print(f"[ERROR] File exists error: {entry.name}")
            except Exception as e:
                print(f"[ERROR] Could not move {entry.name}: {e}")

    print("\n=== Execution Summary ===")
    print(f"Total files relocated: {files_moved}")
    print(f"Categories updated: {', '.join(categories_created) if categories_created else 'None'}")

if __name__ == "__main__":
    organize_directory()
