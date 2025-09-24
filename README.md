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
![Screenshot showing initial options and a single selection](docs/TextGamePrototypeScreenshot1.jpg)

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
`python -m unittest code/TextGamePrototype_TestEndings.py`

## Documentation
- [docs/TextGamePrototypeFlowChartFinal.png](docs/TextGamePrototypeFlowChartFinal.png) – Game logic flowchart  
- [docs/RobinHoodEdexcelPseudocode.md](docs/RobinHoodEdexcelPseudocode.md) - Edexcel iGCSE Computer Science standard Pseudocode for the game
- [docs/TextGamePrototypeScreenshot1.jpg](docs/TextGamePrototypeScreenshot1.jpg) – Gameplay screenshot (raw image)

## License
This project is licensed under the Apache License 2.0 – see the [LICENSE](LICENSE) file for details.

## Challenge
To create a simple, easy to understand text based game in Python that coveres the full development cycle to allow students to see how a game goes from an idea to an implementation. It is a framework for them to be able to customise and adapt to build their own game.
