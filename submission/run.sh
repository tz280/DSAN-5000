
script_path=${PWD}
echo $script_path

# pull repo
git pull

# build pixel package (don't really need to do this each time due to -e flag, but inlcude anyway)
cd pixify
ls
pip install -e .
cd $script_path  #go back to folder with `run.sh` in it 


# tree part 
# save output path as shell variable 
# file="website/pages/tree.qmd"
# echo '# Directory Tree' > $file
# echo '' >> $file
# echo 'Below we see the final directory tree for out project' >> $file


# COMPLETE THE REST HERE
cd submission/scripts
python3 process.py  
cd $script_path 

file="website/pages/tree.qmd"
echo '# Directory Tree' > $file
echo '' >> $file
echo 'Below we see the final directory tree for our project' >> $file
echo '' >> $file
tree >> $file 

tree > website/pages/tree.qmd

cd website
./build-and-deploy.sh

cd ../submission/scripts
./git.sh

cd $script_path
zip -r HW1-tz280.zip submission

