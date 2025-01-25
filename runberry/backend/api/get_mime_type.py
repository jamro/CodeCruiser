def get_mime_type(path):
    mime_types = {
        ".txt": "text/plain",
        ".log": "text/plain",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
    }

    for ext, mime_type in mime_types.items():
        if path.endswith(ext):
            return mime_type
      
    return None