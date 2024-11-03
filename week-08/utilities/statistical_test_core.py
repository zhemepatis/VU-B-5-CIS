def test_hypothesis_by_probability(alfa, probability):
    if alfa > probability:
        print("Hypothesis H0 is rejected - the sequence is not typical.")
    else:
        print("Hypothesis H0 is accepted - the sequence is typical.")