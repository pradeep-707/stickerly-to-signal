import requests
import anyio
import os
from pathlib import Path
from signalstickers_client import StickersClient
from signalstickers_client.models import LocalStickerPack, Sticker


async def upload_pack(stickerly_pack_id, pack_name, pack_author):
    def add_sticker(path, emoji):
        stick = Sticker()
        stick.id = pack.nb_stickers
        stick.emoji = emoji

        with open(path, "rb") as f_in:
            stick.image_data = f_in.read()

        pack._addsticker(stick)

    pack = LocalStickerPack()

    pack.title = pack_name
    pack.author = pack_author

    # Add the stickers here, with their emoji
    # Accepted format:
    # - Non-animated webp
    # - PNG
    # - GIF <100kb for animated stickers
    images = os.listdir(f"res/{stickerly_pack_id}")
    for image_name in images:
        add_sticker(f"res/{stickerly_pack_id}/{image_name}", "🤪")

    # Specifying a cover is optional
    # By default, the first sticker is the cover
    cover = Sticker()
    cover.id = pack.nb_stickers
    # Set the cover file here
    with open(f"res/{stickerly_pack_id}/{images[0]}", "rb") as f_in:
        cover.image_data = f_in.read()
    pack.cover = cover
    print("downloaded all stickers!")

    # Instantiate the client with your Signal credentials
    user_id = open("user-id.txt", "r").read()
    password = open("password.txt", "r").read()
    print("\nuploading pack...")
    async with StickersClient(user_id, password) as client:
        # Upload the pack
        pack_id, pack_key = await client.upload_pack(pack)

    with open("res/" + stickerly_pack_id + "/" + stickerly_pack_id + "_signal.txt", "w") as f:
        f.write(f"https://signal.art/addstickers/#pack_id={pack_id}&pack_key={pack_key}")
    print(f"\nPack uploaded!\nhttps://signal.art/addstickers/#pack_id={pack_id}&pack_key={pack_key}")


pack_id = input()
pack_response = requests.get(f"http://api.sticker.ly/v3.1/stickerPack/{pack_id}")
pack_info = pack_response.json()['result']
base_url = pack_info['resourceUrlPrefix']
stickers_info = pack_info['stickers']
Path(f"res/{pack_id}").mkdir(parents=True, exist_ok=True)
for sticker_info in stickers_info:
    file_name = sticker_info['fileName']
    full_image_url = base_url + file_name
    img_data = requests.get(full_image_url).content
    with open("res/" + pack_id + "/" + file_name, 'wb') as handler:
        handler.write(img_data)
    print("downloading sticker...")

anyio.run(upload_pack, pack_id, pack_info['name'], pack_info['authorName'])
