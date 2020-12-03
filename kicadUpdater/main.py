#from kicadUpdater.LibraryUpdater import *
from LibraryUpdater import *
from os import getcwd

def main():
    updater = LibraryUpdater()

    '''
    add and remove libraries to JSON config file
    '''
    #updater.addLibraryToConfig(os.path.join(os.getcwd(), "kicadUpdater\\config\\updaterConfig.json"), "lablib", "asdff")
    #updater.delLibraryFromConfig(os.path.join(os.getcwd(), "kicadUpdater\\config\\updaterConfig.json"), "lablib")

    '''
    load libraries from JSON file
    '''
    try:
        updater.loadLibrariesFromConfig(os.path.join(os.getcwd(), "kicadUpdater\\config\\updaterConfig.json"))
    except:
        updater.loadLibrariesFromConfig(os.path.join(os.getcwd(), "kicadUpdater\\config\\updaterConfig.json"))


    '''
    update local libraries though git
    '''
    #updater.updateByKey("modules\\packages3d")
    updater.updateByKey("library")
    updater.updateByKey("modules")
    #updater.updateByKey("modules\\packages3d")
    updater.updateByKey("templates")
    #updater.updateAll()

if __name__ == '__main__':
    main()
