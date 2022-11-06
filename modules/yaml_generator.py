# import required module
import os
import random

def audiofile_catalog(directory, txt_dir):
    """
     Generates yaml formatted text for automatically constructing the subjective test pages
    """
# iterate over files in that directory
    for filename in os.listdir(directory):
        subdir = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isdir(subdir):
            foldername=subdir.split(".")[0][-2:]
            with open(f'{os.path.join(txt_dir, foldername)}.txt', 'w') as f:
                for audioname in os.listdir(subdir):
                    g = os.path.join(subdir, audioname)
                    f.write(foldername +"_" + g.split("\\")[-1] +": " +  "\\".join(g.split("\\")[-4:]) + "\n")
                    # print(g.split("\\")[-1] +": " +  "\\".join(g.split("\\")[-4:]))


def txt_randomizer(directory):
    """
    randomizar el orden de las lineas
    """
    for filename in os.listdir(directory):
        txt_name = os.path.join(directory, filename)
        if os.path.isfile(txt_name):
            lines = open(txt_name).readlines()
            random.shuffle(lines)
            open(txt_name, 'w').writelines(lines)
# 

# for filename in os.listdir(directory):
#     txt_name = os.path.join(directory, filename)
#     if os.path.isfile(txt_name):
#         lines = open(txt_name).readlines()
#         open("test", 'w').writelines(lines)


if __name__ == "__main__":
    
    # assign directory
    directory = r'subjective_test\webmushra\configs\resources'
    txt_dir = "txt_dir"
    audiofile_catalog(directory, txt_dir)

    # randomize lines in txts
    directory2 = 'txt_dir'
    txt_randomizer(directory2)