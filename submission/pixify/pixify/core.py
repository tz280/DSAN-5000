import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from torchvision.io import read_image
import os
from torchvision import transforms
import torchvision.transforms.functional as F
from string import Template

class Image:


    #INITIALIZE
    def __init__(self, input):

        # input can either be a path to an image in a string 
        # or a torch tensor representation of an image
        self.path=""
        if isinstance(input, str):
            try:
                #keep a copy of the original
                print("complete me")
                # self.original_tensor = ?
                # self.original_path = ?
            except:
                print("WARNING: unable to read image: "+input)
        elif torch.is_tensor(input)==True:
            print("complete me")
        else:
            print("WARNING: unacceptable input type")\
        
        # version of self that can be transformed and changed
        self.tensor=self.original_tensor
        # self.path=?
        self.transform_log=""

    def show(self):
        # To visualize the image using matplotlib
        # Convert image tensor to numpy array for plotting
        image_np = self.tensor.permute(1, 2, 0).numpy()
        plt.imshow(image_np)
        plt.axis('off')  # Hide axis
        plt.show()


#   SURFACE PLOT
    def surface_plot(self,out_path="tmp.png",show=True):

        # Permute the dimensions of the tensor to rearrange it from (C, H, W) to (H, W, C)
        # where C is the number of channels, and convert it to a NumPy array
        image = self.tensor.permute(1, 2, 0).numpy()
        
        # Print the shape of the image for debugging or checking dimensions
        # print(image.shape)
        
        # Create a meshgrid of coordinates (xx, yy) for the pixel positions on the image grid
        xx, yy = np.mgrid[0:image.shape[0], 0:image.shape[1]]
        
        # Create a figure for the 3D plot
        fig = plt.figure()
        
        # Add a 3D subplot to the figure, using 3D projection
        ax = fig.add_subplot(projection='3d')
        
        # Plot a 3D surface for the first channel of the image (grayscale or one color channel)
        # rstride and cstride define the step size for row and column
        ax.plot_surface(xx, yy, image[:, :, 0], rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)
        
        # If 'show' is True, display the plot
        if show: plt.show()
        
        # Save the plot to the specified output path
        plt.savefig(out_path)

