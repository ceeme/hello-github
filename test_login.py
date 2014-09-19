from splinter import Browser

def test_login(browser): #Todo -parameterize for diff logins with diff roles
    """Go to login page, login,verify and logout""" #Todo - handle potential popups
    browser.visit('https://master-cmm.integration.covermymeds.com/')
    assert browser.is_element_present_by_name('username'),'Could not reach login'
    browser.type('username','Vlad') #Todo - wrap in try except finally
    browser.type('plaintext_password','Impaler!')
    browser.execute_script('document.login.submit()')
    if browser.is_text_present("Logged in as"): print 'Successfully logged in'
    browser.click_link_by_href('https://master-cmm.integration.covermymeds.com/user/logout')
    assert browser.is_element_present_by_name('plaintext_password'),'Did not successfully logout'


if __name__=="__main__":
    browser = Browser()
    test_login(browser)
    browser.quit()
