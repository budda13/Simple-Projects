
def prep(word):
    if word[0] in ('a', 'e', 'i', 'o', 'u'):
        return 'an ' + word
    else:
        return 'a ' + word

adj1 = prep(input("Enter an adjective:  "))
noun1 = input("Enter a noun:  ")
past_verb1 = input("Enter a past tense verb:  ")
adverb1 = input("Enter an adverb:  ")
adj2 = input("Enter another adjective:  ")
noun2 = input("Enter a second noun:  ")
noun3 = input("And a third noun:  ")
adj3 = prep(input("Enter a adjective again:  "))
verb1 = input("Enter a present tense verb:  ")
adverb2 = input("Enter an adverb:  ")
past_verb2 = input("Enter another past tense verb:  ")
adj4 = prep(input("Finally, enter a final adjective:  "))

print(f"""Today I went to the zoo. I saw {adj1} {noun1} jumping up and down in its tree. 
He {past_verb1} {adverb1} through the large tunnel that led to its {adj2} {noun2}.
I got some peanuts and passed them through the cage to a gigantic gray
{noun3} towering above my head. Feeding that animal made me hungry. I went to get
{adj3} scoop of ice cream. It filled my stomach. Afterwards I had to {verb1}
{adverb2} to catch our bus. When I got home I {past_verb2} my mom for
{adj4} day at the zoo""")
