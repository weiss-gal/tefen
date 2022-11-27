import re # import regular expression module - used for cleaning up the text

band_file_name = 'band.txt'
test_text_file_name = 'test.txt'

# Read and parse the band file
with open(band_file_name, 'r') as band_file:
    # \W+ matches any group of non-alphanumeric characters
    band = re.sub("\W+", " ", band_file.read()).lower().split()

#add trivial words to the list
band.append('i')
band.append('a')

# Read and parse the test file
with open(test_text_file_name, 'r') as test_text_file:
    # \W+ matches any group of non-alphanumeric characters
    test_words = re.sub("\W+", " ", test_text_file.read()).lower().split()
    test_words = set(test_words)

#print (band)
#print (test_words)

total_words_num = len(test_words)
difficult_words_num = 0
difficult_words = []
for w in test_words:
    if w not in band:
        difficult_words_num += 1
        difficult_words.append(w)

difficult_words.sort()

print(f"Total number of words: {total_words_num}")
print(f"Number of difficult words: {difficult_words_num}")
print(f"Difficult words: {difficult_words}")