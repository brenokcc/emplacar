import os
import base64
import requests


class GoogleVision:

    def __init__(self):
        self.token = os.environ.get("GOOGLE_VISION_API_KEY")

    def base64(self, path):
        return base64.b64encode(open(path, 'rb').read()).decode()

    def detect_text(self, uri):
        image = {"source": {"image_uri": uri}} if uri.startswith('http') else {"content": uri}
        url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(self.token)
        data = {"requests": [{"image": image, "features": {"type": "TEXT_DETECTION"}}]}
        response = requests.post(url, json=data).json()
        for item in response['responses']:
            if item and 'fullTextAnnotation' in item:
                return item['fullTextAnnotation']['text']
        return ''

    def check_words(self, text, words=()):
        import unidecode
        text = unidecode.unidecode(' '.join(text.split()).upper())
        missing = []
        for word in words:
            for token in word.split(' '):
                if unidecode.unidecode(token.upper()) not in unidecode.unidecode(text):
                    missing.append(token)
        return missing

if __name__ == "__main__":
    ws = GoogleVision()
    text = ws.detect_text("https://sigplac.com.br/media/foto_traseira/8d6b3bcf249e11ed83eeb24e8f392f63.jpeg")
    print(text)
    missing = ws.check_words('**** CARLOS BRENO ***', ('CARLOS', 'BRENO', 'SILVA'))
    print(missing)