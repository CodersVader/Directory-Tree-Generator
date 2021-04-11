
class Tree:

    """
    Tree object contain data to visualize directory structures.

    Parameters
    ----------

    path : object

        object of type path generated using pathlib module.

    Attributes
    ----------

    depth : int

        counter to keep track of folder depth.

    output : str

        String that contains generated directory structure

    """

    depth = 0
    output = ''

    def __init__(self, path):
        self.path = path


    @staticmethod
    def list_folder_files(folder_path):

        """
        Generates two lists containing sub folder paths and file names.

        Parameters
        ----------
        folder_path : object

            path to folder.

        Returns
        -------

        fodlers : list

            list containing path to all sub folders.

        files : list

            list containing all the files in that folder.

        """

        folders = []
        files = []

        for each_item in folder_path.iterdir():
            if each_item.is_dir():
                folders.append(each_item)
            else:
                files.append(each_item.name)

        return folders, files

    def tree_generator(self, fpath=None):

        """
        Recursively generates the directory structure
        and stores it in output variable

        Parameters
        ----------
        fpath : object

            By default None but instansiated to root folder path in first iteration
            and supplied sub folder path in each next iteration.

        """

        global depth
        global output
        BLANK = "   "
        OUTER = "│  "
        INNER = "├──"
        ENDING = "└──"

        if fpath is None:
            fpath = self.path

        folders, files = self.list_folder_files(fpath)
        Tree.depth += 1
        padding = BLANK + OUTER * (self.depth - 1)

        for each_folder in folders:
            Tree.output += padding + INNER + each_folder.name + '\n'
            self.tree_generator(each_folder)
        else:
            for each_file in files:
                if each_file == files[-1]:
                    Tree.output += padding + ENDING + each_file + '\n'
                else:
                    Tree.output += padding + INNER + each_file + '\n'

        Tree.depth -= 1

    def to_cli(self):

        """
        prints the generated structure to command line.
        """

        print(self.path.name)
        print(Tree.output)

    def to_file(self, ):

        """
        creates a text file containing the generated file structure.
        name of file is root folder name.
        """

        with open(self.path.name + '.txt', 'w', encoding="utf-8") as file:
            file.write(self.path.name + '\n')
            file.write(Tree.output)
