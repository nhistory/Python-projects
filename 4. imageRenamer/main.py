import os, pathlib



def main():
    # change the working directory to /images in the project folder
    os.chdir('./images')
    # get the current working directory now
    cwd = os.getcwd()
    # get a list of all the filenames of files in the working directory (/images)
    filenames = os.listdir(cwd)
    # sort the list so image files names are alphabetical
    filenames.sort()

    # testing list of filenames
    # print(filenames)

    # add challenge solution here
    pngFileNames = []
    for filename in filenames:
        extension = pathlib.Path(filename).suffix
        if (extension == ".png"):
            pngFileNames.append(filename)

    # print(pngFileNames)

    for i in range(0, len(pngFileNames)):
        os.rename(pngFileNames[i], "tech"+str(i+1)+".png")


main()