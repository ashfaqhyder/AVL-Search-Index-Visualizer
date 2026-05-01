<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=28&duration=2800&pause=800&color=15D8FF&center=true&vCenter=true&width=900&lines=Real-Time+Keyword+Indexing+System;AVL+Tree+Powered+Search+Engine+Simulator;Fast+Insert+%7C+Search+%7C+Delete+%7C+Auto+Balancing" alt="Animated project title">

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-000000?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Visualization-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![AVL Tree](https://img.shields.io/badge/Data_Structure-AVL_Tree-15D8FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Ready-56F39A?style=for-the-badge)

</div>

<div style="border: 2px solid #15D8FF; border-radius: 12px; padding: 18px; background: #080B12;">

## Project Overview

**Real-Time Keyword Indexing System Using AVL Tree** is a beginner-friendly yet professional Flask mini project that simulates how a search engine can index keywords efficiently.

The application compares a self-balancing **AVL Tree** with a normal unbalanced **Binary Search Tree**, showing how AVL rotations keep searching fast even when data is inserted in sorted or skewed order.

</div>

<br>

<div style="border: 2px solid #56F39A; border-radius: 12px; padding: 18px;">

## Core Features

- Insert keywords into AVL Tree and BST
- Delete keywords from both structures
- Search keywords and compare step counts
- Automatically maintain AVL height and balance factor
- Demonstrate LL, RR, LR, and RL rotations
- Display latest rotation type
- Visualize AVL Tree and BST side by side
- Highlight searched keyword
- Show AVL height, BST height, and height difference
- Reset all indexed keywords
- Generate random sample keywords
- Responsive futuristic dark theme UI

</div>

<br>

<div style="border: 2px solid #FFD166; border-radius: 12px; padding: 18px;">

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Visualization | JavaScript DOM rendering |
| Storage | In-memory data structures |
| Data Structures | AVL Tree, Binary Search Tree |

</div>

<br>

<div style="border: 2px solid #15D8FF; border-radius: 12px; padding: 18px;">

## Project Structure

```text
AVL_ADVANCED/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

</div>

<br>

<div style="border: 2px solid #56F39A; border-radius: 12px; padding: 18px;">

## How To Run

Open the project folder in VS Code:

```powershell
cd C:\Projects\AVL_ADVANCED
```

Install Flask:

```powershell
pip install -r requirements.txt
```

Run the Flask app:

```powershell
python app.py
```

Open this URL in your browser:

```text
http://127.0.0.1:5000
```

If port `5000` is busy, run on another port:

```powershell
python -c "from app import app; app.run(debug=True, use_reloader=False, port=5001)"
```

</div>

<br>

<div style="border: 2px solid #FF5C7A; border-radius: 12px; padding: 18px;">

## Sample Test Inputs

Use these keyword orders to demonstrate AVL rotations:

| Rotation | Insert Order |
|---|---|
| LL Rotation | `gamma`, `beta`, `alpha` |
| RR Rotation | `alpha`, `beta`, `gamma` |
| LR Rotation | `gamma`, `alpha`, `beta` |
| RL Rotation | `alpha`, `gamma`, `beta` |

Use this sorted input to show why BST can become inefficient:

```text
algorithm, backend, cache, database, engine, flask, google
```

</div>

<br>

<div style="border: 2px solid #15D8FF; border-radius: 12px; padding: 18px;">

## How AVL Balancing Works

After every insert or delete operation, the AVL Tree updates each node's height.

It then calculates the balance factor:

```text
Balance Factor = Height of Left Subtree - Height of Right Subtree
```

If the balance factor becomes greater than `1` or less than `-1`, the tree becomes unbalanced.

The app fixes this automatically using rotations:

- **LL Rotation**: fixed with right rotation
- **RR Rotation**: fixed with left rotation
- **LR Rotation**: fixed with left rotation, then right rotation
- **RL Rotation**: fixed with right rotation, then left rotation

This keeps AVL operations close to:

```text
Search: O(log n)
Insert: O(log n)
Delete: O(log n)
```

</div>

<br>

<div style="border: 2px solid #56F39A; border-radius: 12px; padding: 18px;">

## Flask Routes

| Route | Purpose |
|---|---|
| `/` | Main web page |
| `/insert` | Insert a keyword |
| `/delete` | Delete a keyword |
| `/search` | Search a keyword |
| `/get_tree_data` | Return AVL and BST data as JSON |
| `/reset` | Clear both trees |

</div>

<br>

<div style="border: 2px solid #FFD166; border-radius: 12px; padding: 18px;">

## Viva Demonstration Guide

1. Start the app and introduce it as a search-engine keyword indexing simulator.
2. Explain that both AVL Tree and BST store the same keywords.
3. Insert sorted keywords like `algorithm`, `backend`, `cache`, `database`.
4. Show that the BST becomes taller while the AVL Tree stays balanced.
5. Insert `alpha`, `beta`, `gamma` to demonstrate an RR rotation.
6. Search for a keyword and compare AVL steps with BST steps.
7. Delete a keyword and explain that AVL rebalances again if needed.
8. Conclude that AVL Tree improves search reliability by maintaining `O(log n)` height.

</div>

<br>

<div align="center">

### Built For Learning Data Structures Through Visualization

![AVL Animation](https://img.shields.io/badge/Auto_Balancing-Enabled-15D8FF?style=flat-square)
![Search Steps](https://img.shields.io/badge/Search_Step_Comparison-Enabled-56F39A?style=flat-square)
![Dark UI](https://img.shields.io/badge/Futuristic_UI-Dark_Mode-111827?style=flat-square)

</div>
