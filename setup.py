import os
import sys
from setuptools import setup, find_namespace_packages
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

setup(name='docassemble.VTSmallClaimsComplaint',
      version='0.1',
      description=('Small claims complaint - Vermont - Form 100-00257'),
      long_description='# docassemble.VTSmallClaimsComplaint\n\nSmall claims complaint - Vermont - Form 100-00257\n\n## Author\n\nkelizamcguire@gmail.com\n\n',
      long_description_content_type='text/markdown',
      author='Guided interview by Legal Services Vermont / VTCourtForms',
      author_email='kelizamcguire@gmail.com',
      license='The MIT License',
      url='https://VTLawHelp.org/VTCourtForms',
      packages=find_namespace_packages(),
      install_requires=['docassemble.ALToolbox>=0.11.1', 'docassemble.AssemblyLine>=3.2.0', 'docassemble.GithubFeedbackForm>=0.4.1.1', 'docassemble.VTFeedback', 'docassemble.VTSharedYMLFile'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/VTSmallClaimsComplaint/', package='docassemble.VTSmallClaimsComplaint'),
     )

