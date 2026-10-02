import gcis

def test_energy_status():
    expected='Reading is Normal'
    actual=gcis.energy_status([0.01,0.10],0.06)
    assert expected==actual

def test_energy_status_boundry():
    expected='Reading is Normal'
    actual=gcis.energy_status([0.01,0.10],0.10)
    assert expected==actual

def test_energy_status_high():
    expected='Reading is High'
    actual=gcis.energy_status([0.01,0.10],0.12)
    assert expected==actual

def test_energy_status_critical():
    expected='Reading is Critical'
    actual=gcis.energy_status([0.01,0.10],0.3)
    assert expected==actual

def test_energy_status_invalid():
    expected='Reading is Low/Invalid'
    actual=gcis.energy_status([0.01,0.10],-2.00)
    assert expected==actual

def test_energy_cost():
    expected=1.5
    actual=gcis.energy_cost(5.0,0.3)
    assert expected==actual

def test_attention_normal():
    expected=False
    actual=gcis.attention('Reading is Normal')
    assert expected==actual

def test_attention_high():
    expected=True
    actual=gcis.attention('Reading is High')
    assert expected==actual

def test_unknown_device():
    expected='Unknown Device!'
    actual=gcis.check_range('Fan')
    assert expected==actual


test_energy_status()
test_energy_status_boundry()
test_energy_status_high()
test_energy_status_critical()
test_energy_status_invalid()
test_energy_cost()

test_attention_normal()
test_attention_high()

test_unknown_device()