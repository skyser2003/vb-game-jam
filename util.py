import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')
def dataPath(filename):
    return os.path.join(data_dir, filename)
