import pandas as pd

# Exemplo de valores
novo_cont_inter1 = "[3b1c02bac2a429e6, Books, Â£52.29, Â£52.29, Â£0.00, In stock (19 available), 0]"
novo_cont_inter2 = "[UPC, Product Type, Price (excl. tax), Price (incl. tax), Tax, Availability, Number of reviews]"

# Criar uma lista com os valores
coluna_1 = [novo_cont_inter1]
coluna_2 = [novo_cont_inter2, novo_cont_inter2]


# Criar um DataFrame usando pandas
tabela = pd.DataFrame({'Coluna 1': coluna_1})
tabela2 = pd.DataFrame({'Coluna 1': coluna_1})

# Exibir a tabela
print(tabela,tabela2)
