# checks for vowels

string= "A lazy dog jumps on a beer"
string=string.lower()
totalVowel=(string.count("a"),
            string.count("e"),
            string.count("i"),
            string.count("o"),
            string.count("u") )

print(f"total vowels are: ", totalVowel)