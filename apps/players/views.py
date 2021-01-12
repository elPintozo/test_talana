import random
from django.shortcuts import render, redirect
from django.contrib import messages

from verify_email.email_handler import send_verification_email

from apps.players.forms import PlayerCreateForm
from apps.players.models import Player

def create_player(request):
    """
    function to create a new player
    :param request:
    :return:
    """
    response = dict()

    #
    if request.method == 'POST' and request.POST.get('email', False):
        #
        form = PlayerCreateForm(request.POST)
        #
        if form.is_valid() and Player.exists(request.POST.get('email', '')) is False:

            #save form
            form.save()

            #send email for validate
            # inactive_user = send_verification_email(request, form)

            # I send a success message
            messages.success(request, 'Created with success')

            return redirect('index')
        else:
            # I send a error message
            messages.error(request, 'We have a problem.')
    else:
        form = PlayerCreateForm()

    response['form'] = form

    return render(request, 'players/playerform.html', response)


def search_to_winner(request):
    """
    Function that search winner betwen players with participate=True
    :param request:
    :return:
    """
    emails = Player.objects.filter(participate=True).values_list('email', flat=True)
    #emails = Player.objects.all().values_list('email', flat=True)

    if emails:
        winner = random.choice(emails)
        # I send a success message
        messages.success(request, 'The winner is: {}'.format(winner))
    else:
        # I send a success message
        messages.error(request, 'There is not players.')

    return redirect('index')
