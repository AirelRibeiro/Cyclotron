from cyclotron import cyclotron


def test_cyclotron():
    print("\n\nTeste de caso para aceleração sem partículas")
    assert cyclotron("", 4) == [
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
    ]

    print("\nTeste de caso para aceleração com electron")
    assert cyclotron("e", 4) == [
        ["e", "e", "e", "e"],
        ["1", "1", "1", "e"],
        ["1", "1", "1", "e"],
        ["1", "1", "1", "e"],
    ]

    print("\nTeste de caso para aceleração com proton - 4x4 matrix")
    assert cyclotron("p", 4) == [
        ["p", "p", "p", "p"],
        ["p", "1", "1", "p"],
        ["p", "1", "p", "p"],
        ["p", "p", "p", "1"],
    ]

    print("\nTeste de caso para aceleração com proton - 6x6 matrix")
    assert cyclotron("p", 6) == [
        ["p", "p", "p", "p", "p", "p"],
        ["p", "1", "1", "1", "1", "p"],
        ["p", "1", "1", "1", "1", "p"],
        ["p", "1", "1", "1", "1", "p"],
        ["p", "1", "1", "1", "p", "p"],
        ["p", "p", "p", "p", "p", "1"],
    ]

    print("\nTeste de caso para aceleração com neutron")
    assert cyclotron("n", 4) == [
        ["n", "n", "n", "n"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
    ]
