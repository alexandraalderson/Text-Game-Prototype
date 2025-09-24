# Text-Game-Prototype

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alexandraalderson/Text-Game-Prototype/blob/main/code/TextGamePrototype.ipynb)

Python text game prototype for Edexcel iGCSE Computer Science students.

This project demonstrates key programming concepts such as loops, conditionals, functions, and user input/output. It is intended as a learning resource.

Features
- Multiple endings based on player choices
- Branching story logic
- Looping
- Player Inventory 

**Written as a Jupyter/Colab notebook.**

## Screenshot
![Screenshot showing opening game text and initial options](docs/Screenshot1.jpg)

## Code
- [code/TextGamePrototype.ipynb](code/TextGamePrototype.ipynb) – Interactive notebook
- [code/TextGamePrototype.py](code/TextGamePrototype.py) – Plain Python script
- [code/TextGamePrototype_TestEndings.py](code/TextGamePrototype_TestEndings.py) – Plain Python script of automated tests for each story ending

## How to Open
- **On GitHub:**
- Click `code/TextGamePrototype.ipynb' to view directly.
  
- **In Google Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alexandraalderson/Text-Game-Prototype/blob/main/code/TextGamePrototype.ipynb)
  
- **Locally:** Download the file and open with Jupyter Notebook.

## Tests
To run all automated ending tests:
`python -m unittest code/RobinHoodMidnightGold_TestEndings.py`

## Documentation
- [docs/RobinHoodFlowchart.png](docs/RobinHoodFlowchart.png) – Game logic flowchart  
- [docs/RobinHoodScript.md](docs/RobinHoodScript.md) – Game script in detail
- [docs/RobinHoodEdexcelPseudocode.md](docs/RobinHoodEdexcelPseudocode.md) - Edexcel iGCSE Computer Science standard Pseudocode for the game
- [docs/ScreenshotRobinHoodGameplay1.jpg](docs/ScreenshotRobinHoodGameplay1.jpg) – Gameplay screenshot (raw image)

## License
This project is licensed under the Apache License 2.0 – see the [LICENSE](LICENSE) file for details.

## Challenge
To create a simple, easy to understand text based game in Python that coveres the full development cycle to allow students to see how a game goes from an idea to an implementation.
