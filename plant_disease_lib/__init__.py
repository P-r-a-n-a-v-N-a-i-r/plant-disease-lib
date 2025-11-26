import os
from typing import Dict, Any, Optional

from PIL import Image
import numpy as np
import pandas as pd
import torch
import torchvision.transforms.functional as TF

from .CNN import CNN

class PlantDiseasePredictor:
    def __init__(
        self,
        model_path: str,
        disease_csv_path: str,
        supplement_csv_path: str,
        num_classes: int = 39,
        device: Optional[str] = None,
    ) -> None:
        self.model_path = model_path
        self.disease_csv_path = disease_csv_path
        self.supplement_csv_path = supplement_csv_path
        self.num_classes = num_classes

        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        self.disease_info = pd.read_csv(self.disease_csv_path, encoding="cp1252")
        self.supplement_info = pd.read_csv(self.supplement_csv_path, encoding="cp1252")

        self.model = CNN.CNN(self.num_classes)
        state_dict = torch.load(self.model_path, map_location=self.device)
        self.model.load_state_dict(state_dict)
        self.model.eval()
        self.model.to(self.device)

    def _prepare_image_tensor(self, image_path: str) -> torch.Tensor:
        image = Image.open(image_path).convert("RGB")
        image = image.resize((224, 224))
        input_data = TF.to_tensor(image)
        input_data = input_data.view((-1, 3, 224, 224))
        return input_data.to(self.device)

    def predict_index(self, image_path: str) -> int:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        input_tensor = self._prepare_image_tensor(image_path)

        with torch.no_grad():
            output = self.model(input_tensor)
            output_np = output.cpu().numpy()
        index = int(np.argmax(output_np))
        return index

    def predict_with_metadata(self, image_path: str) -> Dict[str, Any]:
        idx = self.predict_index(image_path)
        return self.predict_with_metadata_by_index(idx)

    def predict_with_metadata_by_index(self, idx: int) -> Dict[str, Any]:
        # Defensive: If idx is out of bounds
        if idx < 0 or idx >= len(self.disease_info):
            idx = 0
        title = self.disease_info["disease_name"][idx]
        description = self.disease_info["description"][idx]
        prevent = self.disease_info["Possible Steps"][idx]
        image_url = self.disease_info["image_url"][idx]
        supplement_name = self.supplement_info["supplement name"][idx]
        supplement_image_url = self.supplement_info["supplement image"][idx]
        supplement_buy_link = self.supplement_info["buy link"][idx]

        return {
            "index": idx,
            "disease_title": title,
            "description": description,
            "prevent": prevent,
            "image_url": image_url,
            "supplement_name": supplement_name,
            "supplement_image_url": supplement_image_url,
            "supplement_buy_link": supplement_buy_link,
        }

    def get_market_data(self) -> Dict[str, list]:
        return {
            "supplement_image": list(self.supplement_info["supplement image"]),
            "supplement_name": list(self.supplement_info["supplement name"]),
            "disease": list(self.disease_info["disease_name"]),
            "buy": list(self.supplement_info["buy link"]),
        }
