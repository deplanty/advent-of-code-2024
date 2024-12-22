from queue import deque

from src import Debug, Reader


debug = Debug(False)
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


def ones_digit(number: int) -> int:
    return number % 10


# Read the data
with Reader(22, example) as reader:
    secrets = [x for x in reader.iter_lines(int)]

## Part 1

N = 2000
total = 0
for secret in secrets:
    for _ in range(N):
        secret = calc_next_secret(secret)
    total += secret
print("Part 1:", total)

## Part 2

N = 2000

# List all the possible sequences for all the secrets
all_sequences: dict[tuple[int], dict[int, int]] = dict()
for i, secret in enumerate(secrets):
    debug(f"Secret {i + 1}/{len(secrets)}: {secret}")
    current_secret = secret
    # List all the differences and all the ones digit
    diffs: deque = deque(maxlen=4)
    last: int = ones_digit(secret)
    for j in range(N):
        next_secret = calc_next_secret(secret)
        digit = ones_digit(next_secret)
        diffs.append(digit - last)
        if j >= 3:
            sequence = tuple(diffs)
            if sequence not in all_sequences:
                all_sequences[sequence] = dict()
            if current_secret not in all_sequences[sequence]:
                all_sequences[sequence][current_secret] = digit

        secret = next_secret
        last = digit


# Get the sequence that gives the maximum number of bananas
max_bananas = 0
max_sequence = (0, 0, 0, 0)
for i, (sequence, buyers) in enumerate(all_sequences.items()):
    debug(f"Sequence {i + 1}/{len(all_sequences)}: {sequence}")
    # Calculate the bananas possible with this sequence
    bananas = sum(value for value in buyers.values())
    if bananas > max_bananas:
        max_bananas = bananas
        max_sequence = sequence

debug(max_sequence)
debug(max_bananas)
print("Part 2:", max_bananas)
