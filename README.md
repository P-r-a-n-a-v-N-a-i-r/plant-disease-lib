# plant_disease_lib

A Python library for plant disease detection using deep learning (CNN) and supplementary treatment information.

## Features

- Predict plant disease from leaf images using deep learning models
- Return disease name, description, treatment/prevention steps, and recommended supplements
- CSV-based metadata lookup for diseases and supplements
- Torch-based model loading and inference
- Easily extensible for new disease classes and models

## Installation

Install via pip once released on PyPI:

pip install plant_disease_lib

Or clone the repository:

git clone https://github.com/P-r-a-n-a-v-N-a-i-r/plant-disease-lib.git
cd plant-disease-lib
pip install -e .

## Usage

from plant_disease_lib import PlantDiseasePredictor

predictor = PlantDiseasePredictor(
model_path='models/cnn_model.pth',
disease_csv_path='data/disease_info.csv',
supplement_csv_path='data/supplement_info.csv',
num_classes=39
)

result = predictor.predict_with_metadata('test_image.jpg')
print(result)

Example `result` output:
{
"index": 12,
"disease_title": "Tomato Early Blight",
"description": "...",
"prevent": "...",
"image_url": "...",
"supplement_name": "...",
"supplement_image_url": "...",
"supplement_buy_link": "https://example.com"
}