import torch
from torchvision import models
from torchvision import transforms
from PIL import Image

resnet = models.resnet101(pretrained=True)
transform = transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
img = Image.open("malcolm.jpg")
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
print(labels[index[0]], percentage[index[0]].item())

print("Complete.")