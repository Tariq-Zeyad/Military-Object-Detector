import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

from config import CLASS_NAMES, MODEL_PATH, IMAGE_SIZE


class ImageClassifier:

    def __init__(self):
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.model = self._load_model()

        self.transform = transforms.Compose([
            transforms.Resize(
                (IMAGE_SIZE, IMAGE_SIZE)
            ),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])


    def _load_model(self):

        model = models.efficientnet_b0(
            weights=None
        )

        features = model.classifier[1].in_features

        model.classifier[1] = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(
                features,
                len(CLASS_NAMES)
            )
        )


        state = torch.load(
            MODEL_PATH,
            map_location=self.device
        )

        model.load_state_dict(state)

        model.to(self.device)
        model.eval()

        return model



    def predict(self, image_path):

        image = Image.open(
            image_path
        ).convert("RGB")


        tensor = self.transform(image)
        tensor = tensor.unsqueeze(0)
        tensor = tensor.to(self.device)


        with torch.no_grad():

            output = self.model(tensor)

            prediction = torch.argmax(
                output,
                dim=1
            )


        result = CLASS_NAMES[
            prediction.item()
        ]

        return result, image