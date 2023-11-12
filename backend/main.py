from pytorchvideo.data.encoded_video import EncodedVideo
from fastapi import FastAPI, UploadFile, File
from utils.transform import *
from utils.model import model
# from labels import labels
import aiofiles
import uvicorn
import torch
import json
import os

app = FastAPI(title="Hype")

num_frames = 32
sampling_rate = 2
frames_per_second = 30
start_sec = 0
clip_duration = (num_frames * sampling_rate) / frames_per_second
end_sec = start_sec + clip_duration

@app.post("/predict")
async def get_predict(in_file: UploadFile = File(...)):
    path = "data/" + in_file.filename
    async with aiofiles.open(path, 'wb') as out_file:
        content = await in_file.read()
        await out_file.write(content)
    try:
        video = EncodedVideo.from_path(path)
        video_data = video.get_clip(start_sec=start_sec, end_sec=end_sec)
        video_data = transform(video_data)
        inputs = video_data["video"]
        inputs = [i.to('cpu')[None, ...] for i in inputs]
        post_act = torch.nn.Softmax(dim=1)
        preds = post_act(model(inputs))
        pred_classes = preds.topk(k=5).indices
        with open("classnames/kinetics_classnames.json", "r") as f:
            kinetics_classnames = json.load(f)
        kinetics_id_to_classname = {}
        for k, v in kinetics_classnames.items():
            kinetics_id_to_classname[v] = str(k).replace('"', "")
        pred_class_names = [kinetics_id_to_classname[int(i)] for i in pred_classes[0]]
        return {"name": path, "predict": pred_class_names}

    finally:
        os.unlink(path)


'''
@app.post("/predict1")
def get_predict1():
    path = "C:\\Users\\hecfi\\Downloads\\(Rad)Schlag_die_Bank!_cartwheel_f_cm_np1_le_med_0.avi"
    model = torch.hub.load('facebookresearch/pytorchvideo', 'slowfast_r50', pretrained=True)
    model.blocks[-1].proj = nn.Linear(2304, 400)
    list(model.children())[-1][-2].pool[0] = nn.AvgPool3d(kernel_size=(79, 7, 7), stride=(1, 1, 1), padding=(0, 0, 0))
    list(model.children())[-1][-2].pool[1] = nn.AvgPool3d(kernel_size=(320, 7, 7), stride=(1, 1, 1), padding=(0, 0, 0))
    vid = read_video(path, output_format='THWC')
    frame = vid[0]
    trg = frame.permute(3, 0, 1, 2)
    inputs = UniformTemporalSubsample(81)(trg)
    t = CenterCrop((256, 256))
    inputs = t(inputs)
    inputs = inputs.float() / 255
    inputs = ShortSideScale(size=256)(inputs)
    inputs = NormalizeVideo([0.45, 0.45, 0.45], [0.225, 0.225, 0.225])(inputs)

    slow_pathway = inputs.unsqueeze(0)

    fast_pathway = torch.index_select(inputs, 1, torch.linspace(0, inputs.shape[1] - 1, 322).long()).unsqueeze(0)

    frame_list = [slow_pathway, fast_pathway]
    predictions = list()

    predictions.append(labels[model(frame_list).argmax().item()])
    return 1
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)
'''
