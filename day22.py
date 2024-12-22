from src import Debug, Reader


debug = Debug()
example = False


def calc_next_secret(secret: int) -> int:
    def mix_and_prune(number: int, secret: int) -> int:
        return (number ^ secret) % 16777216

    # First setp
    x = secret * 64
    secret = mix_and_prune(x, secret)
    # Second step
    x = int(secret / 32)
    secret = mix_and_prune(x, secret)
    # Thrid
    x = secret * 2048
    secret = mix_and_prune(x, secret)

    return secret


with Reader(22, example) as reader:
    secrets = [x for x in reader.iter_lines(int)]


N = 2000
total = 0
for secret in secrets:
    for _ in range(N):
        secret = calc_next_secret(secret)
    total += secret
print(total)
