import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.VTDivorce',
      version='1.3.2',
      description=('Fill out initial forms to get a divorce, separation or civil union dissolution in Vermont'),
      long_description='# docassemble.VTDivorce\r\n\r\nDivorce\r\n\r\n## Authors\r\n\r\n- K. Surette, Legal Services Vermont\r\n- Q. Steenhuis, M. Bonardi and S. Constantinou, Lemma Legal\r\n\r\n\r\n',
      long_description_content_type='text/markdown',
      author='K. Surette',
      author_email='ksurette@legalservicesvt.org',
      license='The MIT License',
      url='legalservicesvt.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.ALToolbox>=0.11.1', 'docassemble.AssemblyLine>=3.1.0', 'docassemble.VTSharedYMLFile', 'docassemble.demo>=1.4.112'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/VTDivorce/', package='docassemble.VTDivorce'),
     )
