import os

auto_remove =[ 
    '__pycache__',
]
import glob
location = input('Enter the location of your django project :')

for filename in glob.iglob(location + '**/**', recursive=True):
    print(filename)
    if str(filename).endswith('.pyc') and '__pycache__' in str(filename):
        os.remove(filename)
    if str(filename).endswith('migrations\\'):
        files = glob.glob(filename)
        for file in files:
            os.remove(file)
        
        if not os.path.exists(filename+'__init__.py'):
            with open(os.path.join(filename,'__init__.py'),'w') as f:
                pass
            f.close()
            print("__init__.py created, since it didn't exist..")
        else:
            print('init already exists')