def sort_sentence(sentence):
    sentence = sentence.lower()
    sentence = list(map(str, sentence.split()))
    arr = []
    for i in range(0, len(sentence)):
        b = min(sentence, key=len)
        arr.append(b)
        sentence.remove(b)
    b = arr[0].title()
    arr.remove(arr[0])
    sentence = ' '.join(arr)
    return b + ' ' + sentence
