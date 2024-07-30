```mermaid
graph TD
    A["0. initial_state\nInitializes the Boards"]
    B["1. player\nDetermine current player"]
    C["2. actions\nList Possible Actions for current board"]
    D["3. result\nSimulates the result of a given action"]
    E["4. winner\nChecks for a winner."]
    F["5. terminal\nDetermines if the game is over"]
    G["6. utility\nEvaluates the utility of a terminal board."]
    H["7. minimax\nFinds the optimal move for the player."]



    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
    A --> G
    A --> H
    
    B --> H
    C --> H
    D --> H
    E --> F
    F --> G
    G --> H
    H --> D

```
<!-- 
    subgraph Notes
        note1["1. Initializes the board."]
        note2["2. Determines the current player."]
        note3["3. Lists all possible actions for the current board."]
        note4["4. Simulates the result of a move."]
        note5["5. Checks for a winner."]
        note6["6. Determines if the game is over."]
        note7["7. Evaluates the utility of a terminal board."]
        note8["8. Finds the optimal move using the above functions."]
    end
    A -.-> note1
    B -.-> note2
    C -.-> note3
    D -.-> note4
    E -.-> note5
    F -.-> note6
    G -.-> note7
    H -.-> note8 -->