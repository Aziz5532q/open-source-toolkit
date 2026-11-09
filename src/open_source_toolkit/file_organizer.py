"""File organization utilities."""

from pathlib import Path
import shutil


FILE_TYPES = {
    "Images": {".png", ".jpg", ".jpeg", ".gif", ".webp"},
    "Documents": {".pdf", ".docx", ".txt", ".odt"},
    "Videos": {".mp4", ".mov", ".avi", ".mkv"},
    "Audio": {".mp3", ".wav", ".flac", ".ogg"},
    "Archives": {".zip", ".tar", ".gz", ".rar"},
    "Code": {".py", ".js", ".html", ".css", ".java"},
}


def organize_files(directory):
    """Organize files into category folders."""
    root = Path(directory).resolve()

    if not root.is_dir():
        raise ValueError("Directory does not exist.")

    results = []

    for file_path in list(root.iterdir()):
        if not file_path.is_file():
            continue

        category = "Other"

        for folder, extensions in FILE_TYPES.items():
            if file_path.suffix.lower() in extensions:
                category = folder
                break

        destination_folder = root / category
        destination = destination_folder / file_path.name

        if destination.exists():
            results.append((file_path.name, "Skipped: destination exists"))
            continue

        destination_folder.mkdir(exist_ok=True)
        shutil.move(str(file_path), str(destination))
        results.append((file_path.name, category))

    return results
