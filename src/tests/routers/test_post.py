import pytest
from httpx import AsyncClient

# READ:
# 1. https://www.semrush.com/blog/http-status-codes/?kw=&cmp=BR_POR_SRCH_DSA_Blog_EN&label=dsa_pagefeed&Network=g&Device=c&utm_content=676514000793&kwid=dsa-2185834088336&cmpid=18361973175&agpid=153796425585&BU=Core&extid=105178164144&adpos=&gad_source=1&gclid=CjwKCAjw9IayBhBJEiwAVuc3fhaxgM4rEoH_Mmd7GNjmf5594GswOlQvnuIPkPxnPJSZo7xxgpRK5xoCynoQAvD_BwE

# ========================================
#           REGION: Functions
# ========================================

async def create_post(body: str, async_client: AsyncClient) -> dict:
    url = "/post"
    json = {"body": body}
    response = await async_client.post(url=url, json=json)
    return response.json()

async def create_comment(body: str, post_id: int, async_client: AsyncClient) -> dict:
    url = "/comment"
    json = {"body": body, "post_id": post_id}
    response = await async_client.post(url=url, json=json)

    return response.json()

# ========================================
#           REGION: Fixtures
# ========================================

@pytest.fixture()
async def created_post(async_client: AsyncClient) -> dict:
    return await create_post("Test Post", async_client)

@pytest.fixture()
async def created_comment(async_client: AsyncClient, created_post: dict) -> dict:
    return await create_comment("Test Comment", created_post["id"], async_client)

# ========================================
#           REGION: Test Cases
# ========================================

@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient) -> None:
    url = "/post"
    body = "Test Post"
    json = {"body": body}
    response = await async_client.post(url=url, json=json)

    assert response.status_code == 201
    assert {"id": 1, "body": body}.items() <= response.json().items()


@pytest.mark.anyio
async def test_create_post_missing_data(async_client: AsyncClient) -> None:
    url="/post"
    json = {}
    response = await async_client.post(url=url, json=json)

    assert response.status_code == 422

@pytest.mark.anyio
async def test_get_all_posts(async_client: AsyncClient, created_post: dict) -> None:
    url = "/post"
    response = await async_client.get(url=url)

    assert response.status_code == 200
    assert response.json() == [created_post]

@pytest.mark.anyio
async def test_create_comment(async_client: AsyncClient, created_post: dict) -> None:
    url = "/comment"
    body = "Test Comment"
    post_id = created_post["id"]
    json = {"body": body, "post_id": post_id}
    response = await async_client.post(url=url, json=json)

    assert response.status_code == 201
    assert {"id": 1, "body": body, "post_id": post_id}.items() <= response.json().items()


@pytest.mark.anyio
async def test_get_comments_on_post(
    async_client: AsyncClient,
    created_post: dict,
    created_comment: dict,
) -> None:
    post_id = created_post["id"]
    url = f"/post/{post_id}/comment"
    response = await async_client.get(url=url)

    assert response.status_code == 200
    assert response.json() == [created_comment]


@pytest.mark.anyio
async def test_get_comments_on_post_empty(async_client: AsyncClient, created_post: dict) -> None:
    post_id = created_post["id"]
    url = f"/post/{post_id}/comment"
    response = await async_client.get(url=url)

    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.anyio
async def test_get_post_with_comments(
    async_client: AsyncClient, created_post: dict, created_comment: dict
) -> None:
    post_id = created_post["id"]
    url = f"/post/{post_id}"
    response = await async_client.get(url=url)

    assert response.status_code == 200
    assert response.json() == {"post": created_post, "comments": [created_comment]}


@pytest.mark.anyio
async def test_get_missing_post_with_comments(
    async_client: AsyncClient, created_post: dict, created_comment: dict
) -> None:
    url = f"/post/2"
    response = await async_client.get(url=url)

    assert response.status_code == 404
