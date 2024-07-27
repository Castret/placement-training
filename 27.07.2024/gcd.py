def find_hcf(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    hcf = numbers[0]
    for i in range(1, len(numbers)):
        hcf = gcd(hcf, numbers[i])

    return hcf


user_input = input("Enter the numbers (separated by spaces): ")
num_list = list(map(int, user_input.split()))

hcf = find_hcf(num_list)
print("HCF of", num_list, "is", hcf)
