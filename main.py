from newton_cotes import findQFcoefs as fqfc
from gauss_kind import findGaussKindQFCoefficents as QFCoefs
from input import borders, weightFunc, xs



if (__name__ == "__main__"):
    print(fqfc(weightFunc, xs))
    print(QFCoefs(weightFunc, borders, 3))
    pass
