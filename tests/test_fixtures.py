"""
Сделайте разные фикстуры для каждого теста
"""
from selene.support.shared import browser
from selene import have


def test_github_desktop(browser_settings_desktop):
    browser.element('a[href="/login"]').click()
    assert browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_settings_mobile):
    browser.element('div>[aria-label="Toggle navigation"]').click()
    browser.element('[href="/login"]').click()
    assert browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))
