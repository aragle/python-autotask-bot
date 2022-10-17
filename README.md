# kormochari
Kormochari is an automatic keyboard and mouse controlling system.

## Install kormochari library

Step-1: Download or clone this repository -

    git clone https://github.com/aratheunseen/kormochari.git
    
Step-2: Enter the main directory

    cd kormochari

Step-3: Open CMD/Terminal in this directory

Step-4: Run setup.py file to complete the setup

    pip install .
    
  or
    
    python setup.py
    
 
## Create project
Step-1: create a file with extension `.py` (e.g. file_name.py)

Step-2: import kormochari library

    from kormochari import kaz
    
Step-3: Call function

| Function | Defination | Example |
| -----   | ----- | ----- |
| amar_jaiga_dekhao(n_second_pore) | Print position of mouse after n second   | kaz.amar_jaiga_dekhao(5) |
| jao(x, y, n_second_pore) | Move mouse to (X,Y) position after n second   | kaz.jao(100,203,5) |
| lekho(kotha) | Write inside text box | kaz.lekho("Ami ekai likhte pari.") |
| aste_lekho(kotha,koto_aste) | Write inside text box one by one character | kaz.aste_lekho("Ami asteo likhte pari.",0.25) |
| chapo() | Click left button of mouse | kaz.chapo() |
| dan_button_chapo() | Click right button of mouse  | kaz.dan_button_chapo() |
| button_chapo('x') | Click 'x' button of keyboard  | kaz.button_chapo('enter') |
| dui_bar_chapo() | Double click to left button of mouse  | kaz.dui_bar_chapo() |

Step-4: Run project

        python file_name.py
        
        
## Sample Code
After interpreting this code, It will search 'Notepad' on your start menu and will write "Apni obossoi parben vai." inside Notepad -
        
        from kormochari import kaz

        kaz.jao(20, 1060, 2)
        kaz.chapo()
        kaz.ektu_thamo(2)
        kaz.aste_lekho('Notepad')
        kaz.ektu_thamo(2)
        kaz.key_chapo('enter')
        kaz.ektu_thamo(7)
        kaz.aste_lekho("Apni obossoi parben vai.")
