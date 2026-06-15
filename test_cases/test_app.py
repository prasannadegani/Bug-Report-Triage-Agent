def test_critical_bug():
    assert classify_severity("Application crash on startup") == "Critical"

def test_high_bug():
    assert classify_severity("Server error while saving data") == "High"

def test_medium_bug():
    assert classify_severity("Search page is slow") == "Medium"

def test_low_bug():
    assert classify_severity("Minor UI issue") == "Low"

def test_authentication_login():
    assert classify_area("Login page not working") == "Authentication"

def test_authentication_password():
    assert classify_area("Password reset failed") == "Authentication"

def test_ui_area():
    assert classify_area("Submit button not visible") == "UI"

def test_performance_area():
    assert classify_area("Search results loading slowly") == "Performance"

def test_general_area():
    assert classify_area("Notification issue") == "General"

def test_clarification_required():
    assert clarification("Login failed") != "No clarification required"

def test_clarification_not_required():
    assert clarification(
        "Login page shows error after entering password"
    ) == "No clarification required"

def test_another_critical():
    assert classify_severity("System crash detected") == "Critical"
