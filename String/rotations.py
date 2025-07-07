# Python program to check two strings for rotation by generating all rotations

def areRotations(s1, s2):
    n = len(s1)

    # Generate and check all possible rotations of s1
    for _ in range(n):
        
        # If current rotation is equal to s2, return true
        if s1 == s2:
            return True

        s1 = s1[-1] + s1[:-1]
    return False

if __name__ == "__main__":
    s1 = "aab"
    s2 = "aba"
    print("true" if areRotations(s1, s2) else "false")