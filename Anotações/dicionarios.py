# Declarando dicionários
dicionario = {"Lucas Ribeiro Pedrosa": {"nome": "Lucas", "idade": "18"}}

print(dicionario) # {"Lucas Ribeiro Pedrosa": {"nome": "Lucas", "idade": "18"}}

# Utilizando o dict() para definir
dicionario = dict(nome = "Vitor", idade = "16")
print(dicionario) # {"nome": "Vitor", "idade": "16"}

# Declarando da maneira padrão

dicionario["telefone"] = "98711171"
print(dicionario)   #{"nome": "Vitor", "idade": "16", "telefone": "98711171"}

# Como chamar valores 

clientes = {
    "Lucas": {"email": "lucasrpedrosa25@gmail.com", "senha": "lucas250380", "id": "126"},
    "Vitor": {"email": "vitor25@gmail.com", "senha": "vitor250380", "id": "127"},
    "Gabriel": {"email": "gabriel25@gmail.com", "senha": "gabriel250380", "id": "128"},
    "Leonildo": {"email": "leojunior@gmail.com", "senha": "leo250380", "id": "129"}
}

clientes["Lucas"] # "Lucas"
clientes["Lucas"]["email"] # "lucasrpedrosa25@gmail.com"
clientes["Gabriel"]["id"]  # "128"
clientes["Leonildo"]["senha"] # "leo250380"

# Iterar os valores do dicionário - utilizando o for

for usuario in clientes:
    print(usuario, clientes[usuario])

# Outra forma de utilizar o for com o método items()

for chave, valor in clientes.items():
    print(chave, valor)

# Métodos do dicionário (alguns que estão porém não irei adicionar, como o .clear(), .pop(), .copy())

# .fromkeys() - Adiciona chaves, podendo atribuir o mesmo valor para as que forem adicionadas

dict.fromkeys(["nome", "idade"]) # {"nome": None, "idade": None}

dict.fromkeys(["nome", "idade"], "vazio") # {"nome": "vazio", "idade": "vazio"}

# . get() - Adiciona uma chave caso não estja presente no dicionário, e pode atribuir um valor, em caso da chave não existir dentro do dicionário dará "KeyError"

dic = {"nome": "Lucas", "idade": "18"}

# dic["chave"] --> KeyError

dic.get("chave") # None
dic.get("chave", {}) # {} - Atribui valor
dic.get("nome", {}) # "Lucas" --> Não atribui valor a chave existente

# .items() - Exibe todos os itens do dicionário, incluindo as chaves e valores a eles atribuidos

dic.items() # dict_items ([("nome": "Lucas", "idade": "18")])

# .keys() - Exibe todas as chaves que contêm o dicionário

dic_2 = {"Lucas": {"email": "lucasrpedrosa25@gmail.com", "idade": 18}}

dic_2.keys() # dict_keys (["Lucas"])

# .popitem() - exclui o último item adicionado

dic_2.popitem()
print(dic_2)  # {}  

# .setdefault() - Adiciona uma chave e um valor a ela, caso a chave já exista, o valor se mantém

dic_2 = {"Lucas": {"email": "lucasrpedrosa25@gmail.com", "idade": 18}}

dic_2.setdefault("idade", 12) # 18
dic_2.setdefault("id", 300) # "Lucas": {"email": "lucasrpedrosa25@gmail.com", "idade": 18, "id": 300}

# .update() - Permite atualizar as chaves e adicionar novas

dic_2.update({"Lucas": {"id": 200}}) # {"Lucas": "id": 200}
dic_2.update({"Vitor": {"id": 300}}) # {"Lucas": {"id": 200}, "Vitor": {"id": 300}}

# .values() - Exibe apenas dos valores das chaves

dic_2.values() # ([ {"id": 200}, {"id": 300}])

# del - Deleta itens e chaves especificos

del dic_2["Vitor"] # {"Lucas": {"id": 200}}
del dic_2["Lucas"]["id"] # {"Lucas"}



