from httpx import AsyncClient


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/operations/", json={
        "id": 1,
        "quantity": "25.5",
        "figi": "figi_CODE",
        "instrument_type": "bond",
        "data": "2023-02-01T00:00:00",
        "type": "Something",
    })

    assert response.status_code == 200


async def test_get_specific_operations(ac: AsyncClient):
    res = await ac.get("/operations/", params={
        "operation_type": "Something",
    })

    assert res.status_code == 200
    assert res.json()["status"] == "success"
    assert len(res.json()["data"]) == 1
