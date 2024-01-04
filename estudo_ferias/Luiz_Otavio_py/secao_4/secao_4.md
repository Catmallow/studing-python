#####  108 Escopo de funções e módulos em python

```python
x = 1

def escopo():
    x = 10
    
    def outra_funcao():
        y = 2 
        print(x,y)
    outra_funcao()
    print(x)
escopo()
```

####  109 Escopo de funções e módulos em python

