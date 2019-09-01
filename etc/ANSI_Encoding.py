import io
import shutil

file_path_ansi = '/path/to/ansi_original'
file_path_utf8 = '/path/to/utf8_output'

with io.open(file_path_ansi, encoding='latin-1', errors='ignore') as source:
    with io.open(file_path_utf8, mode='w', encoding='utf-8') as target:
        shutil.copyfileobj(source, target)
