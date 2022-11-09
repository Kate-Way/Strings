# Determine is string is a palindrome considering only alphanumeric characters and ignoring case sensitivity



def is_palindrome(str):
    formatted = ''.join(e for e in str if e.isalnum()).lower()
    i = 0
    j = len(formatted) - 1
    while i < j:
        if formatted[i] == formatted[j]:
            i += 1
            j -= 1
        else:
            return False

    return True

