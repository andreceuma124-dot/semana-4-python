# delaracao do conjunto (chaves)
frutas = {"maca", "uva", "maca"}
# duplicatas sao eliminadas
print(frutas) # {'maca','uva'}
#teste de pertinencia (acesso)
print("uva" in frutas)  #true
# percorrendo o conjunto
for f in frutas:
    print(f)