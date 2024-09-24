# HW-1: Workflow scripting 

**Title**:  Automating Data Processing and Quarto Website Deployment with Python and Bash
**Author(s)**: Dr. H and Gerrard Pendleton Thurston the 4th

This assignment aims to develop proficiency in automating data processing tasks and deploying a static Quarto website using Python and Bash scripting. By the end of this assignment, you should be able to create a fully automated workflow that processes image data, generates insights, and deploys a Quarto-based static website to a remote server.

# Assignment 

## General comments

* Various steps outlined below are not representative of an optimal workflow. There are superfluous processing steps, and some workflow design choices are suboptimal. For example, some scripts could be consolidated into a larger, more efficient script. However, we intentionally designed it this way to ensure you complete specific tasks for educational purposes.

* `Windows users`: If using windows, it is required that you install WSL and do the assignment inside the linux-subsystem, you will not be able to complete the assignment otherwise. 

* `Mandatory`: Use Object oriented programming (OOP) paradigm to the largest extent possible. i.e. utilize classes and objects as the default choice for structuring your code.

## Create a script to sync to GitHub

This project uses Github classroom, please create a Github account, if you don't have one already. 

After accepting the assignment, clone the repo to your laptop using `git clone` from the command line

If you have not done so, run the following commands

`git config --global user.email "you@example.com"`
`git config --global user.name "Your Name"`

Next, create a script in `submission/scripts/git.sh` that does the following

* `git pull`
* `git add` 
* `git commit` 
* `git push` 

Please add the `data` folder to your git `.gitignore` file so it isn't synced to the cloud. 

Remember, to make a shell-script executable, use `chmod +x git.sh`, after that you can run it by navigating to the folder `cd path_to_folder_with_script` and the executing the script using `./git.sh`

Note that the `.git` folder is two levels above the folder `submission`, you can see this by running `ls -a ../../` from inside `submission/scripts`, however, the script `git.sh` should still work even though it is in a sub-directory of the parent `.git` folder.

You can wrap this in an Bash `if statement` if you want, here is some starter code for `git.sh`

```
printf 'Would you like to sync with the github server: (y/n)?'
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then 

    # PULL CLOUD REPO TO LOCAL
    git pull 
    
    # change buffer settings 
    git config http.postBuffer 524288000

    # SYNC TO LOCAL REPO TO CLOUD 
    read -p 'ENTER MESSAGE: ' message
    echo "commit message = "$message; 
    
    # ADD CHANGES TO QUEUE
    git add ../../; 
    
    # MAIN BRANCH
    git commit -m "$message"; 

    # PUSH NON-MAIN BRANCH
    # git push  -u origin branch_name

    # PUSH MAIN BRANCH
    git push

else
    echo NOT SYNCING TO GITHUB!
fi
```

`IMPORTANT:` Remember to run `git.sh` script regularly to back-up your work to `github`, part of your grade will be based on your use of Github and your commit frequency.

## Data

In the provided `data` folder are a few images of cats and dogs 

**DO NOT** edit or change any files in the `data` folder. This is your original "raw data", you generally should NOT change raw data in a workflow. Since it can lead to errors, loss of original data integrity, and hinder reproducibility. It also makes tracking changes difficult, complicates audits, and can introduce biases. Instead, always preserve raw data and apply transformations separately.

```
(base) james@Jamess-MBP HW-1-solution % tree data 
data
├── IMG_0013.jpeg
├── IMG_1486.jpeg
├── IMG_1700.jpeg
├── IMG_3071.jpeg
├── IMG_4033.jpeg
├── IMG_4186.jpeg
├── IMG_4272.jpeg
├── IMG_4799.jpeg
├── IMG_4812.jpeg
├── IMG_4950.JPG
├── IMG_5144.jpeg
├── IMG_5652.jpeg
├── IMG_6018.jpeg
├── IMG_6024.jpeg
└── luna.png
```

Note the use of the `tree` command, it is a useful unix command for visualizing a directory tree in the terminal.

Please `DO NOT` deviate from the directory tree structure provided with the assignment.

## Create a Runner file

* A runner file in a pipeline coordinates the execution of various tasks or scripts in a specified order, ensuring smooth workflow automation. They are commonly named `run.sh`, `main.py`, `pipeline.py`, or `runner.py`.
* Build out the workflow below in `submission/run.sh` 
* The runner file should do the following 
  * save the original path of the script location for later use
    * `script_path=${PWD}`
  * run `git pull` (just to be safe)
  * navigate to `submissions/pixify`
  * build the package
  * navigate back to `$script_path` via `cd $script_path`
  * navigate to `submissions/scripts`
  * run `scripts/process.py` 
  * navigate back to `$script_path` via `cd $script_path`
  * Run the `tree` command and pipe the output using `>` and `>>` into `website/pages/tree.qmd` for inclusion in your website.
    * you may need to install "tree" with `brew` or `apt-get`
  * navigate to `website` folder
  * run `website/build-and-deploy.sh`
  * navigate to `scripts` folder
  * run `git.sh` 
  * create a `.zip` compression of your `submission` and re-names it `HW1-netid.zip`
  * Note: you can navigate around the directory tree into different current working directories as needed

## Create a Package

Create a python package named `pixify` in `submission/pixify` (see reference above)

A skeleton of the package is included for you, you can install it locally using

```
cd pixify
ls
pip install -e .
```

Using the `-e` flag will make it so that any changes made to the source files in `pixify/pixify` will immediately be reflected in the scripts that use `import pixify` on your system. This makes development easier. However, if using `.ipynb` you `MUST restart the kernel` for the changes to take effect. 

### core.py

Do the following in the file `submission/pixify/pixify/core.py`

You will develop a Python class to handle image processing tasks such as gray-scale conversion, resizing, rotating, and visualizing image transformations. Additionally, you'll compute gradients of the image and generate a surface plot for an image, automatically logging the operations in a transformation report which will automatically be included in your website.

* Create a class called "Image" in `pixify/pixify/core.py` that stores and processes an image object
* Please store the images as `torch tensors`, so you inherit functionality from `torch vision` .	
* Your class should have the following functionality 

**Image Class overview**:
   - Create a Python class named `Image` that will handle the following functionalities:
     - Load an image from a file path or as a tensor.
     - Store a copy of the original image and its path as attributes of the class objects.
     - Store a version of the image that can undergo transformations (grayscale, resize, rotation, etc.).

1. **Image Loading**:
   - Implement the constructor (`__init__`) of the class to:
     - Accept an input that can either be an image file path (as a string) or a tensor.
     - Attempt to read the image using `torchvision.io.read_image` if a file path is provided. 
     - If it's a tensor, ensure it is a valid image tensor.
     - Log warnings in case of invalid inputs.

2. **Display the Image**:
   - Write a method `show()` that visualizes the current state of the image using `matplotlib`. 
   - The image should be converted from a tensor to a NumPy array for plotting.

3. **Transformations**:
   - Implement the following transformation `class methods` as part of the class:
     - `grayscale()`: Convert the image to grayscale using `torchvision.transforms.Grayscale`.
     - `resize(h, w)`: Resize the image to a given height `h` and width `w` using `torchvision.transforms.Resize`.
     - `rotate(theta)`: Rotate the image by `theta` degrees using `torchvision.transforms.functional.rotate`.
   - These functions should keep track of all transformations applied to the image in a log string, `self.transform_log`.

4. **Generate a Transformation Report**:
   - Implement a `class method` `report()` that uses a template to generate a report of all the transformations applied to the image. This report should include:
     - Original and transformed image paths and shapes.
     - A detailed log of the transformations performed.
     - Recommended that you use `from string import Template` for this

5. **Surface Plot**:
   - Write a method `surface_plot(out_path="tmp.png", show=False)` to generate a 3D surface plot of the image's pixel intensity values using `matplotlib`. 
   - Save it to a location in the `website` folder for later inclusion in the `quarto website`.

6. **Gradient Computation**:
   - Implement the method `compute_gradient(out_path="tmp.png", show=False)`:
     - Compute the gradients in the x and y directions using finite differences (i.e., manually compute the difference between neighboring pixels in a for loop).
     - Calculate the gradient magnitude and display it using `matplotlib`.
     - Save it using `out_path` in the `website` folder for later inclusion in the `quarto website`.

7. **Save the Transformed Image**:
   - Write a method `save(output_path)` that saves the current state of the transformed image to a file using `torchvision.transforms.ToPILImage()` and `PIL.Image.save()`.
   - Save the transformed image to a location in the `website` folder for later inclusion in the `quarto website`.

### utilities.py 

Do the following in the file `submission/pixify/pixify/utilities.py`

1. **Function 1: Overwrite Folder**
   - Create a function that takes a folder_path as input.
   - Check if the folder exists and whether it's a directory.
   - If the folder exists, delete the folder and all its contents.
   - After checking (and potentially deleting), create a new folder at the specified path.

2. **Function 2: Write to File**
   - Create a function that takes a string, a file path, and an optional boolean flag (for overwriting).
   - The function should open a specified file and write the string to it.
   - If the `overwrite` flag is set to `True`, the function should overwrite the file's contents.
   - If the `overwrite` flag is `False`, the function should append the string to the existing contents of the file.

## Process

In the file `scripts/process.py`, do the following  

Start by Importing the package you created in `submission/pixify` via `import pixify as px`

1. **Create Output Folders:**
   - use the `utilities.py` function to create two output folders:
     - One for storing the original images.
       - `../website/original-images`
     - Another for storing the transformed images.
       - `../website/transformed-images`
   - Use the helper function to ensure that these folders are created anew each time the program runs, overwriting any existing folders.

2. **Initialize a Log File:**
   - Create a log file where you will record information about the image processing steps.
     - `../website/pages/processing-log.qmd`
   - Begin the log file with a markdown header (e.g., "# Preprocessing log").
   - Ensure the log file is deleted and initialized each time the program is run.

3. **Process Images:**
   - Loop through the images stored in the folder `../../data/`
   - For each image:
     - load it, and use it to create an object of your `pixify` class
     - Copy the original image to the website folder for later show-casing
   
4. **Apply Transformations:**
   - Apply the following transformations to each image:
     - Convert the image to grayscale.
     - Resize the image to 100x100 pixels.
     - Rotate the image by -90 degrees.
  - Use appropriate functions from the `pixify` library to perform these transformations.

5. **Save Transformed Images:**
   - For each transformed image, save the following to the website for later showcasing:
     - The transformed image
     - A surface plot of the image.
     - A gradient plot of the image.
     - The final transformed image itself.
   - Save each result with a specific naming convention using zero-padded numbers (e.g., `website/transformed-images/0001-surface.png`, `website/transformed-images/0001-grad.png`, `website/transformed-images/0001.png`).

6. **Log the Processing:**
   - After processing each image, generate a report for that image using the `pixify` library and append it to the log file.
   - Note: the code `process.py` should programmatically generate the file `website/pages/processing-log.qmd` 
     - this file should be completely programmatically generated every time `process.py` is run
     - `website/pages/processing-log.qmd` should include 
       - Header with the original image name, e.g. `## image012.jpeg`
       - The original image embedded in the webpage with `![]()`
       - The text report of the transformation log for that image
       - The final transformed image embedded in the webpage with `![]()`
       - A surface plot of the image embedded in the webpage with `![]()`
       - A vector field image of the image's gradient function embedded in the webpage with `![]()`
       - A heat-map image of the magnitude of the image's gradient field embedded in the webpage with `![]()`
     - Again, the file `website/pages/processing-log.qmd` should be entirely generated by the program (i.e. should require no human editing)

7. **Increment the File Counter:**
   - Ensure that each processed image is numbered sequentially in the output files.

- Your program should handle errors, such as missing images or incorrect file paths, gracefully.

## Website 

Create a Quarto website to show case your assignment results.

An example partially complete version of this website is be provided to you with the assignment, the website is missing the gradient field image and the gradient magnitude image (see above). 

##  build-and-deploy.sh

In this sub-assignment, you will automate the process of building and cleaning up a Quarto website project using a series of shell commands. The tasks involve removing temporary files, rendering a website,  setting file permissions correctly, and pushing the website to the server.

Write a script `website/build-and-deploy.sh` that does the following

1. **Clean-Up Step:**
   - Write a command to remove any existing build of the website by deleting the `_site` directory and all its contents.
   - This ensures that you are starting with a clean build every time.

2. **Build the Website:**
   - Use a command to render the website using the `quarto render` command.
   - This command should compile the website files into the `_site` directory.

3. **Remove Unnecessary Files:** (optional, for MacOs users only)
   - After building the website, navigate to the `_site` directory.
   - Search for and delete all `.DS_Store` files that may have been created. These files are unnecessary and should be removed.
   - Once done, return to the original directory.

4. **Set Correct File Permissions:**
   - Using `for loops` and the `find` command, Set the correct permissions for all files and directories within the `_site` directory:
     - For files, set the permissions to `644`, which allows the owner to read and write, and others to read.
     - For directories, set the permissions to `755`, which allows the owner to read, write, and execute, while others can read and execute.
   - Use the `chmod` command to change permissions for both files and directories within the `_site` folder.

5. **Prompt the User to Push the Website:**
   - After cleaning and setting permissions, prompt the user to decide whether to push the website to your Georgetown University (GU) domains folder.
   - If the user types $y$ or $Y$, proceed with pushing the website using the `rsync` command.
   - If the user types n or N , skip the deployment step and display a message.
     - Hints:
       - Use the read command to capture the user's input.
       - Use a conditional statement ( if ) to check the user's input and determine whether to push the website.

6. **Push the Website to the Remote Server:**
   - If the user opts to push the website, use the rsync command to synchronize the contents of the _site folder with a remote server.
   - Ensure that any files no longer in the local _site folder are deleted from the remote server.

# Submission

Please submit the following to Canvas

* The URL to your Github classroom assignment in the text box
  * This will be used for grading git-hub usage
  * This will also be the version of the code that is graded
* A compressed version of your submission named `HW1-netID.zip` where `netID` is your GU netID, for example `HW1-jh2343.zip`
DO NOT include the data folder 
  * The compressed folder is required, but it is largely a formality, to have a timestamped and static version of your submission
