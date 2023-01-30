"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene import have
from selene.support.shared import browser


@pytest.mark.parametrize('browser_settings', ['desktop'], indirect=True)
def test_github_desktop(browser_settings):
    browser.element('a[href="/login"]').click()
    browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))

@pytest.mark.parametrize('browser_settings', ['mobile'], indirect=True)
def test_github_mobile(browser_settings):
    browser.element('[class="Button-label"]').click()
    browser.element('a[href="/login"]').click()
    browser.element('[class="application-main "]').should(have.text('Password'))
