import operator

from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html', {'given_val': "Given value is empty"})


def count(request):
    given_word = request.GET['fulltext']
    word_count = len(given_word.split())
    word_dic = {}
    for word in given_word.split():
        if word in word_dic:
            # Increase
            word_dic[word] += 1
        else:
            # Create new
            word_dic[word] = 1
    sorted_word_list = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', dict(word_count=word_count, your_text=given_word, word_dict=sorted_word_list))


def about(request):
    return render(request, 'about.html')
