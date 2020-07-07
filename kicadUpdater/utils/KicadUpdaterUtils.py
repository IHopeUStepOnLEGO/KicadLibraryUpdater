import git
import os
import sys

# error handler for shutil.rmtree
def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
        # is the error an access error?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        sys.exit()

class Progress(git.remote.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        message = str(int(round(((cur_count/ max_count)*100), 0))) + "%"
        print('update(%s, files:(%s/%s) - (%s)'%(op_code, int(cur_count), int(max_count), message))
        