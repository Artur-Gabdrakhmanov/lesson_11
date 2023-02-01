"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have
from selene.support.shared import browser


def test_github_desktop(browser_settings_skip):
    size = browser_settings_skip
    if size == 'mobile':
        pytest.skip('Этот тест для ДЕСКТОПНОЙ версии')
    browser.element('a[href="/login"]').click()
    browser.element('[class="auth-form-body mt-3"]').should(have.text('Password'))


def test_github_mobile(browser_settings_skip):
    size = browser_settings_skip
    if size == 'desktop':
        pytest.skip('Этот тест для МОБИЛЬНОЙ версии')
    browser.element('[class="Button-label"]').click()
    browser.element('a[href="/login"]').click()
    browser.element('[class="auth-form-body mt-3"]').should(have.text('Password'))
