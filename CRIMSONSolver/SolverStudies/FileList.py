import os

__author__ = 'rk13'

# [AJM] Note that this pattern is a bit deceptive.
#       Just because a file was opened in the past doesn't mean that it still exists or we have access to it,
#       I think I would rather limit the time that we hold files open and just pass around file paths until 
#       the last possible moment. I'm not a fan of stateful directory interfaces, they're not very robust and
#       they don't give an accurate picture of what the filesystem is really like.
#
#       The other issue with this is that callers to this class might not be prepared or able to create good quality
#       error messages if for some reason file I/O fails (which it always can).
#       e.g., in an error message can a caller say *which file* failed to open, or what the context of that file is? Probably not.
#
#       It also doesn't seem in good taste for __getitem__ ("operator[]") to ever be able to throw exceptions other than "key not found".
#
#       To me it's also counter-intuitive that __getitem__ is meant to be used with files that don't actually exist,
#       when I see fileList['someFile.txt'] and someFile.txt doesn't exist, that looks like a crash condition to me.
#
#       I'm not sure there's much value added in this pattern of having 8 different functions append a few lines to the.supre either,
#       I would have preferred it if a function just returned a string containing its part, and then write the whole
#       giant string at once. With this system you have to keep a virtual "cursor position" in the file in your head at all timeS,
#       and also a "directory state" of what files should be in a directory at a certain time in the execution.
#
#       The other problem is, if there's a failure somewhere in a "file nibbling" setup like this, you'll have a half written 
#       output file.
"""
    A class representing a list of files in a folder.
    Among other things, this allows you to open a file multiple times in different functions and continue to append to it.
"""
class FileList(object):
    def __init__(self, folder):
        self.folder = folder
        self.openFiles = {}

    """
        Will open the file you specify, the file must be in the folder you specified in the constructor.
        Note that this file *need not actually exist* at the time of calling, this fileList is not a listing
        of the directory at some point in time, it's just a (stateful) interface to the directory.
        
        Depending on the open mode it might be created by this call.

        Parameters:
            openFileInfo:
                    an array, [fileName, openMode]
                or
                    the fileName, and openMode will be just 'wt'
                    (why didn't we just use default parameters?)
        Throws: 
            Any exception caused by open if this file isn't already open (!)
    """
    def __getitem__(self, openFileInfo):
        if isinstance(openFileInfo, tuple):
            name = openFileInfo[0]
            openmode = openFileInfo[1]
        else:
            name = openFileInfo
            openmode = 'wt'

        if name not in self.openFiles:
            self.openFiles[name] = open(os.path.join(self.folder, name), openmode)
        return self.openFiles[name]

    def isOpen(self, fileName):
        return self.openFiles.__contains__(fileName)

    def close(self):
        for _, f in self.openFiles.iteritems():
            f.close()