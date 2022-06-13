from distutils.core import setup, Extension

module_spam = Extension('spam', sources=['spammodule.c'])

setup(
    name='ScriptLang_WhereFi',
    version='1.0',

    py_modules=['GUI', 'noti', 'parsing', 'send_gmail', 'setup', 'teller'],

    packages=['image'],
    package_data={'image':['*.png']},

    ext_modules=[module_spam]
)