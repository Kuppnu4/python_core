from setuptools import setup

setup(name = 'clean_folder',
      version = '1',
      description = 'clean folder application',
      url = 'https://github.com/Kuppnu4/python_core/blob/master/modul_6/HomeWork/sort.py',
      author = 'Aleksandr Voitushenko',
      author_email = 'aleksandr.voitushenko@gmail.com',
      license = 'MIT',
      packages = ['clean_folder'],
      entry_points = {'console_scripts': ['clean-folder = clean_folder.clean:clean_report']     
          }
    )
