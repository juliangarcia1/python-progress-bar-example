from tqdm import tqdm
import requests

url = 'https://www.fing.edu.uy/~canale/latex.pdf'

req = requests.get(url)

file_size = int(req.headers['Content-length'])
filename = "aname.pdf" # req.headers['Content-Disposition']
chunk_size = 1024
with open(filename, 'wb') as fw:
    for chunck in tqdm(iterable= req.iter_content(chunk_size=chunk_size), total = file_size/chunk_size, unit = 'kb'):
        fw.write(chunck)

