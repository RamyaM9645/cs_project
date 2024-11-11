# corporate_dict/views.py

from django.shortcuts import render
from .models import CorporateTerm
import random

def corporate_dict_page(request):
     # Get a random word for "Today's Word"
    todays_word = CorporateTerm.objects.order_by('?').first()
    
    # List of fun introductory phrases for "Today's Word"
    fun_phrases = [
        "Here's your buzzword of the day",
        "Get savvy with today's word",
        "Corporate lingo spotlight!",
        "Learn today's term",
        "Your word to impress"
    ]
    
    # Choose a random phrase
    todays_word_phrase = random.choice(fun_phrases)

    # Fetch all terms to display below
    terms = CorporateTerm.objects.all()

    # Alphabet filter
    alphabet_filter = request.GET.get('alphabet', '')
    if alphabet_filter:
        if alphabet_filter == 'A-E':
            terms = terms.filter(word__regex=r'^[A-E]')
        elif alphabet_filter == 'F-J':
            terms = terms.filter(word__regex=r'^[F-J]')
        elif alphabet_filter == 'K-O':
            terms = terms.filter(word__regex=r'^[K-O]')
        elif alphabet_filter == 'P-T':
            terms = terms.filter(word__regex=r'^[P-T]')
        elif alphabet_filter == 'U-Z':
            terms = terms.filter(word__regex=r'^[U-Z]')

    # Sorting filter
    sort_order = request.GET.get('sort', '')
    if sort_order == 'asc':
        terms = terms.order_by('word')
    elif sort_order == 'desc':
        terms = terms.order_by('-word')

    return render(request, 'corporate_dict/corporate_dict_page.html', {
    'todays_word': todays_word,
    'todays_word_phrase': todays_word_phrase,
    'terms': terms,
})