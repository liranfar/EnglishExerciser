# English Exerciser
a lightweight english (to hebrew) phrases exerciser using a simple `.xlsx` file.

##  Usage
    git clone https://github.com/liranfar/EnglishExerciser.git

    cd EnglishExerciser

    sudo apt-get install  pip virtualenv virtualenvwrapper
    
    mkvirtualenv englishExerciser
    
    pip install -r requirements.txt
    
    python reader.py

* The data is in `vocabulary.xlsx`, feel free to create a new one for yours.
* For already initialized virtualenv just use `$ workon englishExerciser` to enable it or `$ deactivate` to disable.
* To remove the established virtual-env just disable it and run `$ rmvirtualenv englishExerciser`
* For now, saving to disk is applied by pressing `ctrl + c`
## Resources
[Automate Your Boring Stuff - Openpyxl](https://automatetheboringstuff.com/chapter12/)

[Python-Textbook](https://python-textbok.readthedocs.io/en/1.0/Object_Oriented_Programming.html)

[Google-Text-to-Speech](https://github.com/pndurette/gTTS)

## License

[WTFPL – Do What the Fuck You Want to Public License](http://www.wtfpl.net)

