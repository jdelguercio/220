
def fibonacci(n):
    n1, n2 = 0, 1
    count, sum = 0, 0

    if n > 0:
        while count <= n:
            output = sum
            count += 1
            n1 = n2
            n2 = sum
            sum = n1 + n2
        return output
    else:
        return None


def double_investment(principal, rate): # keep getting error
    years = 0
    lump = principal
    while lump <= (principal * 2):
        lump *= (1 + rate)
        years += 1
    return years



def syracuse(n):
    output = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            var = n
            output.append(var)
        else:
            n = n * 3 + 1
            var = n
            output.append(var)
    return output


def goldbach(n):
    primes = []
    num = 1
    if n % 2 == 0:
        while (num <= n):
            count = 0
            i = 2
            while (i <= num // 2):
                if (num % i == 0):
                    count += 1
                    break
                i += 1
            if (count == 0 and num != 1):
                primes.append(num)
            num = num + 1

    two_primes = []
    while sum(two_primes) == 0:
        index = 0
        index2 = 0
        while index < len(primes):
            index += 1
            while index2 < len(primes):
                index2 += 1
                summ = primes[index] + primes[index2]
                print(summ)
                if summ == n:
                    two_primes.append(primes[index])
                    two_primes.append(primes[index2])
                    break
                else:
                    pass
    return two_primes



