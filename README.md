# 'plus-1' sample Python function

This contains a complete sample function, wrapped ready for deployment on OpenFaas. Check `SPECS.md` for details of the algorithm. You can use this repo as either a sample or a start-point for your own function. 

*TLDR*: Most of the custom functionality is inside `handler.py`.

There are three levels, and the folder structure looks like:

```
├── README.md <-- The file you're reading
├── SPECS.md <-- Specifications for the function
├── plus-one <-- Folder usually named the same as the function
│   ├── Dockerfile <-- Usually no need to edit, can break deployment
│   ├── function <-- Usually called `function`, contains custom code
│   │   ├── __init__.py <-- Standard Python
│   │   ├── handler.py <-- Main piece of custom code
│   │   ├── preprocess_params.py <-- Include here any checks or shaping of input
│   |   └── requirements.txt <-- Standard Python `pip` requirements
│   └── index.py <-- Wrapper code, don't usually need to edit
└── stack.yml <-- Configuration file for deploying on OpenFaas
```
