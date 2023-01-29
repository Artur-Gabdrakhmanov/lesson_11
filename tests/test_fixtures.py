"""
Сделайте разные фикстуры для каждого теста
"""
import pytest
from selene.support.shared import browser
from selene import have

@pytest.fixture
def config_desktop():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()


@pytest.fixture
def config_mobile():
    browser.config.window_height = 828
    browser.config.window_width = 1792
    yield
    browser.quit()


def test_github_desktop(config_desktop):
    browser.open('https://github.com')
    browser.element('[href="/login"]').click()
    assert browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))
    pass


def test_github_mobile(config_mobile):
    browser.open('https://github.com')
    browser.element('[href="/login"]').click()
    assert browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))
    pass
