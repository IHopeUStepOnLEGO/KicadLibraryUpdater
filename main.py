from kicadUpdater.LibraryUpdater import *
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
    #updater.loadLibrariesFromConfig(os.path.join(os.getcwd(), "kicadUpdater\\config\\updaterConfig2.json"))

    '''
    update local libraries though git
    '''
    #updater.updateByKey("modules\\packages3d")
    #updater.updateByKey("library")
    #updater.updateAll()

if __name__ == '__main__':
    main()
