def batch_images(image_paths, batch_size=3):
    for i in range(0, len(image_paths), batch_size):
        yield image_paths[i:i + batch_size]