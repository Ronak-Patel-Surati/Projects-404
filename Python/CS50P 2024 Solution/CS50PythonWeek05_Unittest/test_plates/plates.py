def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the middle character is a number or not
    length = len(s)
    hf_len = int(length / 2)
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if s[hf_len - 1] in nums: # -1 is because python counts from 0 and not 1
        return False
    
    # Check for alphanumeric characters
    if not s.isalnum():  # Added check for alphanumeric characters
        return False

    # Length Check
    if len(s) < 2 or len(s) > 6:
        return False
    # First 2 letter check
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    # First number check
    for char in s:
        if not char.isalpha():
            if char == "0":
                return False
            else:
                break
    # Other checks
    for char in s:
        if char in ['.', ' ', '!', '?']:
            return False

    if not s.isalnum():
        return False

    return True

if __name__ == "__main__":
  main()
