import pytest
from selene.support.shared import browser

@pytest.fixture(params=['desktop', 'mobile'])
def browser_settings_skip(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844
    browser.open('https://github.com')
    return request.param



@pytest.fixture(params=['desktop', 'mobile'])
def browser_settings(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844
    browser.open('https://github.com')



@pytest.fixture
def browser_settings_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com')
    yield
    browser.quit()


@pytest.fixture
def browser_settings_mobile():
    browser.config.window_width = 390
    browser.config.window_height = 844
    browser.open('https://github.com')
    yield
    browser.quit()
