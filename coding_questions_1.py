def count_unique_consonants(input_string):
    consonants = "bcdfghjklmnpqrstvwxyz"
    input_string = input_string.lower()
    char_counts = {}

    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    unique_consonants_count = 0
    for char in char_counts:
        if char in consonants and char_counts[char] == 1:
            unique_consonants_count += 1

    return unique_consonants_count


# time complexity & space complexity: O(n)
# assumptions: input string contains only English alphabet and may contain both uppercase and lowercase characters, but they are treated as equivalent.


# tests
if __name__ == '__main__':
    print(count_unique_consonants("cat"))  # Output: 2
    print(count_unique_consonants("cataract"))  # Output: 1
