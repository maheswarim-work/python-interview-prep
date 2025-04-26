
def dict_example():
    print("begin")

    # d = {'foo': 100, 'bar': 200, 'baz': 300}
    # print(d)
    #
    # d = {}
    # d['foo'] = 100
    # d['bar'] = 200
    # d['baz'] = 300
    # print(d)
    #
    # d = dict(foo=100, bar=200, baz=300)
    # print(d)
    #
    # d = {
    #     ('foo', 100),
    #     ('bar', 200),
    #     ('baz', 300),
    # }
    # print(d)
    #
    # d = dict(foo=100, bar=200, baz=300)
    # print(d)
    #
    # d = dict([('foo', 100), ('bar', 200), ('baz', 300)])
    # print(d)

    # x = [
    #     'a',
    #     'b',
    #     {
    #         'foo': 1,
    #         'bar':
    #             {
    #                 'x': 10,
    #                 'y': 20,
    #                 'z': 30
    #             },
    #         'baz': 3
    #     },
    #     'c',
    #     'd'
    # ]
    #
    # print(x[2]['bar']['z'])

    # d = {['foo', 'bar']: 1}
    # print(d) #TypeError: unhashable type: 'list'

    # d = {dict(foo=1, bar=2): 1}
    # print(d) #TypeError: unhashable type: 'dict'

    # d = {(3+2j): 1}
    # print(d) #valid

    # d = {len:1}
    # print(type(d)) #dict
    # print(d) #{<built-in function len>: 1} #valid

    # d = {('foo', 'bar'): 1}
    # print(d) #valid

    # d = {'foo': 1}
    # print(d)

    # x = [
    #     'a',
    #     'b',
    #     {
    #         'foo': 1,
    #         'bar':
    #             {
    #                 'x': 10,
    #                 'y': 20,
    #                 'z': 30
    #             },
    #         'baz': 3
    #     },
    #     'c',
    #     'd'
    # ]
    #
    # print('z' in x[2])

    # d = {'foo': 100, 'bar': 200, 'baz': 300}
    # d.pop('bar')
    # print(d)

    # d1 = {'name': 'aarthi', 'age': 42}
    # print(d1)

    # d2 = dict(d1.values()) # Invalid ValueError: dictionary update sequence element #0 has length 6; 2 is required

    # d2 = d1 #Valid

    # d2 = dict(d1.items()) #Valid

    # d2 = {}
    # d2.update(d1) # Valid

    # d2 = dict(d1) # Valid

    #d2 = dict(d1.keys()) # ValueError: dictionary update sequence element #0 has length 4; 2 is required

    # print(d2)

    d1 = {'name': 'aarthi', 'age': 42}
    # d1.items()
    # print(d1.items())
    # print(type(d1.items()))

    # print(list(d1.items()))
    # print(type(list(d1.items())))

    # print(list(d1.items())[1])

    # for i in list(d1.items()):
    #     print(i[1])
    #
    # print(d1.keys())
    # print(d1.values())
    # print(d1.pop('name'))

    # d1.popitem()
    # print(d1)

    # d1 = {
    #     "a": "Robin",
    #     "b": "Galahad"
    # }
    #
    # d2 = {
    #     "c": "Rabbit",
    #     "b": "Black Knight",
    #     "d": "Shrubbery"
    # }

    # d2.update(c='Ni', d='Green Knight')
    # print(d2)

    # print(d1)
    # print(d2)
    #
    # # d1.update(d2)
    # d1.clear()
    # print(d1)

    x = {'type': 'fruit', 'name': 'apple'}
    x.update({'color':'green'})
    print(x)

    print("end")

if __name__ == '__main__':
        dict_example()