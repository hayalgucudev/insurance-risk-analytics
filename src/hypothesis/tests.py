import numpy as np
from scipy import stats


def t_test(group_a, group_b):
    """
    Compare means between two groups
    """
    return stats.ttest_ind(group_a, group_b, nan_policy="omit")


def chi_square_test(table):
    """
    Categorical independence test
    """
    return stats.chi2_contingency(table)


def interpret_p_value(p_value, alpha=0.05):
    """
    Business decision rule
    """
    return "Reject H0" if p_value < alpha else "Fail to Reject H0"