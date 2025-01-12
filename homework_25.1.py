xpaths = [
    "//button[text()='Log in']",
    "//h1[text()='Welcome to QAuto!']",

    "//input[@name='email']",
    "//input[@name='password']",
    "//button[@type='submit']",

    "//div[@class='form-group']/input[@id='password']",
    "//form[@class='login-form']//button[@type='submit']",

    "//div[@class='login-container']//h1",
    "//div[@class='login-container']//button[@type='submit']",

    "//button[contains(text(), 'Log')]",
    "//div[contains(@class, 'header')]",

    "//input[starts-with(@id, 'user')]",
    "//button[starts-with(@class, 'btn')]",

    "//ul/li[position()=1]",
    "//ul/li[position()=last()]",

    "//input[@type='text' and @name='email']",
    "//button[@type='submit' or @class='login-btn']",

    "//button[text()='Log in']/ancestor::div",
    "//input[@name='password']/ancestor::form",

    "//label[text()='Email']/following-sibling::input",
    "//label[text()='Password']/following-sibling::input",

    "//input[@id='email']/preceding-sibling::label",

    "//div[@class='login-container']/descendant::button[@type='submit']",

    "//button[@type='submit' and text()='Log in']/self::button"
]

css_selectors = [
    "input[name='email']",
    "input[name='password']",

    "#email",
    "#password",

    ".login-form",
    ".form-group input",

    ".login-container h1",
    ".login-container button[type='submit']",

    "form.login-form input#email",
    "form.login-form input#password",

    "input[type='text'][name='email']",
    "button[type='submit'][class*='btn']",

    "ul > li:first-child",
    "ul > li:last-child",

    "ul > li:nth-child(2)",
    "ul > li:nth-child(odd)",

    "label + input",
    "input ~ button",

    "[class^='btn']",
    "[class$='container']",
    "[class*='header']",

    "button:not([type='reset'])",

    "[type='submit']",
    "input[placeholder='Enter email']"
]

with open("locators.txt", "w", encoding="utf-8") as f:
    f.write("# XPath Locators\n")
    f.writelines([f"{xpath}\n" for xpath in xpaths])
    f.write("\n# CSS Selectors\n")
    f.writelines([f"{css}\n" for css in css_selectors])
