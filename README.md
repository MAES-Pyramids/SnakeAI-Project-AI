# Classic Snake Game AI Project
<img align="right" alt="GIF"  src="https://raw.githubusercontent.com/demartini/demartini/master/code.gif"  width="30%" /> 

<!-- <img align="right" alt="GIF" height="100%" src="https://camo.githubusercontent.com/0850a9b90bf720b08cafe764aea52d8cf2cc7048d4f8080297e8988b76bb08b8/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f7375706572666f6c696f2f696d6167652f75706c6f61642f76313632303638393937392f36383734373437303733336132663266363932653730363936653639366436373265363336663664326636663732363936373639366536313663373332663633333632663333333332663633333232663633333633333333363333323330363536343635333833323636333036353330363336353634333736343335333733303634363236353333363133313636333332653637363936365f796a756832732e676966"  width="40%" />  -->

This is a university team project for an AI course. The aim of this project is to build a classic snake game with obstacles and food, and then develop it further by integrating some AI algorithms such as A* and DFS to make the snake reach its maximum possible size.

<br>

To ensure an impartial evaluation, we will compare the effectiveness of the AI algorithms to that of a human player by measuring the correlation between the snake's length and the number of steps taken to achieve it. Additionally, we will analyze the collected data to identify any tendencies or insights that might indicate which algorithm is more suitable for the game. Finally, we will present our findings in a report that will be shared with our professor and classmates.


##  Documentation
| Algorithm | Description |
| --- | --- |
| A* | A heuristic search algorithm that uses a cost function to guide its search. In this game, we use A* to find the shortest path from the snake's current position to the food. |
| DFS | A search algorithm that explores as far as possible along each branch before backtracking. In this game, we use DFS to explore all possible paths to the food, and choose the path that results in the longest snake. |

## Requirements
- Python 3.6 or higher
- Pygame library

## Installation
1. Clone the repo to your local machine using `git clone https://github.com/MAES-Pyramids/SnakeAI.git`
2. Navigate to the project directory using `cd snake-game-ai`
3. Install the required dependencies using `pip install -r requirements.txt`
4. Run the game using `python main.py`

## Gameplay
- Use the arrow keys to move the snake
- Collect the food to grow longer
- Avoid hitting the obstacles and the snake's own body
- The game ends when the snake hits an obstacle or its own body

## Contributing
We welcome contributions to this project. If you would like to contribute, please open an issue to discuss your ideas before submitting a pull request.


## Team Members
 <img align="right" alt="GIF"  src="https://github.com/MAES-Pyramids/SnakeAI/blob/main/assets/documentations/chrome_KJaLpP8XXt.png"  width="45%" /> 
 
#### Project done under supervision of  Prof. [@Sara El-Metwally](https://github.com/SaraEl-Metwally) by:
- [@Muhammed Abdulaziz Mahmoud ](https://github.com/muhammed9865) | section 8
- [@Ahmed Mohsen Awad    ](https://github.com/PrinceEGY)     | Section 1
- [@Mohamed Abo El-Seoud ](https://github.com/MAES-Pyramids) | Section 8

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"  width="100%"/>
</p>
