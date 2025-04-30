from telestrations import Telestrations
import os
from dotenv import load_dotenv
from IPython.display import Image, display

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")

T = Telestrations()
prompt = "Neighbor angry about windchimes"

img = T.get_image_url_from_prompt(prompt)
display(Image(url=img))

for i in range(4):
    new_prompt = T.get_prompt_from_image(img)
    print(new_prompt)
    input()

    img = T.get_image_url_from_prompt(new_prompt)
    display(Image(url=img))