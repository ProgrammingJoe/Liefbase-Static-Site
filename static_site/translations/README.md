# Internationalization


* Extract strings to be translated
  * `$ pybabel extract -F babel.cfg -o messages.pot .`
* To add a new language
  * `$ pybabel init -i messages.pot -d translations -l de` ONLY RUN FOR NEW LANGUAGE
* Edit the messages.po files with translations
* Compile translations for use
  * `$ pybabel compile -d translations`
* Merge new string changes
  * `$ pybabel update -i messages.pot -d translations`
