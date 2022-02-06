#include <cstdint>
#include <cstring>

using word_t = uint32_t;
using byte_t = unsigned char;
using cstr_t = const char*;

constexpr byte_t ascii_digits_begin = 0x30;
constexpr byte_t ascii_letters_begin = 0x61;

inline char get_digit_represenation(byte_t x)
{
    return x <= 9 ? ascii_digits_begin + x : ascii_letters_begin + x - 10;
}

template <size_t N>
void fill_out(char* out, const byte_t* in, size_t begin_idx)
{
    byte_t quot = in[begin_idx] / 16;
    byte_t rem = in[begin_idx] % 16;
    word_t out_word = 0x0000785c;
    out_word |= get_digit_represenation(quot) << 16;
    out_word |= get_digit_represenation(rem) << 24;
    memcpy(out, &out_word, sizeof(word_t));

    fill_out<N - 1>(out + sizeof(word_t), in, begin_idx + 1);
}

template <>
void fill_out<0>(char*, const byte_t*, size_t) {}

#define FILL_OUT(out, in, i, iter) \
    byte_t quot_##iter = in[i + iter] / 16; \
    byte_t rem_##iter = in[i + iter] % 16; \
    word_t out_word_##iter = 0x0000785c; \
    out_word_##iter |= get_digit_represenation(quot_##iter) << 16; \
    out_word_##iter |= get_digit_represenation(rem_##iter) << 24; \
    memcpy(out + sizeof(word_t) * iter, &out_word_##iter, sizeof(word_t)); \

inline void hexdump_templates(char* out, const byte_t* in, size_t n)
{
    if (!n) return;

    constexpr size_t unroll_coef = 4;

    for (size_t i = 0; i < n - unroll_coef; i += unroll_coef, out += unroll_coef * sizeof(word_t))
    {
        fill_out<unroll_coef>(out, in, i); 
    }
    
    for (size_t i = (n / unroll_coef) * unroll_coef; i < n; ++i, out += sizeof(word_t))
    {
        fill_out<1>(out, in, i); 
    }
}

inline void hexdump_macros(char* out, const byte_t* in, size_t n)
{
    if (!n) return;

    constexpr size_t unroll_coef = 4;

    for (size_t i = 0; i < n - unroll_coef; i += unroll_coef, out += unroll_coef * sizeof(word_t))
    {
        FILL_OUT(out, in, i, 0); 
        FILL_OUT(out, in, i, 1); 
        FILL_OUT(out, in, i, 2); 
        FILL_OUT(out, in, i, 3); 
    }
    
    for (size_t i = (n / unroll_coef) * unroll_coef; i < n; ++i, out += sizeof(word_t))
    {
        FILL_OUT(out, in, i, 0);
    }
}

void hexdump(char* out, const byte_t* in, size_t n)
{
    // hexdump_macros(out, in, n);
    hexdump_templates(out, in, n);
}
