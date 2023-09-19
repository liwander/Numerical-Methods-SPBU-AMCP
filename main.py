from newton_cotes import findQFcoefs as fqfc
from gauss_kind import findGaussKindQFCoefficents as QFCoefs
from input import xs
from moments import weightFunc



if (__name__ == "__main__"):
    print(QFCoefs(weightFunc, 3))
    pass
