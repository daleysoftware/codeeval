cmake_minimum_required(VERSION 3.5)
project(codeeval_cpp)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

set(AGE_DISTRIBUTION 0-easy/age-distribution/main.cpp)
add_executable(age-distribution ${AGE_DISTRIBUTION})

set (ARMSTRONG_NUMBERS 0-easy/armstrong-numbers/main.cpp)
add_executable(armstrong-numbers ${ARMSTRONG_NUMBERS})

set (EVEN_NUMBERS 0-easy/even-numbers/main.cpp)
add_executable(even-numbers ${EVEN_NUMBERS})

set (FILE_SIZE 0-easy/file-size/main.cpp)
add_executable(file-size ${FILE_SIZE})

set (HAPPY_NUMBERS 0-easy/happy-numbers/main.cpp)
add_executable(happy-numbers ${HAPPY_NUMBERS})

set (HEX_TO_DECIMAL 0-easy/hex-to-decimal/main.cpp)
add_executable(hex-to-decimal ${HEX_TO_DECIMAL})

set (LOWERCASE 0-easy/lowercase/main.cpp)
add_executable(lowercase ${LOWERCASE})

set (MERSENNE_PRIME 0-easy/mersenne-prime/main.cpp)
add_executable(mersenne-prime ${MERSENNE_PRIME})

set (MULTIPLICATION_TABLES 0-easy/multiplication-tables/main.cpp)
add_executable(multiplication-tables ${MULTIPLICATION_TABLES})

set (MULTIPLY_LISTS 0-easy/multiply-lists/main.cpp)
add_executable(multiply-lists ${MULTIPLY_LISTS})

set (ODD_NUMBERS 0-easy/odd-numbers/main.cpp)
add_executable(odd-numbers ${ODD_NUMBERS})

set (SUM_OF_DIGITS 0-easy/sum-of-digits/main.cpp)
add_executable(sum-of-digits ${SUM_OF_DIGITS})

set (SUM_OF_INTEGERS 0-easy/sum-of-integers-in-a-file/main.cpp)
add_executable(sum-of-integers ${SUM_OF_INTEGERS})

set (SUM_OF_PRIMES 0-easy/sum-of-primes/main.cpp)
add_executable(sum-of-primes ${SUM_OF_PRIMES})

set (UNIQUE_ELEMENTS 0-easy/unique-elements/main.cpp)
add_executable(unique-elements ${UNIQUE_ELEMENTS})

set (CONSECUTIVE_PRIMES 1-moderate/consecutive-primes/main.cpp)
add_executable(consecutive-primes ${CONSECUTIVE_PRIMES})

set (DECIMAL_TO_BINARY 1-moderate/decimal-to-binary/main.cpp)
add_executable(decimal-to-binary ${DECIMAL_TO_BINARY})

set (DOUBLE_SQUARES 1-moderate/double-squares/main.cpp)
add_executable(double-squares ${DOUBLE_SQUARES})

set (ENDIANNESS 1-moderate/endianness/main.cpp)
add_executable(endianness ${ENDIANNESS})

set (NUMBER_OF_ONES 1-moderate/number-of-ones/main.cpp)
add_executable(number-of-ones ${NUMBER_OF_ONES})

set (REVERSE_AND_ADD 1-moderate/reverse-and-add/main.cpp)
add_executable(reverse-and-add ${REVERSE_AND_ADD})

set (TO_PI_OR_NOT_TO_PI 1-moderate/to-pi-or-not-to-pi/main.cpp)
add_executable(to-pi-or-not-to-pi ${TO_PI_OR_NOT_TO_PI})

set (TRY_TO_SOLVE_IT 1-moderate/try-to-solve-it/main.cpp)
add_executable(try-to-solve-it ${TRY_TO_SOLVE_IT})

set (COMMUTING_ENGINEER 2-hard/commuting-engineer/main.cpp)
add_executable(commuting-engineer ${COMMUTING_ENGINEER})

set (ROBOT_MOVEMENTS 2-hard/robot-movements/main.cpp)
add_executable(robot-movements ${ROBOT_MOVEMENTS})
