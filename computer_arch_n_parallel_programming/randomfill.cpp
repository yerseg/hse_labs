#include <cstdint>

using namespace std;

void randomfill(uint64_t* out, size_t n, uint64_t x, uint64_t a, uint64_t c)
{
    // randomfill(n, x, a, c) = x * a^n + c * (a^0 + ... + a^i + ... + a^(n-1))
    // randomfill(i + j, x_i, a, c) = x_i * a^j + c * (a^0 + ... + a^(j-1))
    // We need to have precomputed array with partial sums which can be used in every unrolled loop iteration

    constexpr size_t cache_size = 16;

    uint64_t precomputed_a_pows[cache_size] = {0};
    uint64_t precomputed_sums[cache_size] = {0};

    precomputed_a_pows[0] = a;
    precomputed_sums[0] = c;

    for (size_t i = 1; i < cache_size; ++i)
    {
        precomputed_a_pows[i] = precomputed_a_pows[i - 1] * a;
        precomputed_sums[i] = precomputed_sums[i - 1] + c * precomputed_a_pows[i - 1];
    }

    for (size_t i = 0; i < (n / cache_size) * cache_size; )
    {
        for (size_t j = 0; j < cache_size; ++j)
        {
            out[i + j] = x * precomputed_a_pows[j] + precomputed_a_pows[j];
        }

        i += cache_size;
        x = out[i - 1];
    }

    for (size_t i = (n / cache_size) * cache_size; i < n; ++i)
    {
        x = x * a + c;
        out[i] = x;
    }
}