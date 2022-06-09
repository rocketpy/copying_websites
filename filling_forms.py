from pywebcopy.configs import get_config


config = get_config('http://httpbin.org/')
wp = config.create_page()
wp.get(config['project_url'])
form = wp.get_forms()[0]
form.inputs['email'].value = 'email'
form.inputs['password'].value = 'psswrd'
wp.submit_form(form)
wp.get_links()
