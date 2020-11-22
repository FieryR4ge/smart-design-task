## Installation
```
  pip install -r requirements.txt
```
```
  apt-get install httpie
```

## Launch
```
  python run.py
```

## Methods

- Sort by name
```
  http http://0.0.0.0:5000/goods\?sort\=name
```
- Sort by ID

```
  http http://0.0.0.0:5000/goods\?sort\=ID
```
- Get product details by ID
```
  http http://0.0.0.0:5000/goods\?where='{"ID": "12"}'
```

- Create new product 
```
  http http://0.0.0.0:5000/goods name=Xiaomi ID=13 description=China
```
