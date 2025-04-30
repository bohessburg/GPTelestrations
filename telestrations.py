from openai import OpenAI

class Telestrations:
    def __init__(self):
        self.client = OpenAI()
        self.image_from_prompt_model = "gpt-image-1"
        self.prompt_from_image_model = "gpt-4o-mini"
        self.styles = {"MS-Paint", "sketch","simple line drawing"}
        self.max_prompt_length = 100
        self.max_prompt_words = 6
        self.image_size = "128x128"

    def set_model(self, model_string):
        self.model = model_string

    def add_style(self, style):
        self.styles.add(style)

    def remove_style(self, style):
        self.styles.remove(style)

    def get_image_url_from_prompt(self, image_prompt):
        if len(image_prompt) > self.max_prompt_length:
            print("prompt is too long (max length: " + str(self.max_prompt_length) + ")")
            return None

        img = self.client.images.generate(
            model=self.prompt_from_image_model,
            prompt = "{p}, {s}".format(p=image_prompt, s=', '.join(self.styles)),
            size= self.image_size
        )
        return img.data[0].url

    def get_prompt_from_image(self, image_url):
        chat = self.client.chat.completions.create(
            model = self.prompt_from_image_model,
            messages=[
                {"role":"user","content":[
                    {"type":"text","text":"Generate a 1 to {w} word prompt that might generate this picture".format(w=self.max_prompt_words)},
                    {"type":"image_url","image_url":{"url":image_url}}
                ]}
            ])
        return chat.choices[0].message.content
