import math


def prob_start_sex_work(age, ever_sw, life_sex_risk, rred_rc):
    """Compute the probability of a woman becoming a sex worker.

    Probability depends on the person's age, life sex risk, whether
    she has ever been a sex worker in the past and her risk reduction factor.

    Assumes sex is female.
    """
    base_rate_sw = 0.0020

    if life_sex_risk < 2:
        return 0  # we know the final probability will be 0, so can exit early

    if life_sex_risk == 3:
        risk_factor = 3
    else:
        risk_factor = 1

    base_prob = base_rate_sw * math.sqrt(rred_rc)

    if 15 <= age < 20:
        age_factor = 1
    elif 20 <= age < 25:
        age_factor = 1
    elif 25 <= age < 35:
        age_factor = 0.3
    elif 35 <= age < 50:
        age_factor = 0.03
    else:
        return 0

    prob = base_prob * age_factor * risk_factor

    if ever_sw:
        prob = prob * 10

    return min(prob, 1)


# Try a couple of examples that should have probability 0
print(prob_start_sex_work(20, True, 1, 1.0))  # low life risk
print(prob_start_sex_work(55, False, 2, 1.0))  # age outside bounds
# And some with non-zero probability
print(prob_start_sex_work(20, False, 2, 1.0))
print(prob_start_sex_work(20, False, 3, 1.0))
print(prob_start_sex_work(20, True, 2, 1.0))


# How can we write a function that computes the probability of a long-term
# partner being diagnosed with HIV? [Eq. 9, Section 3.6 in Model Details]
# This should depend on the the proportion of HIV-infected long-term partners
# diagnosed at the previous time, and the proportion of subjects with HIV
# who are diagnosed.
def prob_long_term_partner_diagnosed():
    ...
