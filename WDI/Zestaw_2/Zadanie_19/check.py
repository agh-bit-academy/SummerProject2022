# Paweł Konopka
from ....readstdout import Capturing


def my_checkstdout(f, arg, ans):
    output_f, output_g = None, None

    with Capturing() as output_f:
        f(*arg)
    with Capturing() as output_g:
        print(ans)

    print("User output:      ", output_f)
    print("Expected output:  ", output_g)
    return output_f == output_g
