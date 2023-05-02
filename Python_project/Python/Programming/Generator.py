def gens():
    print("1")
    yield 10
    print("2")
    yield 20
gen=gens()

print(next(gen))
print(next(gen))