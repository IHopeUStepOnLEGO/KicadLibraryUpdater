import shutil
import git
from git import Repo
import sys
import json


from utils.KicadUpdaterUtils import *

class LibraryUpdater():
    
    def __init__(self, repo_dir=""):

        # container for all libraries
        self.gitDict = {}

        # check if directory is specified
        if(repo_dir == ""):
            # if not, use same directory as this script
            self.repo_dir = os.path.abspath(os.curdir)
            os.chdir('..')
            self.repo_dir = os.path.abspath(os.curdir)
            print(self.repo_dir)
        else:
            # if specified, use given directory path
            self.repo_dir = repo_dir


    def updateByKey(self, key):
        if key in self.gitDict:
            self.prepareLocalFS(key, self.repo_dir)
            try:
                git.Repo.clone_from(
                    self.gitDict[key], 
                    os.path.join(self.repo_dir, key), 
                    branch="master", progress=Progress()
                )
                #print("updating of \"%s\" successful!" % str(key))
                print('updating of "%s" was  successful!' % str(key))
            except:
                print('updating of "%s" has failed!' % str(key))
        else:
            print("%s key was not found or invalid!")
            sys.exit()

    def updateAll(self):
        for key, value in self.gitDict.items():
            self.updateByKey(key)

    def prepareLocalFS(self, folderName, directory):
        print("checking for folder \"" + folderName +
              "\" in directory: \"" + directory + " ...")

        # if folder already exists, remove folder
        if(os.path.isdir(folderName)):
            print("folder \"" + folderName + "\" found! deleting ...")
            shutil.rmtree(folderName, onerror=onerror)

        print("updating: " + folderName + " ...")

    # load libraries from json file in config folder
    def loadLibrariesFromConfig(self, path_to_config):
        try:
            with open(os.path.join(path_to_config)) as f:
                # open json and save in class variable
                self.gitDict = json.load(f)["libraries"]
                # also save path to config file as variable
                self.configPath = path_to_config
        except IOError as e:
            print("Error occured reading file ... %s" % e)
            

    # add an custom library to config
    def addLibraryToConfig(self, path_to_config, libName, libUrl):
        try:
            with open(os.path.join(path_to_config), 'r+', encoding='utf-8') as f:

                # create temporary dict
                temp = json.load(f)

                temp["libraries"][str(libName)] = str(libUrl)
                    
                # move cursor to beginning of json
                f.seek(0)
                # begin writeing new json data
                json.dump(temp,f)
                # delete any old data exceeding the new one
                f.truncate()

                # close file
                f.close()

        except IOError as e:
            print("Error occured reading file ... %s" % e)
            

    def delLibraryFromConfig(self, path_to_config, libName):
        try:
            with open(os.path.join(path_to_config), 'r+', encoding='utf-8') as f:

                # create temporary dict
                temp = json.load(f)

                # if key is present, delete
                if(str(libName) in temp["libraries"]):
                    temp["libraries"].pop(str(libName), None)

                    print("library: \"" + libName + "\" from \"" + path_to_config + "\"successfully deleted!")
                    # move cursor to beginning of json
                    f.seek(0)
                    # begin writeing new json data
                    json.dump(temp,f)
                    # delete any old data exceeding the new one
                    f.truncate()

                    # close file
                    f.close()
                else:
                    print("library: \"" + libName + "\" was not found in \"" + path_to_config + "\"!")

        except IOError as e:
            print("Error occured reading file ... %s" % e)
            f.close()