import sys
from .randTemplates.RFloat import RFloat
from io import StringIO


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


def prepare(data, float_type):
    if float_type:
        for i in range(len(data)):
            data[i] = data[i].rsplit(" ")
            for j in range(len(data[i])):
                data[i][j] = str(RFloat.print(data[i][j]))
            data[i] = "".join(data[i])
    output = data
    if len(data) > 1:
        output = "".join(data)
    return output[0]


def checkstdout(f, g, arg, float_type=None):
    output_f, output_g = None, None

    with Capturing() as output_f:
        f(*arg)
    with Capturing() as output_g:
        g(*arg)

    output_f = prepare(output_f, float_type)
    output_g = prepare(output_g, float_type)

    print("User output:      ", output_f)
    print("Expected output:  ", output_g)
    return output_f == output_g
