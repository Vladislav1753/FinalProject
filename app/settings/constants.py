import os

DATA_FOLDER = 'data'
DATA = os.path.abspath(os.path.join(DATA_FOLDER, 'healthcare-dataset-stroke-data.csv'))

SAVED_ESTIMATOR = r'C:\Python\final\app\models\LogisticRegression.pickle'

print(DATA)

'''
import os

DATA_FOLDER = os.path.dirname(os.path.dirname(__file__))


def get_full_path(*path):
    return os.path.join(DATA_FOLDER, *path)


DATA = get_full_path('data', 'healthcare-dataset-stroke-data.csv')
SAVED_ESTIMATOR = get_full_path('models', 'LogisticRegression.pickle')
'''