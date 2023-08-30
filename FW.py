"""
file watcher module contain Watcher class, this class read .yml configuration file to get folder path.
This folder will be monitor, if there is any change in folder i.e file added to the folder this newly added file will
collect and return.

"""

import os
import time
# import yaml


class Watcher:

    def __init__(self):
        """
        Watcher class initialisation config.yml file will read and folder will get.
        """
        with open( "E:\Yadnesh\Demo TaskFile","r") as ymlfile:
            try:
                cfg = yaml.safe_load(ymlfile)
                config = cfg['filepath']
            except yaml.YAMLError as exc:
                print(exc)

        self._cached_stamp = 0
        self.folder = config['folder']

    def look(self):
        """
        This method monitor the folder location to check if any file is added or change.

        :return: list of file names.
        """
        stamp = os.stat(self.folder).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            return self.file_collector()
            # File has changed, so do something...

    def file_collector(self):
        """
        file_collector return list of names from folder location.

        :return: list of file names
        """
        return os.listdir(self.folder)


if __name__ == "__main__":
    W = Watcher()
    while True:
        W.look()
        time.sleep(5)
