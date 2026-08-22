# EdgeML-Flow

CLI zero-dep que roda um pipeline de ML leve (normalize min-max + predict por limiar) sobre CSV.

## Install
```
pip install .
```

## Uso
```
echo '{"steps":[{"op":"normalize","cols":["x"]},{"op":"predict","col":"x"}]}' > p.json
EdgeML-Flow dados.csv p.json
```
