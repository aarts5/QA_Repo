browser.get("http://facebook.com")
name=browser.find_elements_by_id("email");
name.send_keys("pk158@hotmail.com");
[8:00:33 PM] sree pavan: p_wd=browser.find_elements_by_id("pass");
p_wd.send_keys("satya_pav123");
log_in=browser.find_element_by_id("u_0_f");
log_in.click();
