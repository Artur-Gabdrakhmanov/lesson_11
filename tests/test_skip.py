"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have
from selene.support.shared import browser


@pytest.mark.parametrize('width, height', [pytest.param(1920, 1080, id='window size 1920x1080'),
                                           pytest.param(390, 844, id='window size 390x844')
                                           ])
def test_github_desktop(browser_settings, width, height):
    if width == 390:
        pytest.skip('этот тест для десктопной версии')
    browser.driver.set_window_size(width, height)
    browser.element('a[href="/login"]').click()
    browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('width, height', [pytest.param(1920, 1080, id='window size 1920x1080'),
                                           pytest.param(390, 844, id='window size 390x844')
                                           ])
def test_github_mobile(browser_settings, width, height):
    if width == 1920:
        pytest.skip('этот тест для мобильной версии')
    browser.driver.set_window_size(width, height)
    browser.element('[class="Button-label"]').click()
    browser.element('a[href="/login"]').click()
    assert browser.element('[class="application-main "]').should(have.text('Password'))
