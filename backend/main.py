import os

import aiofiles
from fastapi import FastAPI, UploadFile, File


app = FastAPI(title="Hype")


@app.post("/predict")
async def get_predict(in_file: UploadFile = File(...)):
    path = "data/" + in_file.filename
    async with aiofiles.open(path, 'wb') as out_file:
        content = await in_file.read()
        await out_file.write(content)
    try:
        '''
        write your code here
        '''
        return path
    finally:
        os.unlink(path)
