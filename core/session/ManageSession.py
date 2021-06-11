
def getheader_info(request):
    header_info = {
        'countryinfo': request.session['ip2country'],
        'weather': request.session['weather']
    }
    return header_info


def get_basic_info(request):
    basic_info = {
        'user_id': request.session['user_id'],
        'is_login': request.session['is_login'],
        'user_name': request.session['user_name']

    }
    return basic_info
