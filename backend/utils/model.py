import torch


model = torch.hub.load('facebookresearch/pytorchvideo', 'slowfast_r50', pretrained=True)
