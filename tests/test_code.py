import subprocess
import pytest

def test_addition1():
    input_data = "2 3/n"
    result_data = 5

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,    # Capture a saída padrão
        stderr=subprocess.PIPE,    # Capture a saída de erro
    )

    assert int(result.stdout.decode()) == result_data


def test_addition2():
    input_data = "3 3/n"

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,    # Capture a saída padrão
        stderr=subprocess.PIPE,    # Capture a saída de erro
    )

    assert int(result.stdout.decode()) == 6


def test_addition3():
    input_data = "4 4/n"

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,    # Capture a saída padrão
        stderr=subprocess.PIPE,    # Capture a saída de erro
    )

    assert int(result.stdout.decode()) == 8
