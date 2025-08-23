def file_exists(path):
    """
    Checks if a file exists at the given DBFS path.
    Returns True if it exists, otherwise False.
    """
    try:
        dbutils.fs.ls(path)
        return True
    except:
        return False