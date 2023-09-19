from newton_cotes import findQFcoefs as fqfc
from gauss_kind import findGaussKindQFCoefficents as QFCoefs
from input import borders, weightFunc



if (__name__ == "__main__"):
    print(QFCoefs(weightFunc, borders, 3))
    pass
