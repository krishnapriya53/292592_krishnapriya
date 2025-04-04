from strops import (
    get_span,
    reverseword,
    remove_punctuation,
    count_words,
    character_map,
    transform,
    makeTitle,
    normalizespace,
    get_permutations
)
 
def test_get_span():
    print("Testing get_span...")
    s = "hello hello"
    substring = "hello"
    print("String:", s)
    print("Substring:", substring)
    print("Span:", get_span(s, substring))
    print()
 
def test_reverseword():
    print("Testing reverseword...")
    s = "Hello"
    print("Original:", s)
    print("Reversed:", reverseword(s))
    print()
 
def test_remove_punctuation():
    print("Testing remove_punctuation...")
    s = "Hello, world!"
    print("Original:", s)
    print("Without punctuation:", remove_punctuation(s))
    print()
 
def test_count_words():
    print("Testing count_words...")
    s = "Hello world, how are you?"
    print("Sentence:", s)
    print("Word count:", count_words(s))
    print()
 
def test_character_map():
    print("Testing character_map...")
    s = "hello"
    print("String:", s)
    print("Character map:", character_map(s))
    print()
 
def test_transform():
    print("Testing transform...")
    s = "Hello World"
    print("Original:", s)
    transform(s)
    print()
 
def test_makeTitle():
    print("Testing makeTitle...")
    s = "hello world"
    print("Original:", s)
    print("Title:", makeTitle(s))
    print()
 
def test_normalizespace():
    print("Testing normalizespace...")
    s = "Hello    world  !  "
    print("Original:", repr(s))
    print("Normalized:", repr(normalizespace(s)))
    print()
 
def test_get_permutations():
    print("Testing get_permutations...")
    s = "ABC"
    print("Permutations of", s, "are:")
    # Since get_permutations expects a sequence (and uses list(s) inside),
    # we'll pass a list of characters to be explicit.
    get_permutations(list(s))
    print()
 
if __name__ == "__main__":
    test_get_span()
    print("-" * 40)
    test_reverseword()
    print("-" * 40)
    test_remove_punctuation()
    print("-" * 40)
    test_count_words()
    print("-" * 40)
    test_character_map()
    print("-" * 40)
    test_transform()
    print("-" * 40)
    test_makeTitle()
    print("-" * 40)
    test_normalizespace()
    print("-" * 40)
    test_get_permutations()
 
 
 