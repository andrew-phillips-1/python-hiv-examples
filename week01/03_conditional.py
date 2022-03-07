def prob_start_sex_work(age, ever_sw, life_sex_risk, rred_rc):
    """Compute the probability of a woman becoming a sex worker.

    Probability depends on the person's age, life sex risk, whether
    she has ever been a sex worker in the past and her risk reduction factor.

    Assumes sex is female.
    """
    base_rate_sw = 0.0020

    if life_sex_risk < 2:
        return 0  # we know the overall probability will be 0

    if life_sex_risk == 3:
        risk_factor = 3
    else:
        risk_factor = 1

    base_prob = base_rate_sw * rred_rc

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


def prob_infection_from_long_term_partner():
    ...


print("Hello world")