from fastapi import FastAPI, UploadFile, File
import torch
from typing import Dict
import json
import urllib
from torchvision.transforms import Compose, Lambda
from torchvision.transforms._transforms_video import (
    CenterCropVideo,
    NormalizeVideo,
)
from pytorchvideo.data.encoded_video import EncodedVideo
from pytorchvideo.transforms import (
    ApplyTransformToKey,
    ShortSideScale,
    UniformTemporalSubsample,
    UniformCropVideo
)

app = FastAPI(title="Hype")

side_size = 256
mean = [0.45, 0.45, 0.45]
std = [0.225, 0.225, 0.225]
crop_size = 256
num_frames = 32
sampling_rate = 2
frames_per_second = 30
alpha = 4


class PackPathway(torch.nn.Module):
    """
    Transform for converting video frames as a list of tensors.
    """

    def __init__(self):
        super().__init__()

    def forward(self, frames: torch.Tensor):
        fast_pathway = frames
        # Perform temporal sampling from the fast pathway.
        slow_pathway = torch.index_select(
            frames,
            1,
            torch.linspace(
                0, frames.shape[1] - 1, frames.shape[1] // alpha
            ).long(),
        )
        frame_list = [slow_pathway, fast_pathway]
        return frame_list


transform = ApplyTransformToKey(
    key="video",
    transform=Compose(
        [
            UniformTemporalSubsample(num_frames),
            Lambda(lambda x: x / 255.0),
            NormalizeVideo(mean, std),
            ShortSideScale(
                size=side_size
            ),
            CenterCropVideo(crop_size),
            PackPathway()
        ]
    ),
)

# The duration of the input clip is also specific to the model.
clip_duration = (num_frames * sampling_rate) / frames_per_second

model = torch.hub.load('facebookresearch/pytorchvideo', 'slowfast_r50', pretrained=True)

start_sec = 0
end_sec = start_sec + clip_duration


@app.post("/predict")
def get_predict(filepath: str):
    # Load the desired clip
    video = EncodedVideo.from_path(filepath)
    #video = EncodedVideo()
    # Load the desired clip
    video_data = video.get_clip(start_sec=start_sec, end_sec=end_sec)

    # Apply a transform to normalize the video input
    video_data = transform(video_data)

    # Move the inputs to the desired device
    inputs = video_data["video"]
    inputs = [i.to('cpu')[None, ...] for i in inputs]
    post_act = torch.nn.Softmax(dim=1)
    #print(model)
    preds = post_act(model(inputs))
    pred_classes = preds.topk(k=5).indices
    print(pred_classes)
    # Map the predicted utils to the label names
    json_url = "https://dl.fbaipublicfiles.com/pyslowfast/dataset/class_names/kinetics_classnames.json"
    json_filename = "kinetics_classnames.json"
    try:
        urllib.URLopener().retrieve(json_url, json_filename)
    except:
        urllib.request.urlretrieve(json_url, json_filename)
    with open(json_filename, "r") as f:
        kinetics_classnames = json.load(f)
    # Create an id to label name mapping
    kinetics_id_to_classname = {}
    for k, v in kinetics_classnames.items():
        kinetics_id_to_classname[v] = str(k).replace('"', "")
    pred_class_names = [kinetics_id_to_classname[int(i)] for i in pred_classes[0]]
    return {
        "name": file.filename,
        "data": {
            "content_type": file.content_type,
            "headers": file.headers,
            "file_size": file.size,
        },
        "predict": pred_class_names
    }

@app.post("/predict2")
def get_predict2(file: File()):
    # vid = read_video('/kaggle/input/hmdb-human-activity-recognition/HMDB_dataset/brush_hair/testing_14.avi', output_format='THWC')

    return {

    }
