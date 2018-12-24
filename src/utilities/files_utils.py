import zipfile

class FilesUtils:

    @staticmethod
    def unzip(source,target_dir):
        with zipfile.ZipFile(source,"r") as zip_ref:
            zip_ref.extractall(target_dir)

