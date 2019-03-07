import pdb

import requests
from tqdm import tqdm

url = 'https://cdn-10.nikon-cdn.com/pdf/manuals/dslr/D90_es.pdf'

req = requests.get(url, stream=True, headers={'Accept-Encoding': None})

file_size = int(req.headers['Content-length'])
filename = "aname.pdf" # req.headers['Content-Disposition']
chunk_size = 1024
with open(filename, 'wb') as fw:
    for chunck in tqdm(iterable= req.iter_content(chunk_size=chunk_size), total = file_size/chunk_size, unit = 'KB'):
        fw.write(chunck)
