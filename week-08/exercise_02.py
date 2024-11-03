# Text: ATEISPAVASARISATBUSKAMPERZIEMAMIEGOTILEMTA
# First cipher: [19, 2, 145, 220, 230, 117, 44, 31, 26, 1, 23, 134, 220, 230, 100, 57, 11, 14, 1, 29, 149, 216, 229, 96, 63, 19, 18, 23, 27, 149, 216, 252, 96, 42, 6, 15, 27, 26, 145, 216, 225, 100]
# Second cipher: [95, 226, 183, 183, 211, 239, 225, 121, 169, 88, 187, 80, 183, 211, 254, 244, 109, 189, 88, 177, 67, 179, 208, 250, 242, 117, 161, 78, 183, 67, 179, 201, 250, 231, 96, 188, 66, 182, 71, 179, 212, 254]
# Conduct a bit pairs test for these streams.

from scipy.stats import chi2
import utilities.conversion as converter
import utilities.statistical_test_core as stc
import utilities.bit_pairs_test as bpt

alfa = 0.1

# applying bit pairs test to original text
txt = "ATEISPAVASARISATBUSKAMPERZIEMAMIEGOTILEMTA"
txt_bin = converter.text_to_binary(txt)
text_len = len(txt_bin)

t = bpt.get_bit_pair_test_statistic(txt_bin)
probability = 1 - chi2.cdf(t, 2)

print(f"t = {t:.10f}, p = {probability:.10f}")
stc.test_hypothesis_by_probability(alfa, probability)
print()


# applying bit pairs test to text ciphered using Linear-feedback shift registers
txt = [19, 2, 145, 220, 230, 117, 44, 31, 26, 1, 23, 134, 220, 230, 100, 57, 11, 14, 1, 29, 149, 216, 229, 96, 63, 19, 18, 23, 27, 149, 216, 252, 96, 42, 6, 15, 27, 26, 145, 216, 225, 100]
txt_bin = converter.num_list_to_binary(txt)
text_len = len(txt_bin)

t = bpt.get_bit_pair_test_statistic(txt_bin)
probability = 1 - chi2.cdf(t, 2)

print(f"t = {t:.10f}, p = {probability:.10f}")
stc.test_hypothesis_by_probability(alfa, probability)
print()


# applying bit pairs test to text ciphered using A5/1
txt = [95, 226, 183, 183, 211, 239, 225, 121, 169, 88, 187, 80, 183, 211, 254, 244, 109, 189, 88, 177, 67, 179, 208, 250, 242, 117, 161, 78, 183, 67, 179, 201, 250, 231, 96, 188, 66, 182, 71, 179, 212, 254]
txt_bin = converter.num_list_to_binary(txt)
text_len = len(txt_bin)

t = bpt.get_bit_pair_test_statistic(txt_bin)
probability = 1 - chi2.cdf(t, 2)

print(f"t = {t:.10f}, p = {probability:.10f}")
stc.test_hypothesis_by_probability(alfa, probability)