from fpylll import IntegerMatrix, GSO, LLL, FPLLL, BKZ

FPLLL.set_random_seed(1337)
M = GSO.Mat(LLL.reduction(IntegerMatrix.random(100, "qary", bits=30, k=50)))

from bkz_simulator import averaged_simulate_prob, simulate_prob
# from fpylll.tools.bkz_simulator import averaged_simulate_prob, simulate_prob

# prof, it = simulate_prob(M, BKZ.Param(block_size=40, max_loops=10, flags=BKZ.VERBOSE))
prof, it = averaged_simulate_prob(M, BKZ.Param(block_size=60, max_loops=4))
print(*[f"{x:9.3f}" for x in prof[:3]])
print(it)
