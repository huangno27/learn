#python标准库

from collections import OrderedDict

favorite_languages = OrderedDict

favorite_languages['jin'] = 'python'
favorite_languages['srach'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.title():
    print(name.title() + " 's favorite languages" +
          language.title())
