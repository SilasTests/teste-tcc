import subprocess

def test_addition4():
    input_data = "2 3/n"

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,    # Capture a saída padrão
        stderr=subprocess.PIPE,    # Capture a saída de erro
    )

    assert int(result.stdout.decode()) == 5


def test_addition5():
    input_data = "3 3/n"

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,    # Capture a saída padrão
        stderr=subprocess.PIPE,    # Capture a saída de erro
    )

    assert int(result.stdout.decode()) == 6


def test_addition6():
    input_data = "4 3/n"

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,    # Capture a saída padrão
        stderr=subprocess.PIPE,    # Capture a saída de erro
    )

    assert int(result.stdout.decode()) == 7