import os
import numpy as np
import torch
from pathlib import Path


class Model:
    app_dir = Path(os.getcwd())
    model_path = app_dir.joinpath('app').joinpath('models').joinpath('nn_model.pt')
    model = torch.load(model_path)

    def get_predictions(self, imgs):
        imgs = torch.Tensor(imgs)
        with torch.no_grad():
            pred = torch.exp(self.model(imgs))
        return [np.argmax(i).tolist() for i in pred]
