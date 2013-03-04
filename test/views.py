from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/test.pt')
def my_view(request):
    return {'project': 'test'}

@view_config(route_name='index', renderer='templates/mytemplate.pt')
def index_view(request):
	return {'project': 'test'}
