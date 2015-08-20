import requests
f = open('00000001.webp','wb')


image_url = 'https://k2.okccdn.com/php/load_okc_image.php/images/225x225/225x225/308x59/604x355/2/5649049356000747631.webp'
f.write(requests.get(image_url).content)
f.close()