from .start import soma_dois_numeros


def test_soma_dois_numeros():
    """teste soma"""

    result = soma_dois_numeros(2, 4)
    assert result == 6
