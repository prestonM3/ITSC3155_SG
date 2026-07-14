from fastapi.testclient import TestClient

from main import app 

client = TestClient(app)

# define a test function for reasding a specific sheep 
def test_read_sheep(): 
    # Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (OK) 
    assert response.status_code == 200 

    # Assert that the response JSON matches the expected data
    assert response.json() == {
        # Expected JSON structure 
        "id": 1, 
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

# Define a test function for adding a new sheep  
def test_add_sheep():
    # 1. Define the new sheep data (using a Babydoll sheep as suggested)
    new_sheep_data = {
        "id": 8,  
        "name": "Barnaby",
        "breed": "Babydoll",
        "sex": "ram"
    }

    # 2. Send the POST request to the /sheep endpoint
    # As the assignment noted, we use the keyword json=new_sheep_data
    response = client.post("/sheep", json=new_sheep_data)

    # 3. Assert that the request was successful 
    # (201 Created is standard for POST, but 200 OK is also common depending on your main.py)
    assert response.status_code == 201