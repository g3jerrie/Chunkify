# 
#   Chunkify
#
#   @g3jerrie
#



import os
import contextlib

def split_file(file_path, chunk_size):
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk
            
            
def write_chunk(chunk, index):
    with open(f'chunk_{index}', 'wb') as f:
        f.write(chunk)
        
def split_file_to_chunks(file_path, chunk_size):
    with contextlib.ExitStack() as stack:
        f = stack.enter_context(open(file_path, 'rb'))
        for i, chunk in enumerate(split_file(file_path, chunk_size)):
            write_chunk(chunk, i)
            
# Split into max 1GB chunks       
split_file_to_chunks('largeFileName.zip', 1 * 1024 * 1024 * 1024)