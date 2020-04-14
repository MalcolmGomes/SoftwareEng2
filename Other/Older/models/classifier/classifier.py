import torch
import time
import sys
from torchvision import models
from torchvision import transforms
from PIL import Image

def classify(img):
    start = time.time()
    resnet = models.resnet101(pretrained=True)
    transform = transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)
    resnet.eval()
    out = resnet(batch_t)
    with open('imagenet_classes.txt') as f:
        classes = [line.strip() for line in f.readlines()]
    _, index = torch.max(out, 1)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    _, indices = torch.sort(out, descending=True)
    labels = classes
    [(labels[idx], percentage[idx].item()) for idx in indices[0][:5]]
    inference = labels[index[0]]
    confidence = round(percentage[index[0]].item(), 2)
    end = time.time()
    duration = round(end - start, 2)
    return (inference, confidence, duration)

if __name__ == '__main__':
    img = Image.open("malcolm.jpg")
    inference, confidence, duration = classify(img)
    print('Predicted Class:', inference, 'Confidence:', confidence, '% Runtime:', duration, 'seconds.')
    print("\nExecution Complete.")