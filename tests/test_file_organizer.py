from open_source_toolkit.file_organizer import organize_files


def test_organize_files(tmp_path):
    sample = tmp_path / "photo.jpg"
    sample.write_text("sample image")

    results = organize_files(tmp_path)

    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert ("photo.jpg", "Images") in results


def test_skip_existing_destination(tmp_path):
    source = tmp_path / "photo.jpg"
    source.write_text("new image")

    folder = tmp_path / "Images"
    folder.mkdir()
    (folder / "photo.jpg").write_text("existing image")

    results = organize_files(tmp_path)

    assert source.exists()
    assert ("photo.jpg", "Skipped: destination exists") in results
