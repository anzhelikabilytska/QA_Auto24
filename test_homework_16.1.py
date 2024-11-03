def test_team_lead_attributes():
    team_lead = TeamLead("Alice", 120000, "Engineering", "Python", 5)

    assert hasattr(team_lead, 'name'), "Attribute 'name' missing"
    assert hasattr(team_lead, 'salary'), "Attribute 'salary' missing"
    assert hasattr(team_lead, 'department'), "Attribute 'department' missing"
    assert hasattr(team_lead, 'programming_language'), "Attribute 'programming_language' missing"
    assert hasattr(team_lead, 'team_size'), "Attribute 'team_size' missing"

    print("All required attributes are present in TeamLead")

test_team_lead_attributes()
