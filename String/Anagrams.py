def areAnagrams(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    # Create a hashmap to store
    # character frequencies
    charCount = {}
    
    # Count frequency of each 
    # character in string s1
    for ch in s1:
        charCount[ch] = charCount.get(ch, 0) + 1
  
    # Count frequency of each
    # character in string s2
    for ch in s2:
        charCount[ch] = charCount.get(ch, 0) - 1
  
    # Check if all frequencies are zero
    for value in charCount.values():
        if value != 0:
            return False
    
    return True

if __name__ == "__main__":
    
    s1 = "level"
    s2 = "level"
    if areAnagrams(s1, s2):
        print("true")
    else:
        print("false")