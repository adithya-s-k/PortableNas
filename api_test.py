import requests

# assuming the server is running on localhost:8000

def test_root():
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_help():
    response = requests.get("http://localhost:8000/help")
    assert response.status_code == 200
    # assert that the response from the server is correctly parsed and handled

def test_logout():
    response = requests.get("http://localhost:8000/logout")
    assert response.status_code == 200
    # assert that the response from the server is correctly parsed and handled

def test_ls():
    response = requests.get("http://localhost:8000/ls")
    assert response.status_code == 200
    # assert that the response from the server is correctly parsed and handled

def test_cd():
    path = "/some/path"
    response = requests.get(f"http://localhost:8000/cd/{path}")
    assert response.status_code == 200
    # assert that the response from the server is correctly parsed and handled

def test_mkdir():
    path = "/some/path"
    response = requests.get(f"http://localhost:8000/mkdir/{path}")
    assert response.status_code == 200
    # assert that the response from the server is correctly parsed and handled

def test_rmdir():
    path = "/some/path"
    response = requests.get(f"http://localhost:8000/rmdir/{path}")
    assert response.status_code == 200
    # assert that the response from the server is correctly parsed and handled

def test_rm():
    path = "/some/file"
    response = requests.get(f"http://localhost:8000/rm/{path}")
    assert response.status_code == 200
    # assert that the response from the server is correctly parsed and handled

def test_upload():
    path = "/some/file"
    file_content = "some file content"
    response = requests.post(f"http://localhost:8000/upload/{path}", data=file_content)
    assert response.status_code == 200
    # assert that the response from the server is correctly parsed and handled


