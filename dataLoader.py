import torch
import os
from torch.utils.data import DataLoader, Dataset
import pandas as pd
import numpy as np
from PIL import Image
from skimage import io, transform
import matplotlib.pyplot as plt
from skimage.transform import rotate, AffineTransform, warp

class data(Dataset):
    # construct dataset
    def __init__(self, csvFile, root, transform = None):
        self.transform = transform
        self.root = root
        self.CT = pd.read_csv(csvFile)
    
    # dataset length
    def __len__(self):
        return len(self.CT)
    
    # indexing
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

	# image
        img_Name = os.path.join(self.root, self.CT.iloc[idx,1])
        img = Image.open(img_Name).convert('L')
        cS = self.CT.iloc[idx,3]

        if self.transform:
            img = self.transform(img)
	
        return (img, cS)

class EngineeredData(Dataset):
	# construct dataset
    def __init__(self, csvFile, root, transform = None, op):
        self.transform = transform
        self.root = root
        self.CT = pd.read_csv(csvFile)
	self.op = op
    
    # dataset length
    def __len__(self):
        return len(self.CT)
    
    # indexing
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

	# image
        img_Name = os.path.join(self.root, self.CT.iloc[idx,1])
        img = Image.open(img_Name).convert('L')
        cS = self.CT.iloc[idx,3]
	if op == 1:
		img = np.flipud(img)
	elif op == 2:
		seed(1)
		a = (random()) * 300
		img = rotate(img, angle=a, mode = 'wrap')

        if self.transform:
            img = self.transform(img)
	
        return (img, cS)
