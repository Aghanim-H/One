
def gen():
    for c in 'AB':
        yield c

# list直接用生成器作为参数
print(list(gen()))

def gen_new():
    yield from 'AB'

print(list(gen_new()))