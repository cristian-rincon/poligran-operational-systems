import os
from typing import List, Optional

import typer
from loguru import logger
import httpx
import threading

app = typer.Typer()

BASE_URL_PEXELS_API = "https://api.pexels.com/v1/"
PEXELS_API_KEY = ""


def get_photo(photo_id: int):
    url = f"{BASE_URL_PEXELS_API}photos/{photo_id}"
    headers = {"Authorization": f"{PEXELS_API_KEY}"}
    response = httpx.get(url, headers=headers)
    original_image_size = httpx.get(response.json()["src"]["original"])
    # Save the photo to a file
    file = open(f"{photo_id}.png", "wb")
    file.write(original_image_size.content)
    file.close()


@app.command()
def download_photos(
    photo_ids: List[int]
):
    """Download photos from pexels.com"""
    current_directory = os.getcwd()
    typer.secho(f"Downloading {len(photo_ids)} photos", fg="green")
    with typer.progressbar(photo_ids, label="Downloading progress") as bar:
        for photo_id in bar:
            new_thread = threading.Thread(target=get_photo, args=(photo_id,))
            typer.secho(f"\nStarting thread for photo {photo_id}", fg="green")
            new_thread.start()
    typer.secho(f"\nAll photos downloaded to {current_directory}", fg="green")

if __name__ == "__main__":
    app()